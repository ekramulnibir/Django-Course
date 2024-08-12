from django.http import HttpResponse

def home(request):
    return HttpResponse('This is Project/home page')

def contacts(request):
    return HttpResponse('This is project/contacts page')
