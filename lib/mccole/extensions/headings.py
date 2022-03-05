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
