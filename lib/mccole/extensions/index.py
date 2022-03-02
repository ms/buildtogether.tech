"""Create index and index references.

Index entries are created using `[% i "some" "key" %]...text...[% /i %]`.  Keys
can use `major!minor` notation to create subheadings (LaTeX-style).

If some text is in both the glossary and the index, wrap the index shortcode
around the glossary shortcode:

    [% i "some" %][% g key %]some text[% /g %][% /i %]
"""

import re

import ivy
import shortcodes
import util

# Match the index marker in an HTML page.
INDEX_MARKER = re.compile(r"<!--\s*INDEX\s*-->")


@shortcodes.register("i", "/i")
def index_ref(pargs, kwargs, node, content):
    """Handle [% i "some" "key" %]...text...[% /i %] index shortcodes."""
    # Badly formatted.
    if len(pargs) == 0:
        util.fail(f"Badly-formatted 'i' shortcode {pargs} in {node.filepath}")

    # Store entries.
    index = util.make_config("index")
    for entry in [key.strip() for key in pargs]:
        entry = tuple(s.strip() for s in entry.split("!") if s.strip())
        if 1 <= len(entry) <= 2:
            index.setdefault(entry, set()).add(node.slug)
        else:
            util.fail(f"Badly-formatted index key {entry} in {node.filepath}")

    # Format.
    joined = ";".join(pargs)
    return f'<span class="indexref" key="{joined}" markdown="1">{content}</span>'


@ivy.events.register(ivy.events.Event.EXIT)
def make_index():
    """Rewrite the file containing the overall index."""
    # Find and rewrite the index file.
    def visitor(node):
        if node.slug == "contents":
            out_path = node.get_output_filepath()
            try:
                with open(out_path, "r") as reader:
                    content = reader.read()
                content = INDEX_MARKER.sub(_make_index(), content)
                with open(out_path, "w") as writer:
                    writer.write(content)
            except OSError:
                pass  # we are clearing Ivy's output so the file doesn't exist

    # Look for the node with the index file.
    ivy.nodes.root().walk(visitor)


def _make_index():
    # No entries.
    if not (content := util.get_config("index")):
        return ""

    # Format multi-level list.
    result = ['<ul class="indexlist">']
    previous = None
    for (current, occurrences) in sorted(content.items()):
        links = _make_links(occurrences)
        if len(current) == 1:
            result.append(f"<li>{current[0]}: {links}</li>")
            previous = current[0]
        elif len(current) != 2:
            util.fail(f"Internal error in index key {current}")
        else:
            if current[0] != previous:
                result.append(f"<li>{current[0]}</li>")
            result.append(f"<li>…{current[1]}: {links}</li>")
    result.append("</ul>")

    return "\n".join(result)


def _make_links(slugs):
    """Turn a set of node slugs into links."""
    # Too early in cycle.
    if not (headings := util.get_config("headings")):
        return ""

    # Match headings to slugs and format.
    paths = ["../" if not s else f"../{s}/" for s in slugs]
    titles = [headings[s].title for s in slugs]
    triples = list(zip(slugs, paths, titles))
    major = util.make_major()
    triples.sort(key=lambda x: str(major[x[0]]))
    result = ", ".join(f'<a href="{path}">{title}</a>' for (_, path, title) in triples)
    return result
