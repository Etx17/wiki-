from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    entryPage = util.get_entry(entry)
    
    if entryPage is None:
        return render(request, "encyclopedia/notfound.html", {
            "entryTitle": entry
        })
            
    else:
        return render(request, "encyclopedia/entry.html", { 
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry 
        })