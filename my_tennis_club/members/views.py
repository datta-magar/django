from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.all().get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())  

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'cars' : [
            {'name': 'BMW', 'model': 'X5', 'year': 2020},
            {'name': 'Audi', 'model': 'A6', 'year': 2019},
            {'name': 'Mercedes', 'model': 'C-Class', 'year': 2021},
            {'name': 'Toyota', 'model': 'Camry', 'year': 2022},
            {'name': 'Honda', 'model': 'Accord', 'year': 2023},
            {'name': 'Ford', 'model': 'Mustang', 'year': 2020},
            {'name': 'Chevrolet', 'model': 'Malibu', 'year': 2018},
            {'name': 'Nissan', 'model': 'Altima', 'year': 2021},
            {'name': 'Hyundai', 'model': 'Sonata', 'year': 2022},
            {'name': 'Kia', 'model': 'Optima', 'year': 2023},
            {'name': 'Volkswagen', 'model': 'Passat', 'year': 2020},
            {'name': 'Subaru', 'model': 'Legacy', 'year': 2019},
            {'name': 'Mazda', 'model': '6', 'year': 2021},
            {'name': 'Chrysler', 'model': '300', 'year': 2022},
            {'name': 'Dodge', 'model': 'Charger', 'year': 2023},
            {'name': 'Jeep', 'model': 'Cherokee', 'year': 2020},
            {'name': 'Buick', 'model': 'Regal', 'year': 2019},
            {'name': 'GMC', 'model': 'Sierra', 'year': 2021},
            {'name': 'Ram', 'model': '1500', 'year': 2022},
            {'name': 'Tesla', 'model': 'Model S', 'year': 2023},
            {'name': 'Porsche', 'model': '911', 'year': 2020},
            {'name': 'Lexus', 'model': 'ES', 'year': 2019},
            {'name': 'Acura', 'model': 'TLX', 'year': 2021},
            {'name': 'Infiniti', 'model': 'Q50', 'year': 2022},
            {'name': 'Land Rover', 'model': 'Range Rover', 'year': 2023},
            {'name': 'Jaguar', 'model': 'XF', 'year': 2020},
            {'name': 'Volvo', 'model': 'S60', 'year': 2019},
            {'name': 'Mitsubishi', 'model': 'Eclipse', 'year': 2021},
            {'name': 'Mini', 'model': 'Cooper', 'year': 2022},
            {'name': 'Fiat', 'model': '500', 'year': 2023}
        ],
        'mymembers': mymembers,
        'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'], 
    }
    return HttpResponse(template.render(context, request))
