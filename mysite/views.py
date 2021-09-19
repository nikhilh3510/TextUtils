from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    newlineremover = request.POST.get('newlineremover', 'default')
    spaceremover = request.POST.get('spaceremover', 'default')
    charcounter = request.POST.get('charcounter', 'default')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for char in djtext:
            if char !=" ":
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcounter == "on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcounter != "on"):
        return HttpResponse("ERROR")
    else:
        return render(request, 'analyze.html', params)


def capfirst(request):
    return HttpResponse("Capitalize First")
