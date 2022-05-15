from django.shortcuts import render

def media(request):
    return render(request, 'media.html')

def card(request):
    return render(request, 'mediacard.html')
