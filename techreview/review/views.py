from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'review/index.html')#tells it to render a webpage

