from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for user {username}')
            return redirect('blog-home')
        else:
            messages.error(request, form.errors, extra_tags='danger')
            return render(request, 'user/register.html', {'form': form})

    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})
