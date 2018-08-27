from rest_framework import permissions

class Permission(permissions.BasePermission):

    def has_permission(self,request,view):
        pass

    def has_object_permission(self,request,view,obj):
        #this method is called only if method has_permission is passed
        pass
