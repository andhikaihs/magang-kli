from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password


def register(request):
    role_choices = CustomUser.ROLE_CHOICES 
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        nip = request.POST.get('nip')
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user already exists
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'User with this email already exists.'})

        # Create a new user
        user = CustomUser(full_name=full_name, nip=nip, role=role, email=email, password=make_password(password))
        user.save()

        return redirect('/login')

    return render(request, 'register.html', {'role_choices': role_choices})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if user exists
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

        # Check user password
        if not check_password(password, user.password):
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

        # Store user information in session
        request.session['user_id'] = str(user.id)  # Convert UUID to string
        request.session['full_name'] = user.full_name
        request.session['nip'] = user.nip
        request.session['role'] = user.role
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
    
def logout(request):
    # Clear the session data
    request.session.clear()
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def profile(request):
    full_name = request.session.get('full_name')
    nip = request.session.get('nip')
    role = request.session.get('role')
    email = request.session.get('email')
    password = request.session.get('password')

    return render(request, 'profile.html', {'full_name': full_name, 'nip': nip, 'role': role, 'email': email, 'password': password})