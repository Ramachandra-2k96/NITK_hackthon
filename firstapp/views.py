from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages


from firstapp.forms import LoginForm, SignUpForm

def custom_login(request):
    login_form = LoginForm()
    signup_form = SignUpForm()

    if request.method == 'POST':
        if 'login-submit' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('event_list')  
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Login form is not valid')
                print(form.errors)
        elif 'signup-submit' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                auth_login(request, user)
                messages.success(request, 'Signup successful!')
                return redirect('event_list')
            else:
                messages.error(request, 'Signup form is not valid')
                print(form.errors)

    return render(request, 'login.html', {'login_form': login_form, 'signup_form': signup_form})
