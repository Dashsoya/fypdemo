"""
URL configuration for fypdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_view'),
    path('login/', views.loginauth, name='login'),
    path('patienthome/', views.patienthome_view, name='patienthome'),
    path('doctorhome/', views.doctorhome_view, name='doctorhome'),
    path('adminhome/', views.adminhome_view, name='adminhome'),
    path('logout/', views.logoutbye, name='logout'),
    path('accdetails/', views.accdetails, name='accdetails'),
    path('updatedetails/', views.updatedetails, name='updatedetails'),
    path('list_users/', views.list_users, name='list_users'),
    path('delete_user/<int:account_id>/', views.delete_user, name='delete_user'),
]
