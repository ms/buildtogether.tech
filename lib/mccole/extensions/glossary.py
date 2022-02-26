"""Create glossary and glossary references.

Glossary data is stored in a [Glosario](https://glosario.carpentries.org/)-format
file referenced by config["glossary"].

-   `glossary_ref` turns `[% g key "some text" %]` into a glossary reference.
    (The generated HTML assumes that the glossary is in `@root/glossary/index.html`.)

-   `glossary` turns `[% glossary %]` into an HTML glossary.  It requires a
    configuration key `config["lang"]`, and expects every glossary entry to have
    a definition keyed by that language.
"""

import re

import ivy
import shortcodes
import util
import yaml

# Regex to turn multiple spaces in glossary definition body into single space.
MULTISPACE = re.compile(r"\s+", re.DOTALL)

# Regex to extract internal cross-references from bodies of definitions.
INTERNAL_REF = re.compile(r'\]\(#(.+?)\)')


@shortcodes.register("g")
def glossary_ref(pargs, kwargs, node):
    """Handle [% g slug "text" %] glossary reference shortcodes."""
    if len(pargs) != 2:
        util.fail(f"Badly-formatted 'g' shortcode {pargs} in {node.filepath}")

    definitions = util.make_config("definitions", set())
    slug, text = pargs
    definitions.add(slug)

    return f'<a class="glossref" href="@root/glossary/#{slug}" markdown="1">{text}</a>'


@shortcodes.register("glossary")
def glossary(pargs, kwargs, node):
    """Convert glossary to Markdown."""
    if "glossary" not in ivy.site.config:
        return '<p class="warning">No glossary specified.</p>'
    if "lang" not in ivy.site.config:
        return '<p class="warning">No language specified.</p>'

    with open(ivy.site.config["glossary"], "r") as reader:
        glossary = yaml.safe_load(reader) or {}
    lang = ivy.site.config["lang"]

    try:
        glossary.sort(key=lambda x: x[lang]["term"].lower())
    except KeyError as exc:
        util.fail(f"Glossary entry or entries missing key, term, or {lang}: {exc}.")

    util.make_config("glossary", glossary)

    lookup = {entry["key"]: entry[lang]["term"] for entry in glossary}
    result = "\n\n".join(_as_markdown(lookup, lang, entry) for entry in glossary)
    return result


@ivy.events.register(ivy.events.Event.EXIT)
def check():
    glossary = util.get_config("glossary")
    glossary_keys = {entry["key"] for entry in glossary}

    lang = ivy.site.config["lang"]
    definitions = util.get_config("definitions")
    definitions |= _internal_references(glossary, lang)

    util.report("unknown glossary references", definitions - glossary_keys)
    util.report("unused glossary entries", glossary_keys - definitions)


def _as_markdown(lookup, lang, entry):
    """Convert a single glossary entry to Markdown."""
    first = f'<span class="glosskey" id="{entry["key"]}">{entry[lang]["term"]}</span>'

    if "acronym" in entry[lang]:
        first += f" ({entry[lang]['acronym']})"

    body = MULTISPACE.sub(entry[lang]["def"], " ").rstrip()

    if "ref" in entry[lang]:
        seealso = util.TRANSLATIONS[lang]["seealso"]
        try:
            refs = [f"[{lookup[r]}](#{r})" for r in entry[lang]["ref"]]
        except KeyError as exc:
            util.fail(f"Unknown glossary cross-reference key in {entry['key']}: {exc}")
        body += f"<br/>{seealso}: {', '.join(refs)}."

    result = f"{first}\n:   {body}"
    return result


def _internal_references(glossary, lang):
    """Get all cross-references from body of glossary entries."""
    result = set()
    for entry in glossary:
        for match in INTERNAL_REF.finditer(entry[lang]["def"]):
            result.add(match.group(1))
    return result
