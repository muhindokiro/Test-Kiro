from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer


# Create your views here.
def cocktail_list(request):

    cocktails =  Drink.objects.all()

    serializer = DrinkSerializer(cocktails, many=True)
    return JsonResponse(serializer.data, safe=False)