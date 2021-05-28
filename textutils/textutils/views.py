from typing import Text
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse(f'''hello this is about page''')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    if removepunc == "on":
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        analyzed_text = ""
        for i in djtext:
            if i not in punc:
                analyzed_text = analyzed_text + i
        djtext = analyzed_text
        params = {'purpose':'Remove punctuations','analyzed_text': analyzed_text}

    if uppercase == 'on':
        analyzed_text = ""
        for i in djtext:
           analyzed_text =analyzed_text + i.upper()
        djtext = analyzed_text
        params = {'purpose':'upper case','analyzed_text': analyzed_text}

    if spaceremove == 'on':
        analyzed_text = ""
        for index, i in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed_text = analyzed_text + i
        params = {'purpose':'upper case','analyzed_text': analyzed_text}
        djtext = analyzed_text
    
    if newlineremover == 'on':
        analyzed_text = ""
        for i in djtext:
            if i != "\n" and i != "\r":
                analyzed_text = analyzed_text + i
        params = {'purpose':'upper case','analyzed_text': analyzed_text}
        djtext = analyzed_text

    if charcount == 'on':
        analyzed_text_no = len(djtext)
        params = {'purpose':'upper case','analyzed_text': analyzed_text_no}

    if(removepunc != "on" and newlineremover!="on" and spaceremove !="on" and uppercase!="on" and charcount != 'on'):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyzed.html', params)