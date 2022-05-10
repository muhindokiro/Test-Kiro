from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view('GET', 'POST')
def cocktail_list(request): 

    cocktails =  Drink.objects.all()

    serializer = DrinkSerializer(cocktails, many=True)
    return JsonResponse({'cocktails': serializer.data})