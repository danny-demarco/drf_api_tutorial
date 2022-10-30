from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from snippets_app.models import Snippet
from snippets_app.serializers import SnippetSerializer



# Create your views here.

"""
    The root of our API is going to be a view that supports listing all the existing snippets, or creating a new snippet.
    csrf_exempt views are not recommended and are provided to give an understanding of how things are working together
"""

# Function based view
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class based view
# class SnippetListView(APIView):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# The CRUD operations we complete in classed based views are going to be very similar for all model backed views.
# To keep things DRY and Django has Mixin classes that implement these common pieces of code. 

# Mixin classes
# The mixins provide the .list() and .create() methods
# class SnippetListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get_queryset(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# Generic class based views take steps even further to reduce code. REST framework provides generic views that already incorporate
# mixins. The following example does everything the above methods do.

# Generic class based view.
class SnippetListView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



# Function based view
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Class based view
# class SnippetDetailView(APIView):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)



# Mixin class based views provice the .retrieve() method, .update() method, and .destroy() method.
# class SnippetDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get_object(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Generic class based view
class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    
