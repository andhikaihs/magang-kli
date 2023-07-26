from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import User

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        nip = request.POST['nip']
        roles = request.POST['roles']
        email = request.POST['email']
        password = request.POST['password']

        if get_user_model().objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'User with this email already exists.'})
          
        user = get_user_model().objects.create_user(username=email, full_name=full_name, nip=nip, roles=roles, email=email, password=password)
        print("username: ", email)
        print("email: ", email)
        print("New User:", user)
        user.save()

        return redirect('/login')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        print("email: ", email)
        password = request.POST['password']

        # Check if user exists
        try:
            user = User.objects.get(email=email)
            print("user is already exists: ", user)
        except get_user_model().objects.DoesNotExist:
            return render(request, 'login.html', {'error': 'You are not registered yet.'})
        
        
        # Check user password
        if not check_password(password, user.password):
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
        
        auth_login(request, user)
        request.session['user_id'] = str(user.id)
        request.session['full_name'] = user.full_name
        request.session['nip'] = user.nip
        request.session['roles'] = user.roles
        request.session['email'] = user.email
        request.session['password'] = user.password
        return redirect('dashboard')

    return render(request, 'login.html')

def dashboard(request):
    user_id = request.session.get('user_id')
    full_name = request.session.get('full_name')
    role = request.session.get('role')

    if user_id and full_name:
        # if user is logged in
        return render(request, 'dashboard.html', {'full_name': full_name, 'role': role})
    else:
        # if user is not logged in, redirect to the login page
        return redirect('login')
    
@login_required
def logout(request):
    # Clear the session data
    request.session.clear()
    return redirect('login')

def home(request):
    return render(request, 'home.html')