import os
import sys

import expressionive.expressionive as xpres
from expressionive.expressionive import htmltags as T

def page_text(page_contents,
              title=None,
              style_text="",
              script_text="",
              stylesheet=None,
              ):
    """Return the text of an expressionive page.

    The page contents are given as an expressionive expression,
    and the stylesheet and scripts as strings."""
    head = [T.meta(charset='utf-8')]
    if stylesheet:
        head.append(T.meta(rel='stylesheet',
                           type_='text/css',
                           href=stylesheet))
    if title:
        head.append(T.title[title])
    return xpres.Serializer(xpres.examples_vmap, 'utf-8').serialize(
        xpres.HTML5Doc([xpres.safe_unicode(style_text
                                           + script_text),
                        page_contents],
                       head=T.head[head]))

def file_contents(filename):
    """Return the contents of a file."""
    if os.path.isfile(filename):
        with open(filename) as instream:
            return instream.read()
    return f"File {filename} not found"

def tagged(tag, text):
    """Surround some text with opening and closing HTML tags."""
    return "<" + tag + ">" + text + "</" + tag + ">"

def tagged_file_contents(tag, filename):
    """Return the contents of a file, wrapped with begin and end tags.
    Can be used to include stylesheets and scripts in web pages."""
    return tagged(tag, file_contents(filename))
