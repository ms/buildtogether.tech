"""McCole extension utilities."""

import os
import re
import sys

import ivy

# Multilingual terms.
TRANSLATIONS = {
    "en": {
        "appendix": "Appendix",
        "chapter": "Chapter",
        "figure": "Figure",
        "seealso": "See also",
        "section": "Section",
        "table": "Table",
    },
    "es": {
        "appendix": "Anexo",
        "chapter": "Capítulo",
        "figure": "Figura",
        "seealso": "Ver también",
        "section": "Sección",
        "table": "Tabla",
    },
}

# Configuration sections and default values.
CONFIGURATIONS = {
    "bibliography": set(),  # bibliography entries
    "citations": set(),  # references to bibliography entries
    "definitions": set(),  # glossary definitions
    "figures": {},  # numbered figures
    "glossary": [],  # full glossary
    "headings": {},  # number chapter, section, and appendix headings
    "inclusions": {},  # included files
    "index": {},  # index entries
    "links": [],  # links table entries
    "tables": {},  # numbered tables
}

# Regex to turn multiple spaces in glossary definition body into single space.
MULTISPACE = re.compile(r"\s+", re.DOTALL)


def fail(msg):
    """Stop processing with an error message."""
    sys.exit(msg)


def get_config(part):
    """Get configuration subsection or None."""
    if part not in CONFIGURATIONS:
        fail(f"Unknown configuration section '{part}'")
    mccole = ivy.site.config.setdefault("mccole", {})
    return mccole.get(part, None)


def make_config(part, filler=None):
    """Make configuration subsection."""
    if part not in CONFIGURATIONS:
        fail(f"Unknown configuration section '{part}'")
    filler = filler if (filler is not None) else CONFIGURATIONS[part]
    return ivy.site.config.setdefault("mccole", {}).setdefault(part, filler)


def make_copy_paths(node, filename):
    """Make source and destination paths for copying."""
    src = os.path.join(os.path.dirname(node.filepath), filename)
    dst = os.path.join(os.path.dirname(node.get_output_filepath()), filename)
    return src, dst


def make_label(kind, number):
    """Create a figure label with a name and number."""
    translations = TRANSLATIONS[ivy.site.config["lang"]]
    if kind == "figure":
        name = translations["figure"]
    elif kind == "part":
        if len(number) > 1:
            name = translations["section"]
        elif number[0].isdigit():
            name = translations["chapter"]
        else:
            name = translations["appendix"]
    elif kind == "table":
        name = translations["table"]
    else:
        fail(f"Unknown kind of label {kind}")

    number = ".".join(number)
    return f"{name} {number}"


def make_major():
    """Construct major numbers/letters based on configuration."""
    chapters = {slug: i + 1 for (i, slug) in enumerate(ivy.site.config["chapters"])}
    appendices = {
        slug: chr(ord("A") + i)
        for (i, slug) in enumerate(ivy.site.config["appendices"])
    }
    return chapters | appendices


def report(title, items):
    if not items:
        return
    print(title)
    for item in sorted(items):
        print(f"- {item}")
