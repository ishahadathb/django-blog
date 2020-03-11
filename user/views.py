from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UpdateProfileForm, UpdateProfilePic
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request):

    if request.method == "POST":
        up_form = UpdateProfileForm(request.POST, instance=request.user)
        propic_form = UpdateProfilePic(
            request.POST, request.FILES, instance=request.user.profile)

        if up_form.is_valid():
            up_form.save()
            propic_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')

        else:
            messages.error(request, up_form.errors, extra_tags='danger')
            return redirect('profile')

    else:
        up_form = UpdateProfileForm(instance=request.user)
        propic_form = UpdateProfilePic(instance=request.user.profile)

    context = {
        'up_form': up_form,
        'propic_form': propic_form
    }

    return render(request, 'user/profile.html', context=context)
