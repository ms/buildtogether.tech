"""Ivy configuration."""

# Theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {"extensions": ["markdown.extensions.extra"]}

# Site title.
title = "Building Software Together"

# Output directory.
out_dir = "docs"

# GitHub repository.
github = "https://github.com/gvwilson/buildtogether.tech.git"

# Published domain.
domain = "buildtogether.tech"

# Site logo.
logo = "files/codebender.svg"

# Use "a/" URLs instead of "a.html".
extension = "/"

# Language code.
lang = "en"

# Chapter and appendix slugs in order.
chapters = [
    "introduction",
    "important",
    "starting",
    "teams",
    "rules-persuade",
    "conflict",
    "git-solo",
    "git-team",
    "ip",
    "communicate",
    "testing",
    "design",
    "security",
    "errors",
    "debugging",
    "automation",
    "tooling",
    "rules-comfortable",
    "process",
    "rules-joining",
    "rules-newcomers",
    "research",
    "rules-research",
    "fairness",
    "rules-fired",
    "delivery",
    "rules-handover",
    "conclusion"
]
appendices = [
    "license",
    "bibliography",
    "conduct",
    "contributing",
    "glossary",
    "thinking",
    "methods",
    "onboarding",
    "project-eval",
    "personal-eval",
    "reading",
    "rules-freelance",
    "rules-change",
    "authors"
]

# BibTeX bibliography file and style.
bibliography = "bibliography.bib"
bibliography_style = "unsrt"

# Glossary definitions.
glossary = "glossary.yml"

# Link table file.
links = "links.yml"

# Footer entries are (link, title).
footer = [
    ("@root/license/", "License"),
    ("@root/conduct/", "Code of Conduct"),
    ("@root/bibliography/", "Bibliography"),
    ("@root/glossary/", "Glossary"),
    ("@root/links/", "Links"),
    (github, "GitHub"),
]
