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

-   `collector` walks the node tree to find these div's and builds a lookup table
    in config["mccole"]["tables"] mapping slugs to multi-part table numbers.

-   `table_ref` uses that information to fill in table reference shortcodes of
    the form `[% t slug %]`.  It assumes there is a language defined by
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


@dataclass
class Table:
    """Keep track of information about a single table."""

    fileslug: str = ""
    slug: str = ""
    caption: str = ""
    number: tuple = ()


# Regular expressions to match table elements.
TABLE = re.compile(r'<div[^>]+class="table"[^>]*?>')
TABLE_CAPTION = re.compile(r'caption="(.+?)"')
TABLE_ID = re.compile(r'id="(.+?)"')
TABLE_DIV = re.compile(
    r'<div\s+caption="(.+?)"\s+class="table"\s+id="(.+?)">\s*<table>', re.DOTALL
)


@ivy.events.register(ivy.events.Event.INIT)
def collector():
    """Collect information about tables."""
    # Get per-node information.
    collected = {}
    ivy.nodes.root().walk(lambda node: _collect(node, collected))

    # Convert to flat lookup table.
    major = util.make_major()
    tables = util.make_config("tables")
    for fileslug in collected:
        if fileslug in major:
            for (i, entry) in enumerate(collected[fileslug]):
                entry.number = (str(s) for s in (major[fileslug], i + 1))
                tables[entry.slug] = entry


def _collect(node, collected):
    """Collect table information from a single node."""
    collected[node.slug] = []
    for (i, match) in enumerate(TABLE.finditer(node.text)):
        if (caption := TABLE_CAPTION.search(match.group(0))) is None:
            util.fail(f"Table div '{match.group(0)}' without caption in {node.filepath}")
        if (slug := TABLE_ID.search(match.group(0))) is None:
            util.fail(f"Table div '{match.group(0)}' without ID in {node.filepath}")
        collected[node.slug].append(
            Table(fileslug=node.slug, caption=caption.group(1), slug=slug.group(1))
        )


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
        return f'<div class="table"><table id="{slug}"><caption>{caption}</caption>'

    return TABLE_DIV.sub(_replace, text)
