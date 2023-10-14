from rest_framework import serializers
from .models import EmailModel

class EmailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailModel
        fields=('__all__')