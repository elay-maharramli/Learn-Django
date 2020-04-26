from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            category = form.cleaned_data['category']
            about = form.cleaned_data['about']

            print(name, age, category, about)

    form = ContactForm()
    return render(request, 'form.html', {'form': form})
