from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('textarea')

    removePunctuation = request.GET.get('removePunc', 'defualt')
    capitalize = request.GET.get('capitalize', 'defualt')
    remspace = request.GET.get('removespaces', 'defualt')

    if removePunctuation == 'on':
        symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzedText = ""
        for i in text:
            if i not in symbols or i==' ':
                analyzedText += i
        text = analyzedText

    if remspace == 'on':
        analyzedText = ""
        for i in range(len(text)):
            if text[i] == ' ' and text[i+1] == ' ':
                continue
            analyzedText += text[i]
        text = analyzedText

    print(capitalize)
    if capitalize == 'on':
        text = text.title()

    if text == "":
        text = "NO TEXT ENTERED BY USER"

    return render(request, 'analyze.html', {'text': text})
