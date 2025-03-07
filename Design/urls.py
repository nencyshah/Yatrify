from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
     path('', views.Indexview, name='Indexview'),
     path('Scripttrans', views.Scripttrans, name="Scripttrans"),
     path('Usertrans', views.Usertrans, name="Usertrans"),
     path('Buytrans', views.Buytrans, name="Buytrans"),
     path('Selltrans', views.Selltrans, name="Selltrans"),
     path('Login', views.Login, name="Login"),
     path('AdminDashBoard', views.AdminDashBoard, name="AdminDashBoard"),
     path('UserDashBoard', views.UserDashBoard, name="UserDashBoard"),
     path('Aboutus', views.Aboutus, name="Aboutus"),
     path('Contactus', views.Contactus, name="Contactus"),
     path('Service', views.Service, name="Service"),
     path('Package', views.Package, name="Package"),
     path('PlaceTrans', views.PlaceTrans, name="PlaceTrans"),
     path('PlaceView', views.PlaceView, name="PlaceView"),
     path('PlaceViewInfo/<int:id>', views.PlaceViewInfo, name="PlaceViewInfo"),
      
     
     
]
