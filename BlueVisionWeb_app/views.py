from django.shortcuts import render, redirect
from .models import SendMessage
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserCreationForm

#registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('BlueVisionWeb_app:contact')  # Redirect to a desired page after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register/register.html', {'form': form})


#login
def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('BlueVisionWeb_app:show_data')  # Redirect after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    return render(request, 'login/login.html', {'form': form})

#logout
def custom_logout(request):
    logout(request)
    return redirect('BlueVisionWeb_app:contact')  # Redirect after logout


# Create your views here.
def index(request):
    context = {
        'name': 'BlueVisionWeb'
    }
    return render(request, 'index.html', context)


#form submission 
def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BlueVisionWeb_app:contact')  # Redirect to prevent form resubmission
    else:
        form = ContactForm()
    
    context = {}
    return render(request, 'contact/contact.html', context)

#show data
def show_data(request):
    messages = SendMessage.objects.all()  # Fetch messages for display
    context = {
        'messages': messages,
    }
    return render(request, 'show/show.html', context)

#contact page
def contact(request):
    context = {}
    return render(request, 'contact/contact.html', context)

#service page
def service(request):
    context = {}
    return render(request, 'service/service.html', context)

#about page
def about(request):
    context = {}
    return render(request, 'about/about.html', context)

# license page
def license(request):
    context = {}
    return render(request, 'license/license.html', context)

#career page
def career(request):
    context = {}
    return render(request, 'career/career.html', context)