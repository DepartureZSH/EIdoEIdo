# urls.py in app
from django.urls import path
from . import views

urlpatterns = [
    path(r'1/create/', views.IELTS1CreateAPI.as_view(), name='IELTS1_create_api'),
    path(r'2&3/create/', views.IELTS2_3CreateAPI.as_view(), name='IELTS2_create_api'),
    path(r'3/create/', views.IELTS3CreateAPI.as_view(), name='IELTS3_create_api'),
    # # 将 {your web prefix}/api/Speaking/{int num}/ 的所有请求打给views.IntAPI
    # # 并附上参数 int pk = num
    path(r'1/<int:pk>/', views.IELTS1TopicsAPI.as_view(), name='IELTS1_Topic_get_api'),
    path(r'detail/1/<int:pk>/', views.IELTS1API.as_view(), name='IELTS1_get_api'),
    # # 将 {your web prefix}/api/Speaking/{int num}/ 的所有请求打给views.IntAPI
    path(r'23/<int:pk>/', views.IELTS23API.as_view(), name='IELTS23_get_api'),
    # # 并附上参数 int pk = num
    # path(r'2/<int:pk>/', views.IELTS2API.as_view(), name='IELTS2_get_api'),
    path(r'detail/2/<int:pk>/', views.IELTS2API.as_view(), name='IELTS2_get_api'),
    # # 将 {your web prefix}/api/Speaking/{int num}/ 的所有请求打给views.IntAPI
    # # 并附上参数 int pk = num
    path(r'detail/3/<int:pk>/', views.IELTS3API.as_view(), name='IELTS3_get_api'),
]