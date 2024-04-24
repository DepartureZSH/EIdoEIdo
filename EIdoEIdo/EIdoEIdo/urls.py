"""EIdoEIdo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

urlpatterns = [
    ###################################################################################
    # User api
    # 将 {your web prefix}/api/User/ 的所有请求打给UserCenter.urls
    path('api/User/', include('User.urls')),
    # Speaking api
    # 将 {your web prefix}/api/Speaking/ 的所有请求打给UserCenter.urls
    path('api/Speaking/', include('Speaking.urls')),

    path('api/Listening/', include('Listening.urls')),
    ###################################################################################
    path('admin/', admin.site.urls),
]
