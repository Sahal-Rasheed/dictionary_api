from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from .models import Dictionary
from .serializers import DictionarySerializer
# Create your views here.


class DictionaryView(ViewSet):
    # Method to handle POST requests
    def create(self,request,*args,**kwargs):
        serializer = DictionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    # Method to handle GET requests    
    def list(self,request,*args,**kwargs):
        query = request.query_params.get("search","")
        if not query:
            words = Dictionary.objects.all()
        else:
            words = Dictionary.objects.filter(label__icontains=query)
            for word in words:
                word.increment_search_count()

        serializer = DictionarySerializer(words,many=True) 
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle PUT requests
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        word = Dictionary.objects.get(id=id)
        serializer = DictionarySerializer(data=request.data, instance=word)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)  
        
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)              

    # Method to handle DELETE requests
    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        word = Dictionary.objects.get(id=id)
        word.delete()
        return Response({"Message":"Word Deleted"}, status=status.HTTP_200_OK)