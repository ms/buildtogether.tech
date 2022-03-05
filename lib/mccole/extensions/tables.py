"""Handle tables.

In a better world than this, tables would be represented in Markdown as:

    | a | b |
    | - | - |
    | 1 | 2 |
    {: #slug caption="Some words"}

However, the Markdown parser doesn't seem to accept attribute lists on tables,
so instead tables are represented as:

    <div class="table" id="slug" caption="Some words" markdown="1">
    | a | b |
    | - | - |
    | 1 | 2 |
    </div>

-   `table_ref` uses collected information to fill in table reference shortcodes
    of the form `[% t slug %]`.  It assumes there is a language defined by
    `config["lang"]` that matches a language in `util.TRANSLATIONS`

-   `table_caption` modifies the generated HTML to turn:

        <div class="table" id="slug" caption="Some words">
        <table>
        ...
        </table>
        </div>

    into:

        <div class="table">
        <table id="slug">
        <caption>Some words</caption>
        ...
        </table>
        </div>
"""

import re
from dataclasses import dataclass

import ivy
import shortcodes
import util


@shortcodes.register("t")
def table_ref(pargs, kwargs, node):
    """Handle [% t slug %] table reference."""
    # Shortcode used improperly.
    if len(pargs) != 1:
        util.fail(f"Badly-formatted 't' shortcode {pargs} in {node.filepath}")

    # Haven't collected information yet.
    if (tables := util.get_config("tables")) is None:
        return ""

    # Create cross-reference.
    slug = pargs[0]
    if slug not in tables:
        util.fail(f"Unknown table cross-reference slug {slug} in {node.filepath}")
    table = tables[slug]
    label = util.make_label("table", table.number)
    return f'<a class="tblref" href="@root/{table.fileslug}/#{slug}">{label}</a>'


@ivy.filters.register(ivy.filters.Filter.NODE_HTML)
def table_caption(text, node):
    """Get the caption in the right place."""

    def _replace(match):
        caption = match.group(1)
        slug = match.group(2)
        table = util.get_config("tables")[slug]
        label = util.make_label("table", table.number)
        return f'<div class="table"><table id="{slug}"><caption>{label}: {caption}</caption>'

    return util.TABLE_DIV.sub(_replace, text)
