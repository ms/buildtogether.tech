from dataclasses import dataclass

import ivy
import shortcodes
import util


@dataclass
class Heading:
    """Keep track of heading information."""

    fileslug: str = ""
    depth: int = 0
    title: str = ""
    slug: str = ""
    number: tuple = ()


@dataclass
class Table:
    """Keep track of information about a single table."""

    fileslug: str = ""
    slug: str = ""
    caption: str = ""
    number: tuple = ()


@ivy.events.register(ivy.events.Event.INIT)
def collect_regexp():
    """Collect information using regular expressions."""
    major = util.make_major()
    collected = {"headings": {}, "tables": {}}
    ivy.nodes.root().walk(lambda node: _parse_regexp(node, major, collected))

    _flatten_tables(collected["tables"])

    _number_headings(major, collected["headings"])
    _flatten_headings(collected["headings"])
    ivy.nodes.root().walk(_modify_headings)


def _parse_regexp(node, major, collected):
    """Collect table information from a single node."""
    _process_headings(node, major, collected["headings"])
    _process_tables(node, collected["tables"])


def _process_headings(node, major, headings):
    # Home page is untitled.
    if node.slug not in major:
        return

    # Use page metadata to create entry for level-1 heading.
    try:
        title = node.meta["title"]
    except KeyError:
        util.fail(f"No title in metadata of {node.filepath}")
    headings[node.slug] = [Heading(node.slug, 1, title, node.slug)]

    # Collect depth, text, and slug from each heading.
    headings[node.slug].extend(
        [
            Heading(node.slug, len(m.group(1)), m.group(2), m.group(4))
            for m in util.HEADING.finditer(node.text)
        ]
    )


def _number_headings(major, headings):
    """Calculate heading numberings."""
    for slug in major:
        stack = [major[slug]]
        for entry in headings[slug]:
            depth = entry.depth

            # Level-1 heading is already in the stack.
            if depth == 1:
                pass

            # Deeper heading, so extend stack.
            elif depth > len(stack):
                while len(stack) < depth:
                    stack.append(1)

            # Heading at the same level, so increment.
            elif depth == len(stack):
                stack[-1] += 1

            # Shallower heading, so shrink stack and increment.
            elif depth < len(stack):
                stack = stack[:depth]
                stack[-1] += 1

            # Record number as tuple of strings.
            entry.number = tuple(str(s) for s in stack)


def _flatten_headings(collected):
    """Create flat cross-reference table."""
    headings = util.make_config("headings")
    for group in collected.values():
        for entry in group:
            headings[entry.slug] = entry


def _modify_headings(node):
    node.text = util.HEADING.sub(_patch_heading, node.text)
    headings = util.get_config("headings")
    if node.slug in headings:
        node.meta["major"] = util.make_label("part", headings[node.slug].number)


def _patch_heading(match):
    """Modify a single heading."""
    headings = util.get_config("headings")
    prefix = match.group(1)
    text = match.group(2)
    attributes = match.group(3) or ""
    slug = match.group(4)

    if slug is None:
        return f"{prefix} {text} {attributes}".rstrip()
    else:
        label = util.make_label("part", headings[slug].number)
        return f"{prefix} {label}: {text} {attributes}"


def _process_tables(node, tables):
    """Collect table information."""
    tables[node.slug] = []
    for (i, match) in enumerate(util.TABLE.finditer(node.text)):
        if (caption := util.TABLE_CAPTION.search(match.group(0))) is None:
            util.fail(
                f"Table div '{match.group(0)}' without caption in {node.filepath}"
            )
        if (slug := util.TABLE_ID.search(match.group(0))) is None:
            util.fail(f"Table div '{match.group(0)}' without ID in {node.filepath}")
        tables[node.slug].append(
            Table(fileslug=node.slug, caption=caption.group(1), slug=slug.group(1))
        )


def _flatten_tables(collected):
    """Convert collected table information to flat lookup table."""
    major = util.make_major()
    tables = util.make_config("tables")
    for fileslug in collected:
        if fileslug in major:
            for (i, entry) in enumerate(collected[fileslug]):
                entry.number = (str(major[fileslug]), str(i + 1))
                tables[entry.slug] = entry
