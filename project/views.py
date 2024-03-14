from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, "index.html")
    

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('upper', 'off')
    newlineremover = request.POST.get('nliner', 'off')
    extraspaceremover = request.POST.get('espacer', 'off')
    charcount = request.POST.get('charcounter', 'off')
   

        

    if removepunc=="on":
        modified_text = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in range(len(djtext)):
            if djtext[i] not in punctuations:
                modified_text+=djtext[i]

        analyzed = modified_text
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed,}
        djtext = analyzed
    if uppercase=="on":
        stri = ""
        for i in range(len(djtext)):
            if djtext[i].islower():
                stri += djtext[i].upper()
            else:
                stri+=djtext[i]
        analyzed = stri
        params = {'purpose':'Convert to Uppercase', 'analyzed_text':analyzed,}
        djtext = analyzed
      

    if newlineremover=="on":
        stri = ""
        for i in range(len(djtext)):
            if djtext[i]!="\n" and djtext[i]!="\r":
                stri += djtext[i]
            
        analyzed = stri
        params = {'purpose':'Remove New Line', 'analyzed_text':analyzed,}
        djtext = analyzed
       
    
    if extraspaceremover=="on":
        stri = ""
        for i, char in enumerate(djtext):
            if not (djtext[i]==" " and djtext[i+1]==" "):
                stri += char
            
        analyzed = stri
        params = {'purpose':'Remove Extra Spaces', 'analyzed_text':analyzed,}
        djtext = analyzed
    
    if charcount=="on":
        count = 0
        for i in range(len(djtext)):
            if djtext[i].isalnum():
                count+=1

        analyzed = f"The Total Number of Characters is {count}."
        params = {'purpose':'Count Total Characters', 'analyzed_text':analyzed}
    
    if (removepunc!="on" and uppercase!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Error!")
        

    return render(request, 'analyze.html', params)
   


