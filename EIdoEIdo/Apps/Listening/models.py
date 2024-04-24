from django.db import models
from datetime import datetime

class Corpus(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Words_file = models.FileField(upload_to='Corpus/Listening/Words/')
    Src_file = models.FileField(upload_to='Corpus/Listening/File/')
    Create_time = models.DateTimeField(auto_now_add=True)
    Update_time = models.DateTimeField(auto_now=True)
