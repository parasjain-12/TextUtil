from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dic = {'name': 'Paras Jain', 'place': "Venus"}
    return render(request, "index.html", dic)

def analyze(request):
    # Get the Text
    text = request.POST.get("text", "default")
    # Get the checkbox values
    check = request.POST.get("check", "off")
    removeNewLine = request.POST.get("removeNewLine", "off")
    extraSpaceRemove = request.POST.get("extraSpaceRemove", "off")
    upper = request.POST.get("upper", "off")

    # Remove Punctuatiaons
    if check == 'on':
        final_text = ''
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in text:
            if i not in punc:
                final_text += i

        text = final_text

    # Remove New Line
    if removeNewLine == "on":
        final_text = ""
        for char in text:
            if char != "\n" and char != '\r':
                final_text = final_text + char

        text = final_text

    # Remove Extra Space
    if extraSpaceRemove == "on":
        final_text = ''
        for index, value in enumerate(text):
            if not (text[index] == ' ' and text[index + 1] == ' '):
                final_text += value

        text = final_text

    # Convert Char to UpperCase
    if upper == "on":
        final_text = ''
        for i in text:
            final_text += i.upper()

        text = final_text

    params = {'purpose': 'Text Analayze', 'finalText': text}
    if upper == "on" or extraSpaceRemove == "on" or removeNewLine == "on" or check == 'on':
        return render(request, "analayze.html", params)
    else:
        return HttpResponse("You must click the check box on ")
