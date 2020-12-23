from rest_framework import serializers
from .models import Attendence

class attendence(serializers.ModelSerializer):
    intime = serializers.DateField(format="%H:%M:%S",read_only=True)
    outtime = serializers.DateField(format="%H:%M:%S",read_only=True)
    class Meta:
        model = Attendence
        fields = ('id','date',"intime","out_time_recorded",'outtime')