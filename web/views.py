from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "web/home.html", {})

def contact(request):
    return render(request, "web/contact.html", {})

def about(request):
    return render(request, "web/about.html", {})