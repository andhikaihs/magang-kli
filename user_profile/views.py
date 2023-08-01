# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from .models import Profile

# @login_required
# def profile(request):
#     profile = Profile.objects.get_or_create(user=request.user)[0]

#     if request.method == 'POST':
#         profile = Profile.objects.get_or_create(user=request.user)[0]
#         profile.profile_picture = request.FILES.get('profile_picture', profile.profile_picture)
#         profile.user.full_name = request.POST.get('full_name', profile.user.full_name)
#         profile.user.nip = request.POST.get('nip', profile.user.nip)
#         profile.user.email = request.POST.get('email', profile.user.email)
#         password = request.POST.get('password')
#         if password:
#             profile.user.set_password(password)
#         profile.user.save()
#         profile.save()

#         messages.success(request, 'Successfully applied!')

#         # # Redirect to the profile page
#         # return redirect(reverse('profile'))

#         # Redirect back to the previous URL (profile page)
#         return redirect(request.META.get('HTTP_REFERER'))
    
#     return render(request, 'profile.html', {'profile': profile})

from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Profile

def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get_or_create(user=request.user)[0]

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

            messages.success(request, 'Successfully applied!')

            # Redirect to the profile page
            return redirect(reverse('profile'))
        
        return render(request, 'profile.html', {'profile': profile})
    else:
        # If user is not authenticated, redirect to custom login with the 'next' parameter
        next_url = reverse('profile')
        return redirect(reverse('login') + f'?next={next_url}')

def similarity_checker(request):

    return render(request, 'similarity-checker.html')

def roles(request):

    return render(request, 'roles.html')

def input_as(request):

    return render(request, 'input-as.html')

def statistic(request):
    return render(request, 'statistic.html')