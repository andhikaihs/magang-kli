from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        print("profile exists")
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
        print("Profile not found, so it'll create user's profile: ", profile)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)  # Ganti instance=request.user dengan instance=profile
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile has been updated!'))
            print("berhasil disave!!")
            return redirect('profile')
        else:
            print("gagal disave")
            messages.error(request, ('Unable to update your profile'))
    else:
        profile_form = ProfileForm(instance=profile)  # Ganti instance=request.user dengan instance=profile

    context = {
        'profile_form': profile_form,
    }

#     return render(request, 'profile.html', context)


    #     print("harusnya dipost")
    #     full_name = request.POST['full_name']
    #     nip = request.POST['nip']
    #     password = request.POST['password']

    #     # Update datas
    #     profile.full_name = full_name
    #     profile.nip = nip
    #     profile.password = password
    #     profile.save()

    #     return redirect('profile')
    # else:
    #     print("ga dipost")
    #     print("methodnya ", request.method)
    # return render(request, 'profile.html', {'profile': profile})
