"""McCole extension utilities."""

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

# Configuration sections
CONFIGURATIONS = {
    "bibliography",  # bibliography entries
    "citations",  # references to bibliography entries
    "definitions",  # glossary definitions
    "figures",  # numbered figures
    "glossary",  # full glossary
    "headings",  # number chapter, section, and appendix headings
    "inclusions",  # included files
    "index",  # index entries
    "tables"  # numbered tables
}


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
    filler = filler if (filler is not None) else {}
    return ivy.site.config.setdefault("mccole", {}).setdefault(part, filler)


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
