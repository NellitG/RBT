from django.shortcuts import render
from rest_framework import generics
from .models import GalleryImage
from .serializers import GalleryImageSerializer

# Create your views here.
class GalleryImageListView(generics.ListAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer