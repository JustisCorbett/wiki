from django.shortcuts import render, redirect, reverse
from markdown2 import Markdown
from . import util
import random


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
        return redirect(reverse("entry", kwargs={"title":title}))

def edit(request, title):
    entry = util.get_entry(title)

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "entry": entry
    })

def ran_entry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)

    return redirect(reverse("entry", kwargs={"title":random_entry}))
