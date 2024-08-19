from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age': 20, 'list': ['Python', 'is', 'fun'], 'courses': [
        {
            'name': 'Python',
            'id': 1,
            'fee' : 5000
        },
        {
            'name': 'Django',
            'id': 2,
            'fee' : 6500
        },
        {
            'name': 'Data Science',
            'id': 3,
            'fee' :10000
        },
    ], 'date': datetime.now(), 'empty_string:': '', 'name':'nibir ekramul', 'name_char':['n', 'i', 'b', 'i', 'r', ' ', 'e', 'k', 'r', 'a', 'm', 'u', 'l'], 'animals':['cat', 'dog', 'horse']
    }
    return render(request, 'home.html', context = d)
