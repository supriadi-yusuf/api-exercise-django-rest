from django.shortcuts import render

# spd : import moduls, class that we need
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
