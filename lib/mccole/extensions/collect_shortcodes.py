from dataclasses import dataclass

import ivy
import shortcodes
import util


@dataclass
class Figure:
    """Keep track of information about a figure."""

    node: ivy.nodes.Node = None
    fileslug: str = ""
    slug: str = ""
    img: str = ""
    alt: str = ""
    caption: str = ""
    number: tuple = ()
    width: str = ""


@ivy.events.register(ivy.events.Event.INIT)
def collect_shortcodes():
    """Collect information by parsing shortcodes."""
    parser = shortcodes.Parser(inherit_globals=False, ignore_unknown=True)
    parser.register(_process_figure, "figure")
    parser.register(_process_index, "i", "/i")

    collected = {"figures": {}, "index": util.make_config("index")}
    ivy.nodes.root().walk(lambda node: _parse_shortcodes(node, parser, collected))

    _flatten_figures(collected["figures"])


def _parse_shortcodes(node, parser, collected):
    """Collect information from node."""
    seen = {"node": node, "figures": [], "index": collected["index"]}
    parser.parse(node.text, seen)
    collected["figures"][node.slug] = seen["figures"]


def _process_figure(pargs, kwargs, seen):
    """Collect information from a single figure shortcode."""
    seen["figures"].append(Figure(seen["node"], **kwargs))
    return ""


def _process_index(pargs, kwargs, extra, content):
    """Gather information from a single index shortcode."""
    node = extra["node"]
    accum = extra["index"]
    if not pargs:
        util.fail(f"Empty index key in {node.filepath}")
    for entry in [key.strip() for key in pargs]:
        entry = util.MULTISPACE.sub(" ", entry)
        entry = tuple(s.strip() for s in entry.split("!") if s.strip())
        if 1 <= len(entry) <= 2:
            accum.setdefault(entry, set()).add(node.slug)
        else:
            util.fail(f"Badly-formatted index key {entry} in {node.filepath}")


def _flatten_figures(collected):
    """Convert collected figures information to flat lookup table."""
    major = util.make_major()
    figures = util.make_config("figures")
    for fileslug in collected:
        if fileslug in major:
            for (i, entry) in enumerate(collected[fileslug]):
                entry.fileslug = fileslug
                entry.number = (str(major[fileslug]), str(i + 1))
                figures[entry.slug] = entry
