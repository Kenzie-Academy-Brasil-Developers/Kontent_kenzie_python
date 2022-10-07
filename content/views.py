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
            
            contenty = Content.objects.create(**data_validade.data)
            contenty_dict = model_to_dict(contenty)
            return Response(contenty_dict, status.HTTP_201_CREATED)

        else:
            return Response(data_validade.errors,status.HTTP_400_BAD_REQUEST)

class Api_Class_View_by_id (APIView):

    def get(self, request,content_id):
        try:
            contenty = Content.objects.get(id=content_id)
            contenty_dict = model_to_dict(contenty)
            return Response(contenty_dict)
        except Content.DoesNotExist: 
            return Response({"message": "Content not found."}, status.HTTP_404_NOT_FOUND)


    def patch(self, request,content_id):
        try:
            contenty = Content.objects.get(id=content_id)
        except Content.DoesNotExist: 
            return Response({"message": "Content not found."}, status.HTTP_404_NOT_FOUND)


        for key, value in request.data.items():
            # ipdb.set_trace()
            setattr(contenty, key, value)

        contenty.save()
        person_dict = model_to_dict(contenty)

        return Response(person_dict)

    def delete(self, request,content_id):
        try:
            person = Content.objects.get(id=content_id)
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Content.DoesNotExist:
            return Response({"message": "Content not found."}, status.HTTP_404_NOT_FOUND)

class Api_Class_View_by_title (APIView):
    
 def get(self, request):
      title = request.query_params.get('title', None)

      content = Content.objects.filter(title__iexact=title)

      content_dict = [model_to_dict(account) for account in content]

      return Response(content_dict)
