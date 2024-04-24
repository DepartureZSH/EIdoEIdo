# urls.py in app
from django.urls import path
from . import views

urlpatterns = [
    path(r'dictation/<int:pk>/', views.IELTSWangAPI.as_view(), name='IELTS_Wang_api'),
    path(r'dictation_corpus/<int:pk>/', views.IELTSMyCorpusAPI.as_view(), name='IELTS_Wang_Corpus_api'),
]