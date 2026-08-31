from .views import *
from django.urls import path

urlpatterns = [
    path('Register', PostManApi),
    path('Login-MasterApi', LoginApi),
    path('Users', GetApi),
    path('Delete-Data/<int:x_id>', DeleteApi),
    path('UsersGet/<int:z_id>', GetUsersApi),
    path('Update-Users-Api/<int:user_id>', UpdateApi)
]