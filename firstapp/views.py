from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from firstapp.forms import LoginForm, SignUpForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        redirect_url = '/custom_login'
        return redirect(redirect_url)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


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
                    messages.add_message(request, messages.SUCCESS, 'Login successful!')
                    return redirect('home', permanent=True)  # 'permanent=True' will cause a 301 redirect  
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
                return redirect('home')
            else:
                messages.error(request, 'Signup form is not valid')
                print(form.errors)

    return render(request, 'login.html', {'login_form': login_form, 'signup_form': signup_form})

@login_required
def home(request):
    return render(request,'home.html')
@login_required
def meet(request):
    user =request.user
    return render(request,'WEB_UIKITS.html',{'username':user.first_name})

@login_required
def Custom_logout(request):
    logout(request)
    return redirect('custom_login')