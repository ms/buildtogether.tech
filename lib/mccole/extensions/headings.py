"""Enumerate headings.

This code collects and numbers headings in source files, and provides
a shortcode for creating cross-references to them.

-   `[% x slug %]` creates a named cross-reference to a chapter, appendix,
    or section.  It requires names for these terms in `util.TRANSLATIONS`,
    and assumes cross-reference information has already been collected.

-   Rather than running the Markdown parser on each source file and looking
    for heading tokens, this code uses a regular expression to find
    headings with attribute lists containing IDs:

        ## Some Title {: #some-slug}

    These are numbered and stored in `config["mccole"]["headings"]` for
    later use, and the source text modified to include the numbering
    prior to HTML generation.  Note that page-level titles are taken from
    page metadata: there should not be an H1-level heading in the body
    of the page.
"""

import re
from dataclasses import dataclass

import ivy
import shortcodes
import util

# Match a Markdown heading with optional attributes.
HEADING = re.compile(r"^(#+)\s*(.+?)(\{:\s*#(.+\b)\})?$", re.MULTILINE)


@dataclass
class Heading:
    """Keep track of heading information."""

    fileslug: str = ""
    depth: int = 0
    title: str = ""
    slug: str = ""
    number: tuple = ()


@shortcodes.register("x")
def section_ref(pargs, kwargs, node):
    """Handle [% x slug %] section reference."""
    if len(pargs) != 1:
        util.fail(f"Badly-formatted 'x' shortcode {pargs} in {node.filepath}")

    headings = util.get_config("headings")

    slug = pargs[0]
    heading = headings[slug]
    label = util.make_label("part", heading.number)
    anchor = f"#{slug}" if (len(heading.number) > 1) else ""

    return f'<a href="@root/{heading.fileslug}/{anchor}">{label}</a>'


@ivy.events.register(ivy.events.Event.INIT)
def collector():
    """Enumerate headings.

    1. Find Markdown headings in pages and enumerate those with IDs.
    1. Modify Markdown headings to include numberings.
    1. Create config["mccole"]["headings"] for cross-referencing.
    1. Add "major" to page metadata so that templates can fill in H1 headings.
    """
    major = util.make_major()
    headings = _gather(major)
    _number(major, headings)
    _cross_reference(headings)
    _modify()


def _cross_reference(seen):
    """Create flat cross-reference table."""
    headings = util.make_config("headings")
    for group in seen.values():
        for entry in group:
            headings[entry.slug] = entry


def _gather(major):
    """Gather heading information from pages."""
    seen = {}

    # Collect data from a single node.
    def visitor(node):
        # Home page is untitled.
        if node.slug not in major:
            return

        # Use page metadata to create entry for level-1 heading.
        seen[node.slug] = [Heading(node.slug, 1, node.meta["title"], node.slug)]

        # Collect depth, text, and slug from each heading.
        seen[node.slug].extend(
            [
                Heading(node.slug, len(m.group(1)), m.group(2), m.group(4))
                for m in HEADING.finditer(node.text)
            ]
        )

    # Get information from each node.
    ivy.nodes.root().walk(visitor)
    return seen


def _modify():
    """Modify page content and metadata with collected information."""
    headings = util.get_config("headings")

    # Add text to headings with attributes.
    def patch(match):
        prefix = match.group(1)
        text = match.group(2)
        attributes = match.group(3) or ""
        slug = match.group(4)

        if slug is None:
            return f"{prefix} {text} {attributes}".rstrip()

        else:
            label = util.make_label("part", headings[slug].number)
            return f"{prefix} {label}: {text} {attributes}"

    # Replace level-2 headings and deeper while adding metadata for templates.
    def visitor(node):
        node.text = HEADING.sub(patch, node.text)
        if node.slug in headings:
            node.meta["major"] = util.make_label("part", headings[node.slug].number)

    # Act on each node.
    ivy.nodes.root().walk(visitor)


def _number(major, headings):
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
