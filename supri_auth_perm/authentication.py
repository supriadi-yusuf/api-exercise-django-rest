from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class SupriAuthentication(authentication.BaseAuthentication):

    def authenticate(self,request):
        print(request.method)
        print(dir(request.POST))
        print(type(request.POST))
        print(request.POST.keys())
        print("welcome to authentication")
        print(dir(request.META))
        print(type(request.META))
        print(request.META.keys())
        print(type(request.META['USER']))

        username = request.META.get('USERNAME')
        print("user name is {}".format(username))
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")

        return (user, None) # return (user,auth) # auth is additional info ex. tokens
