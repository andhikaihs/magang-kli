from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    role_choices = User.ROLE_CHOICES 
    
    if request.method == 'POST':
        full_name = request.POST['full_name']
        nip = request.POST['nip']
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'User with this email already exists.'})

        # Create a new user
        user = User(full_name=full_name, nip=nip, role=role, email=email, password=make_password(password))
        user.save()

        return redirect('/login')

    return render(request, 'register.html', {'role_choices': role_choices})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

        # Check user password
        if not check_password(password, user.password):
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

        # Store user information in session
        request.session['user_id'] = user.id
        request.session['user_full_name'] = user.full_name
        return redirect('dashboard')

    return render(request, 'login.html')

def dashboard(request):
    user_id = request.session.get('user_id')
    user_full_name = request.session.get('user_full_name')

    if user_id and user_full_name:
        # if user is logged in
        return render(request, 'dashboard.html', {'user_full_name': user_full_name})
    else:
        # if user is not logged in, redirect to the login page
        return redirect('login')
    
def logout(request):
    # Clear the session data
    request.session.clear()
    return redirect('login')
