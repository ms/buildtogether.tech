"""Manage links in Markdown files.

To keep links consistent between files, create a list `config["links"]`
of three-part tuples: a slug, a URL, and a short description.

-   The `[% links %]` shortcode turns this into an HTML table showing
    the descriptions and URLs.

-   `links_append` turns these into a Markdown links table:

        [slug-1]: url-1
        [slug-2]: url-2

    and appends it to the bottom of every `.md` file so that all links
    in Markdown pages can be written `[text][slug]`.
"""

import ivy
import shortcodes


@shortcodes.register("links")
def links_table(pargs, kwargs, node):
    """Create a table of links."""
    if "links" not in ivy.site.config:
        return ""

    links = "\n".join(
        [
            f'<tr><td>{title}</td><td><a href="{url}">{url}</a></td></tr>'
            for (_, url, title) in ivy.site.config["links"]
        ]
    )
    title = "<tr><th>Link</th><th>URL</th></tr>"
    return f'<table class="links-table">\n{title}\n{links}\n</table>'


@ivy.events.register(ivy.events.Event.INIT)
def links_append():
    """Add Markdown links table to Markdown files."""
    if "links" not in ivy.site.config:
        return

    links_table = "\n".join(
        f"[{slug}]: {url}" for (slug, url, _) in ivy.site.config["links"]
    )

    def visitor(node):
        if _needs_links(node):
            node.text += "\n\n" + links_table

    ivy.nodes.root().walk(visitor)


def _needs_links(node):
    """Markdown files and slides need links."""
    if node.ext == "md":
        return True
    if node.meta.get("template", None) == "slides":
        return True
    return False
