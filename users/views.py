from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout

# View for sign up
def sign_up(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:    
        form = signUpForm()
    
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)
    
# View for profile
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

# View for logout
def logout_view(request):
    logout(request)  # This will log the user out
    return render(request, 'users/logout.html')
