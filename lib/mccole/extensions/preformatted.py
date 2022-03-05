"""Modify preformatted blocks to display correctly."""

import re

import ivy

CODE_BLOCK = re.compile(r'<pre><code\s+class="(language-.+?)">')


@ivy.filters.register(ivy.filters.Filter.NODE_HTML)
def code_blocks(text, node):
    """Copy the class from '<pre><code class="language-x">' into the '<pre>'.

    This is needed so that background colors will fill the whole block,
    not just work line by line.
    """

    def _replace(match):
        lang = match.group(1)
        return f'<pre class="{lang}"><code class="{lang}">'

    return CODE_BLOCK.sub(_replace, text)
