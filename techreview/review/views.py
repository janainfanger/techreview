from django.shortcuts import render
from.models import ProductType

# Create your views here.
def index(request):
    return render(request, 'review/index.html')#tells it to render a webpage

def techtypes (request):
    type_list=ProductType.objects.all()
    return render(request, 'review/types.html', {'type list': type_list})
