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
    keyword = request.GET.get("q", "")
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

def new_page(request):
    return render(request, "encyclopedia/newpage.html")

def save_page(request):
    title = request.POST.get("title", "")
    entry = request.POST.get("entry", "")

    if not title:
        message = "Error: Please enter a title when making a new entry."
        return render(request, "encyclopedia/result.html", {
            "message": message
        })
    elif not entry:
        message = "Error: Blank entry is not allowed."
        return render(request, "encyclopedia/result.html", {
            "message": message
        })
    else:
        util.save_entry(title, entry)
        message = "Success: Entry was successfully saved."
        return render(request, "encyclopedia/result.html", {
            "message": message
        })