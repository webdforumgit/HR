from rest_framework import serializers
from .models import Apprizals

class apprizal(serializers.ModelSerializer):
    # intime = serializers.DateField(format="%H:%M:%S")
    # outtime = serializers.DateField(format="%H:%M:%S")
    class Meta:
        model = Apprizals
        fields = ('__all__')

