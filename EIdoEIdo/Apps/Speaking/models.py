from django.db import models
from datetime import datetime

class IELTS1Topics(models.Model):
    id = models.AutoField(primary_key=True)
    Topic = models.CharField(max_length=1000)
    Description = models.CharField(max_length=100)
    IsOld = models.BooleanField(default=False)

class IELTS1(models.Model):
    id = models.AutoField(primary_key=True)
    Topic = models.ForeignKey("Speaking.IELTS1Topics", on_delete=models.CASCADE)
    Question = models.CharField(max_length=1000)
    Intro_scr_file = models.FileField(upload_to='Corpus/IELTS1/introduce/', null=True)
    Src_file = models.FileField(upload_to='Corpus/IELTS1/file/', null=True)

class IELTS23Topics(models.Model):
    id = models.AutoField(primary_key=True)
    Topic = models.CharField(max_length=1000)
    Description = models.CharField(max_length=100)
    IsOld = models.BooleanField(default=False)

class IELTS2(models.Model):
    id = models.AutoField(primary_key=True)
    Topic = models.ForeignKey("Speaking.IELTS23Topics", on_delete=models.CASCADE)
    Question = models.CharField(max_length=1000)
    Requirement = models.CharField(max_length=1000)
    Intro_scr_file = models.FileField(upload_to='Corpus/IELTS2/introduce/', null=True)
    Src_file = models.FileField(upload_to='Corpus/IELTS2/file/', null=True)

class IELTS3(models.Model):
    id = models.AutoField(primary_key=True)
    Topic = models.ForeignKey("Speaking.IELTS23Topics", on_delete=models.CASCADE)
    Question = models.CharField(max_length=1000)
    Intro_scr_file = models.FileField(upload_to='Corpus/IELTS3/introduce/', null=True)
    Src_file = models.FileField(upload_to='Corpus/IELTS3/file/', null=True)
