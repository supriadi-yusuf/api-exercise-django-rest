from django.shortcuts import render

# spd : import moduls, class that we need
from rest_framework import viewsets
from .models import Language, Paradigm, Programmer
from .serializers import LanguageListSerializer, LanguageDetailSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework.response import Response
#from rest_framework.decorators import action
from rest_framework import permissions #spd: need this modul for permissions

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageDetailSerializer
    #permission_classes = (permissions.AllowAny,) #spd : set permission here
    #permission_classes = (permissions.IsAuthenticated,) #spd : set permission here
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #spd : set permission here
    permission_classes = (permissions.IsAdminUser,) #spd : set permission here

    def list(self, request):
        languages = Language.objects.all()
    #
    #    # spd : if the serializer does not contain serializers.HyperlinkedIdentityField
    #    # we do not need serializer context to instantiate the serializer
    #    #serializer = LanguageListSerializer( languages, many=True)
    #
    #    # spd : but if the serializer contains serializers.HyperlinkedIdentityField
    #    # we need serializer context to instantiate the serializer
    #    #serializer = LanguageListSerializer( self.queryset, many=True, context = { 'request' : request})
        serializer = LanguageListSerializer( languages, many=True, context = { 'request' : request})
    #
        return Response( serializer.data)

    #def create(self, request):
    #    pass

    #def retrieve(self, request, pk=None):
    #    self.queryset = Language.objects.all()
    #    self.serializer_class = LanguageSerializer
    #    return Response({'status':'oke bro'})

    #def update(self, request, pk=None):
    #    pass

    #def partial_update(self, request, pk=None):
    #    pass

    #def destroy(self, request, pk=None):
    #    pass

class ParadigmView(viewsets.ModelViewSet):

    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):

    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
