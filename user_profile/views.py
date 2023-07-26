from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    return render(request, 'profile.html', {'profile': profile})

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get_or_create(user=request.user)[0]
        profile.profile_picture = request.FILES.get('profile_picture', profile.profile_picture)
        profile.user.full_name = request.POST.get('full_name', profile.user.full_name)
        profile.user.nip = request.POST.get('nip', profile.user.nip)
        profile.user.email = request.POST.get('email', profile.user.email)
        password = request.POST.get('password')
        if password:
            profile.user.set_password(password)
        profile.user.save()
        profile.save()
        return redirect('profile')
    return render(request, 'profile.html')
