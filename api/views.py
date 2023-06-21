from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from .models import Dictionary
from .serializers import DictionarySerializer
# Create your views here.


class DictionaryView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer = DictionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    def list(self,request,*args,**kwargs):
        query = request.query_params.get("search")
        if query == "" or query == None:
            words = Dictionary.objects.all()
        else:
            words = Dictionary.objects.filter(label__icontains=query)
            for word in words:
                word.increment_search_count()

        serializer = DictionarySerializer(words,many=True) 
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        word = Dictionary.objects.get(id=id)
        serializer = DictionarySerializer(data=request.data, instance=word)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)              

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        word = Dictionary.objects.get(id=id)
        word.delete()
        return Response({"Message":"Word Deleted"}, status=status.HTTP_200_OK)