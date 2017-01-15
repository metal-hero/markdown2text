import re

MARKDOWN2TEXT = [
    ('!\[', ''),  # remove images
    ('\](.*)', ''),  # remove images and links
    ('\]\[.*\]', ''),  # remove links
    ('[\[\]]', ''),  # remove brackets

    ('~~', ''),  # remove strikethrough texts
    ('---', '\n'),  # replace separated lines to "new line"
    ('(\n\s*|^\s*)\*\s+', '\n• '),  # replace all list "*" to •
    ('[#_*]', ''),  # remove # _ (h1,h2,h3 etc. and **___(bold, italic))
    ('(\n\s*|^\s*)>+', '\n\t'),  # replace "tabular" to "new line" and "tab"
]


def convert(mkdown=''):
    '''
    This function convert markdown text to simple text
    without Bold, Italic, Lists and so on
    :param mkdown:
    :return:
    '''
    for i in MARKDOWN2TEXT:
        mkdown = re.sub(i[0], i[1], mkdown)
    return mkdown
