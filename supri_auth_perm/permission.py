from rest_framework import permissions

class SupriPermission(permissions.BasePermission):

    #message = "ga boleh cuy ..."
    #message = 'Adding customers not allowed.'

    def has_permission(self,request,view): #it is always executed. it is executed first
        #print( str(self.__class__) + "has_permission")
        #print(request.method)
        #print(permissions.SAFE_METHODS)
        #print(request.META['REMOTE_ADDR'])
        #print(type(request.META['REMOTE_ADDR']))
        #print(dir(request.META.values()))
        #print('permisionnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
        return True

    def has_object_permission(self,request,view,obj): # it is only executed for object-details
        #this method is called only if method has_permission is passed
        print( str(self.__class__) + " has_object_permission")
        #return obj.owner == request.user
        return True
