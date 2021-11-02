from rest_framework.permissions import BasePermission
        
class Instrutor(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
  
        return (request.user.is_staff == True and request.user.is_superuser == True)

class Facilitador_and_instrutor(BasePermission):
    def has_permission(self, request, view):


        return (request.user.is_staff == True)

class Estudante(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_staff == False and request.user.is_superuser == False)