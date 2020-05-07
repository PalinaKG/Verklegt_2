from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from templates.user.forms.user_form import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': CustomUserCreationForm()
    })

