# urls.py in app
from django.urls import path
from . import views

urlpatterns = [
    # 将 {your web prefix}/api/User/ 的所有请求打给views.NoneAPI
    path('', views.NoneAPI.as_view(), name='user_center_none_api'),
    # # 将 {your web prefix}/api/User/{int num}/ 的所有请求打给views.IntAPI
    # # 并附上参数 int pk = num
    # path(r'<int:id>/', views.API.as_view(), name='neckname2'),
]