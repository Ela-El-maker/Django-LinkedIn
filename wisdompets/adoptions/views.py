from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Pet

# Home view to list all pets
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,
    })

# Detail view to show a specific pet by ID
def pet_detail(request, pet_id):
    # Using get_object_or_404 for a cleaner way to handle non-existent pets
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
