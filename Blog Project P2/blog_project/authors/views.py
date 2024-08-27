from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_from = forms.AuthorForm(request.POST)
#         if author_from.is_valid():
#             author_from.save()
#             print(author_from.cleaned_data)
#             return redirect('add_author') 
#     else:
#         author_from = forms.AuthorForm()

#     return render(request, './authors/add_author.html', {'form':author_from})


def registration(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('registration')
    else:
        registration_form = forms.RegistrationForm()
    
    return render(request, './authors/form.html', {'form': registration_form, 'type':'Registration'})

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']

            user = authenticate(username = user_name, password = user_pass)

            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            
            messages.warning(request, 'No user Found')
            return redirect('registration')
            
    else:
        login_form = AuthenticationForm()
        return render(request, './authors/form.html', {'form': login_form, 'type':'Login'})
    
@login_required
def profile(request):
    # data = Post.objects.all()
    data = Post.objects.filter(author = request.user)
    return render(request, './authors/profile.html',{'data':data})

@login_required
def change_pass(request):
    if request.method == 'POST':
        change_pass_form = PasswordChangeForm(request.user, data = request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, change_pass_form.user)
            return redirect('profile')
    else:
        change_pass_form = PasswordChangeForm(user=request.user)
    
    return render(request, './authors/change_pass.html', {'form': change_pass_form, 'type':'Change Password'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserDataForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserDataForm(instance = request.user)
    
    return render(request, './authors/edit_profile.html', {'form': profile_form, 'type':'Profile'})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')