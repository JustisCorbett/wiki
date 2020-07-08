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

def search(request):
    keyword = request.GET.get('q', '')
    match = util.get_entry(keyword)

    if not match:
        entries = util.list_entries()
        res = [i for i in entries if keyword in i]
        return render(request, "encyclopedia/search.html", {
            "results": res
        })
    else:
        return render(request, "encyclopedia/search.html", {
            "results": match
        })

def newPage