from rest_framework.permissions import BasePermission
        
class Instrutor(BasePermission):
    def has_permission(self, request, view):

     

        return (request.user.is_staff == True and request.user.is_superuser == True)

class Facilitador(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_staff == True and request.user.is_superuser == False)

class Estudante(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_staff == False and request.user.is_superuser == False)