from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_from = forms.AuthorForm(request.POST)
        if author_from.is_valid():
            author_from.save()
            print(author_from.cleaned_data)
            return redirect('add_author') 
    else:
        author_from = forms.AuthorForm()

    return render(request, './authors/add_author.html', {'form':author_from})
