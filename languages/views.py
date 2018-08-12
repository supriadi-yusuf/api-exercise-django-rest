from django.shortcuts import render

# spd : import moduls, class that we need
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageListSerializer, LanguageDetailSerializer
from rest_framework.response import Response
#from rest_framework.decorators import action

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageDetailSerializer

    def list(self, request):
        #languages = Language.objects.all()

        # spd : if the serializer does not contain serializers.HyperlinkedIdentityField
        # we do not need serializer context to instantiate the serializer
        #serializer = LanguageListSerializer( languages, many=True)

        # spd : but if the serializer contains serializers.HyperlinkedIdentityField
        # we need serializer context to instantiate the serializer
        serializer = LanguageListSerializer( self.queryset, many=True, context = { 'request' : request})

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
