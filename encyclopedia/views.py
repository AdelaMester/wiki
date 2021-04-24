from django.shortcuts import render
from django.http import HttpResponse
import random
import re
from . import util



def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
})

def pages(request, title):
    return render(request, "encyclopedia/pages.html", {
        "pages": util.get_entry(title),
        "title_template":title
    })

def search(request):
    q = request.GET["q"]
    print(q)
    print(util.get_entry(q))
    if util.get_entry(q):
        return render(request, "encyclopedia/pages.html", {
        "pages": util.get_entry(q),
        "title_template": q
    })

    matchedEntries = []
    for pages in util.list_entries():
        if q in pages:
            matchedEntries.append(pages)

    if matchedEntries:
        return render(request, "encyclopedia/search_result.html", {
            "pages": matchedEntries,
        })
    else:
        return render(request, "encyclopedia/search_results.html", {
            "pages": pages
        })

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")


    title = request.GET["newtitle"]
    print(title)
    matchedTitles = []
    if util.get_entry(title):
        return render(request, "encyclopedia/error.html", {
        "pages": util.get_entry(title),
        "title_template": title
    })
    
    for pages in util.list_entries( title):
        if newtitle in pages:
            return render(request, "encyclopedia/error.html")

    if matchedTitles:
        return render(request, "encyclopedia/new_page.html", {
            "pages": pages
        })

    if request.method == "POST":
        title = request.POST['newTitle']
        content = request.POST['newPage']
        util.save_entry(title, content)
        return render(request, "encyclopedia/pages.html", {
            "pages": util.get_entry(title),
            "title_template": title
        })









