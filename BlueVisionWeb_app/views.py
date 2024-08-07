from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'BlueVisionWeb'
    }
    return render(request, 'index.html', context)

#contact page
def contact(request):
    context = {}
    return render(request, 'contact/contact-1.html', context)

#service page
def service(request):
    context = {}
    return render(request, 'service/service-v2.html', context)

#about page
def about(request):
    context = {}
    return render(request, 'about/about-v2.html', context)

# license page
def license(request):
    context = {}
    return render(request, 'license/license.html', context)

#career page
def career(request):
    context = {}
    return render(request, 'career/career.html', context)