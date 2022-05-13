from urllib.request import Request
from django.shortcuts import render
from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from KiroTest import serializers
import json

# def drinks():
#     url = "http://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
#     payload={}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     return response


# Create your views here.
@api_view(['GET'])
def getLocalCockTails(request):
    if request.method == 'GET':
        cocktails =  Drink.objects.all()
        serializer = DrinkSerializer(cocktails, many=True)
        # print(serializer,"TESTING THE OUTPUT FOR THE USERS!!!")
        # print(type(serializer.drink),"DATA TYPE WE GETTING!!!")
        # data = json.loads(serializer)
        # data={
        #     "name":serializer['name'],
        #     'description':serializer['description']
        # }
        return serializer
    
@api_view(['GET', 'POST'])
def cocktail_list(request): 
    
    if request.method == 'GET':
        url = "http://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        print(type(data), "HEHEHHHEHa")
 
        return Response(data)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def cocktail_detail(request, id):
   
    # try:
        # print("TESTING THE GET",id)
        # cocktail = Drink.objects.get(pk=id)
    # except Drink.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print("TESTING THE VALUES",id)
        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=0"
        payload={}
        print(url,"THE URL TO GET")
        headers = {'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text,'TESTING STATUS')
        data = json.loads(response.text)
        print(type(data),data, "HEHEHHHEHa")
        return Response(data)
        # serializer = DrinkSerializer(cocktail)
        # return Response(serializer.data)
    
    # elif request.method == 'PUT':
    #     serializer = DrinkSerializer(cocktail, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     cocktail.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        