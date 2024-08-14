from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age': 20, 'list': ['Python', 'is', 'fun'], 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee' : 5000
        },
        {
            'id': 2,
            'name': 'Django',
            'fee' : 6500
        },
        {
            'id': 3,
            'name': 'Data Science',
            'fee' :10000
        },
    ], 'date': datetime.now(), 'empty_string:': ''}
    return render(request, 'home.html', context = d)
