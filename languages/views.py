from django.shortcuts import render
import supri_auth_perm.permission
import supri_auth_perm.filter

# spd : import moduls, class that we need
from rest_framework import viewsets
from .models import Language, Paradigm, Programmer
from .serializers import LanguageListSerializer, LanguageDetailSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework.response import Response
#from rest_framework.decorators import action
from rest_framework import permissions #spd: need this modul for permissions
from rest_framework import status
from django.contrib.auth import logout

from django.utils.six import text_type
from rest_framework import HTTP_HEADER_ENCODING
import base64

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
import django_filters
from rest_framework.decorators import action

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    CursorPagination
)

# Create your views here.
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageDetailSerializer

    #authentication_classes = (BasicAuthentication, SessionAuthentication,)

    #permission_classes = (permissions.AllowAny,) #spd : set permission here
    #permission_classes = (permissions.IsAuthenticated,) #spd : set permission here
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #spd : set permission here
    #permission_classes = (supri_auth_perm.permission.SupriPermission,)
    #permission_classes = (permissions.IsAdminUser,) #spd : set permission here

    #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_backends = (supri_auth_perm.filter.SupriFilter,)
    #filter_class = supri_auth_perm.filter.SupriFilter

    pagination_class = CursorPagination
    pagination_class.ordering = '-name' #spd: field ordering is mandatory for CursorPagination

    @action(detail=False)
    #@action(detail=False, url_name='lihat-user-akhir')
    def recent_users(self, request):
        return Response({'hasil': 'mantap'})

    #def get_queryset(self): #suppose we do not want to use queryset variable
    #    return Language.objects.all()

    #def get_permissions(self): #suppose we do not want to variable permission_classes above
    #    return [ijin() for ijin in(permissions.IsAuthenticated, permissions.IsAdminUser)]

    #def get_serializer_class(self):
    #    return LanguageDetailSerializer

    #def list(self, request):
    #    #languages = Language.objects.all()
    #    #languages = Language.objects.filter()
    #
    #    # spd : if the serializer does not contain serializers.HyperlinkedIdentityField
    #    # we do not need serializer context to instantiate the serializer
    #    #serializer = LanguageListSerializer( languages, many=True)
    #
    #    # spd : but if the serializer contains serializers.HyperlinkedIdentityField
    #    # we need serializer context to instantiate the serializer
    #    #serializer = LanguageListSerializer( self.queryset, many=True, context = { 'request' : request})
    #    #serializer = LanguageListSerializer( languages, many=True, context = { 'request' : request})
    #    queryset = self.queryset
    #    for backend in self.filter_backends:
    #        queryset = backend().filter_queryset(self.request, queryset, view=self)
    #
    #    serializer = LanguageListSerializer( queryset, many=True, context = { 'request' : request})
    #
    #    return Response( serializer.data)
    ordering = 'name'

    def list(self, request):
        self.serializer_class = LanguageListSerializer
        #self.ordering = 'name'
        return super().list(request)

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

class ParadigmViewSet(viewsets.ModelViewSet):

    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

    #def list(self, request):
    #    print('over write')
    #    return super().list(request)

class ProgrammerViewSet(viewsets.ModelViewSet):

    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class LogoutView(viewsets.ModelViewSet):
    def list(self, request):
        #auth = request.META.get('HTTP_AUTHORIZATION', b'')
        #print(auth)
        #if isinstance(auth, text_type):
        #    # Work around django test client oddness
        #    auth = auth.encode(HTTP_HEADER_ENCODING)
        #print(auth)
        #print(auth.split())
        #print(auth.split()[1])
        ##base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')
        #print(base64.b64decode(auth.split()[1]))

        #print(dir(request))
        #print(dir(request.user))
        #print(request.auth)
        #print(request.user)
        request.META['HTTP_AUTHORIZATION']='test'
        logout(request)
        #print(dir(request))
        #print(request.user)
        response=Response( status=status.HTTP_200_OK)
        #response['WWW-Authenticate']='over'
        print(request.META.items())
        print(dir(request.META))
        return response #Response( status=status.HTTP_200_OK)
