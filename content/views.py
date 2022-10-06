from urllib import response
from rest_framework.views import APIView, Response, status
from .models import Content
from django.forms.models import model_to_dict

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

        # print("-" * 100)
        # print(request.data)
        # print("-" * 100)

        # ipdb.set_trace()

        contenty = Content.objects.create(**request.data)
        contenty_dict = model_to_dict(contenty)

        return Response(contenty_dict, status.HTTP_201_CREATED)

# class Api_Class_View (APIView):
