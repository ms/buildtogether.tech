#!/usr/bin/env python

'''Check the structure of the generated HTML.'''


import sys
import bs4

import utils


KNOWN = {
    'a': {
        'aria-label': None,
        'class': {'doi', 'dropdown-item'},
        'href': None,
        'title': None
    },
    'blockquote': {},
    'body': {
        'class': {'draft'}
    },
    'br': {},
    'caption': {},
    'cite': {},
    'code': {
        'class': {
            'language-html',
            'language-js',
            'language-make',
            'language-out',
            'language-py',
            'language-sh',
            'language-txt',
            'language-yml'
        }
    },
    'dd': {
        'class': None
    },
    'div': {
        'class': {
            'glossary',
            'callout',
            'centered',
            'container',
            'content',
            'dropdown',
            'dropdown-content',
            'file-link',
            'terms'
        },
        'id': None
    },
    'dl': {
        'class': {
            'bibliography',
            'glossary'
        }
    },
    'dt': {
        'class': {
            'bibliography',
            'glossary'
        },
        'id': None
    },
    'em': {},
    'figcaption': {},
    'figure': {
        'class': None,
        'id': None,
        'slug': None
    },
    'footer': {},
    'h1': {
        'class': {
            'landing-title',
            'nochaptertitle',
            'page-title'
        },
        'slug': None
    },
    'h2': {
        'class': {
            'landing-subtitle'
        },
        'id': None
    },
    'h3': {
        'id': None
    },
    'head': {},
    'header': {},
    'hr': {},
    'html': {
        'lang': {
            'en'
        }
    },
    'i': {
        'aria-hidden': None,
        'class': None
    },
    'img': {
        'alt': None,
        'class': {
            'iconlink'
        },
        'src': None
    },
    'li': {},
    'link': {
        'href': None,
        'rel': {
            'icon',
            'shortcut',
            'stylesheet',
            'image/x-icon',
            'text/css'
        },
        'type': None
    },
    'main': {},
    'meta': {
        'charset': None,
        'content': None,
        'name': None
    },
    'nav': {
        'class': {
            'nav-main'
        }
    },
    'ol': {},
    'p': {
        'class': {
            'continue'
        }
    },
    'pre': {
        'class': None,
        'title': None
    },
    'script': {
        'async': None,
        'crossorigin': None,
        'src': None,
        'type': None
    },
    'small': {},
    'span': {
        'class': {
            'copyright',
            'navtitle',
            'nowrap'
        },
        'f': None,
        'g': None,
        'i': None,
        't': None,
        'x': None
    },
    'strong': {},
    'table': {
        'class': {
            'links'
        },
        'id': None
    },
    'tbody': {},
    'td': {
        'style': None
    },
    'th': {
        'style': None
    },
    'thead': {},
    'time': {
        'datetime': None
    },
    'title': {},
    'tr': {},
    'ul': {
        'class': {
            'toc'
        }
    }
}


def check_dom(options):
    '''Main driver.'''
    problems = {}
    for filename in options.sources:
        with open(filename, 'r') as reader:
            doc = bs4.BeautifulSoup(reader, features='lxml')
            for node in doc.descendants:
                if isinstance(node, bs4.element.Tag):
                    check(problems, filename, node)
    report(problems)


def check(problems, filename, node):
    '''Check individual element.'''
    if node.name not in KNOWN:
        problems[node.name] = f'unknown ({filename})'
        return
    for attr in node.attrs:
        if attr not in KNOWN[node.name]:
            if node.name not in problems:
                problems[node.name] = []
            problems[node.name].append(f'unknown attribute "{attr}" in {filename}')
        elif KNOWN[node.name][attr] is not None:
            values = node[attr] if isinstance(node[attr], list) else [node[attr]]
            for value in values:
                if value not in KNOWN[node.name][attr]:
                    if node.name not in problems:
                        problems[node.name] = []
                    problems[node.name].append(f'"{attr}" has unknown value "{value}" in {filename}')


def report(problems):
    '''Report results.'''
    if not problems:
        return
    print('- DOM')
    for name in sorted(problems.keys()):
        print(f'  - {name}')
        for problem in problems[name]:
            print(f'    - {problem}')


if __name__ == '__main__':
    options = utils.get_options(
        ['--sources', True, 'List of input files']
    )
    check_dom(options)
