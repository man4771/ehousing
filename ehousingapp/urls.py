from django.urls import path
from .views import *

urlpatterns = [
    path('index_page/',index_page,name='index_page'),
    path('', index, name=''),
    path('login_page/', login_page, name='login_page'),
    path('register_page/', register_page, name='register_page'),
    path('profile_page/', profile_page, name='profile_page'),
    path('login/', login, name='login'),
    path('otp_page/', otp_page, name="otp_page"),
    path('verify_otp/<str:verify_for>/', verify_otp, name="verify_otp"),
    path('register/', register, name='register'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change_password/', change_password, name='change_password'),
    path('upload_image/', upload_image, name='upload_image'),
    path('remove_profile_image/', remove_profile_image, name="remove_profile_image"),
    
    


    path('logout/', logout, name='logout'),
]
