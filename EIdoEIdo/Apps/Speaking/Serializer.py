from rest_framework import serializers
from . import models

class IELTS1TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IELTS1Topics
        fields = '__all__'

class IELTS23TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IELTS23Topics
        fields = '__all__'

class IELTS1Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.IELTS1
        fields = '__all__'

class IELTS2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.IELTS2
        fields = '__all__'

class IELTS3Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.IELTS3
        fields = '__all__'
