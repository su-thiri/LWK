from django.shortcuts import render


def home(requests):
    return render(requests,'home.html')

def region(requests):
    return render(requests,'regionandstate.html')

def township(requests):
    return render(requests,'township.html')