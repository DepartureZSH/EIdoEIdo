from django.db import models
from datetime import datetime
from django.utils import timezone

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    # 听力语料
    MyDictation = models.ForeignKey("User.Listening", on_delete=models.SET_NULL, null=True)
    # 口语语料
    MyIELTS1 = models.ForeignKey("User.SpeakingIELTS1Topics", on_delete=models.SET_NULL, null=True)
    MyIELTS123 = models.ForeignKey("User.SpeakingIELTS23Topics", on_delete=models.SET_NULL, null=True)
    MyTopics = models.ForeignKey("User.SpeakingTopics", on_delete=models.SET_NULL, null=True)

class Listening(models.Model):
    id = models.AutoField(primary_key=True)
    # 听力语料列表
    Listening_Corpus_list = models.CharField(max_length=1000)
    # 听写本、当前语料、播放断点
    Listening_Last_MyDictation = models.CharField(max_length=1000)
    Listening_Last_MyCorpusID = models.ForeignKey("Listening.Corpus", on_delete=models.SET_NULL, null=True)
    Listening_Last_MyCorpusBreak = models.IntegerField(default=0)
    Create_time = models.DateTimeField(auto_now_add=True)
    Update_time = models.DateTimeField(auto_now=True)

class SpeakingIELTS1Topics(models.Model):
    id = models.AutoField(primary_key=True)
    # 口语语料列表
    IELTS1Topics_list = models.CharField(max_length=10000)

class SpeakingIELTS23Topics(models.Model):
    id = models.AutoField(primary_key=True)
    # 口语语料列表
    IELTS1Topics_list = models.CharField(max_length=10000)

class SpeakingTopics(models.Model):
    id = models.AutoField(primary_key=True)
    # 口语语料列表
    IELTS1Topics_list = models.CharField(max_length=10000)

# Create your models here.
