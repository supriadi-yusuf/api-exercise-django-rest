from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate

class SupriAuthentication(authentication.BaseAuthentication):

    def authenticate(self,request):
        #print(self.www_authenticate_realm)
        #print('authenticate')
        #return super( self.__class__, self).authenticate(request)
        #return super( SupriAuthentication, self).authenticate(request)
        #print(request.META['username'])#error
        #print(dir(request.META.values()))
        #print(request.META.keys())
        #for key,value in request.META.items(): # request.META is dictionary
        #    print("{0} => {1}".format(key,value))
        #d={'test':'1', 'a': '2'}
        #for (key,value) in d.items():
        #    print('{0} => {1}'.format(key,value))#pass

        try:
            username=request.META['HTTP_USERNAME'] #from http header
            password=request.META['HTTP_PASSWORD'] #from http header
            user = authenticate(username=username, password=password)
        except:
            user = None

        #if user is not None:
        #    print(user.is_authenticated())

        return user, None

    def authenticate_header(self, request):
        #print('authenticate_header')
        #print(self.www_authenticate_realm)
        #return super( SupriAuthentication, self).authenticate_header(request)
        pass
