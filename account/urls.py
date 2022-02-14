from django.urls import path
from .views import ShowProfile, LoginUser,registerUser, LogoutUser


urlpatterns = [
   path('loginUser/', LoginUser, name = 'login'),
   path('logoutUser/', LogoutUser, name = 'logout'),
   path('registerUser/', registerUser, name = 'register'),
   path('profile/<str:slug>', ShowProfile, name = 'profile'),


   

]