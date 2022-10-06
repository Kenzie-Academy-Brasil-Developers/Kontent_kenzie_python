from pickle import TRUE
from turtle import title
from urllib import response
from rest_framework.views import APIView, Response, status
from .models import Content
from django.forms.models import model_to_dict
from .content_serializer import Content_serializer

import ipdb

class Api_Class_View (APIView):
    def get(self, request):
        conts = Content.objects.all()
        contList = []

        for i in conts:
            cont_disc = model_to_dict(i)
            contList.append(cont_disc)

        return Response(contList)



    def post(self, request):

        data_validade = Content_serializer(**request.data)

        
        if data_validade.is_valid():
            
            contenty = Content.objects.create(**request.data)
            contenty_dict = model_to_dict(contenty)
            return Response(contenty_dict, status.HTTP_201_CREATED)

        else:
            return Response(data_validade.errors,status.HTTP_400_BAD_REQUEST)




        # contador2 = 0

        # obj2 = {}

        # if(request.data["title"]):
        #     print(type(request.data["title"]))
        #     return Response(obj2)


        # contador = 0

        # obj = {}
        

        # if(type(request.data["title"]) != str):
        #     contador = contador + 1
        #     obj["title"] = "must be a str"
            
        # if(type(request.data["module"]) != str):
        #     contador = contador + 1
        #     obj["module"] = "must be a str"

        # if(type(request.data["description"]) != str):
        #     contador = contador + 1
        #     obj["description"] = "must be a str"

        # if(type(request.data["students"]) != int):
        #     contador = contador + 1
        #     obj["students"] = "must be a int"

        # if(type(request.data["is_active"]) != bool):
        #     contador = contador + 1
        #     obj["titis_activele"] = "must be a bool"


        # if(contador > 0):
        #     return Response(obj)
            

        # ipdb.set_trace()
    
        # print("-" * 100)
        # print(request.data["title"])
        # print("-" * 100)



