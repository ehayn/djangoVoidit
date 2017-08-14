from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['confirmPassword']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error': 'Username is already taken'})
			except User.DoesNotExist:			
				user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
				login(request, user)
				return render(request, 'accounts/signup.html')
		else:
			return render(request, 'accounts/signup.html', {'error': 'Passwords don\'t match'})
	
	else:
		return render(request, 'accounts/signup.html')

def loginView(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST['next'])
			else:
				return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error': 'Invalid Username and/or Password'})
	
	else:
		return render(request, 'accounts/login.html')
		
def logoutView(request):
	if request.method == 'POST':
		logout(request)
	return redirect('home')