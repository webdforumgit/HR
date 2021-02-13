from rest_framework import serializers
from .models import Attendence,Attendence_sample_video
from structure.models import Employeess
import os
from hrmanagement.settings import BASE_DIR

class attendence(serializers.ModelSerializer):
    intime = serializers.DateField(format="%H:%M:%S",read_only=True)
    outtime = serializers.DateField(format="%H:%M:%S",read_only=True)
    class Meta:
        model = Attendence
        fields = ('id','date',"intime","out_time_recorded",'outtime')

class uploded_video(serializers.ModelSerializer):
    class Meta:
        model = Attendence_sample_video
        fields = ('id','employee_id',"file")

    def validate(self, data):
        if data["employee_id"] :
                query = Attendence_sample_video.objects.filter(employee_id=data["employee_id"])
                if query.exists():
                    samp = Attendence_sample_video.objects.get(employee_id=data["employee_id"])
                    os.remove(str(BASE_DIR)+'/media/'+str(samp.file))
                    query.delete()
        else:
            raise serializers.ValidationError(
                "Wrong Employee ID")

        return data