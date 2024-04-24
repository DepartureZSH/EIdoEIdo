from rest_framework import serializers
from . import models

class CorpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Corpus
        fields = '__all__'
