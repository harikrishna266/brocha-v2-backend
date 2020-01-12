from django.shortcuts import render
from fbx.models import Fbx
from .serializers import FbxSerializer
from rest_framework import generics, filters

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.
class listFbx(generics.ListCreateAPIView):
  serializer_class = FbxSerializer
  def get_queryset(self):
    return Fbx.objects.all()





# Imaginary function to handle an uploadee

