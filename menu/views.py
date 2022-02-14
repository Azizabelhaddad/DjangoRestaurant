from django.http import HttpResponse
from django.shortcuts import redirect, render
from menu.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from menu.models import Pizza

# Create your views here.

def index(request):
    return render(request, 'pizza/index.html')

def about(request):
    return render(request, 'pizza/about.html')

def contact(request):
    return render(request, 'pizza/contact.html')

def blog(request):
    return render(request, 'pizza/blog.html')


def menu(request):
    allpizza = Pizza.objects.filter(state=1, type=6)
    slicepizza = Pizza.objects.filter(state=1, type=5)
    rollpizza = Pizza.objects.filter(state=1, type=2)
    boxpizza = Pizza.objects.filter(state=1, type=3)
    return render(request, 'pizza/menu.html', {'allpizza': allpizza, 'slicepizza':slicepizza , 'rollpizza':rollpizza })

def pizzas(request):
    pizzas = Pizza.objects.filter(state=1, type=6)

    return render(request, 'pizza/pizzas.html', {'pizzas': pizzas})

def addPizza(request, id):
    lapizza = Pizza.objects.get(pk=id)
    return render(request, 'pizza/index.html', {'lapizza': lapizza})

def contact(request):
    if request.method == 'GET' :
        form =ContactForm
    elif  request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            try:
                send_mail(name,comment, email, ['aziza.belhaddad@gmail.com'])
            except BadHeaderError:
        
                return HttpResponse(BadHeaderError)
        return redirect('menu')

    return render(request, 'pizza/contact.html', {'form': form})

def successContact(request):
    return HttpResponse('Success! Thank you for your message.')