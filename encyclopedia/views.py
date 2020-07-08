from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    
    if not entry:
        html = None
    else:
        html = Markdown().convert(entry)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "html": html
    })

