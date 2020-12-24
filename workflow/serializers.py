from rest_framework import serializers
from .models import Work_flow,Work_flow_employee_detail,Uplodaed_file
from structure.models import Employeess

class workflow(serializers.ModelSerializer):
    created_time = serializers.CharField(read_only=True)
    class Meta:
        model = Work_flow
        fields = ('id','branch_wise_workflow',"name","created_time","dead_line","is_done","status")


class custom_employee_table(serializers.ModelSerializer):

    class Meta:
        model = Employeess
        fields = ('id','email',"firstname","lastname",'profile_photo')




class work_flow_employee_detail(serializers.ModelSerializer):
    # emp_id = custom_employee_table(read_only=True)
    class Meta:
        model = Work_flow_employee_detail
        fields = ('id','workflow_id',"emp_id","role","assignment","progress","status")
        # depth=1
    def validate(self, data):
        if data["workflow_id"] and data["emp_id"]:
            query = Work_flow_employee_detail.objects.filter(workflow_id=data["workflow_id"],emp_id_id=data["emp_id"])
            if query.exists():
                raise serializers.ValidationError(
                    "Employee already in workflow Already Exist ...")
        return data




class uploded_file(serializers.ModelSerializer):
    class Meta:
        model = Uplodaed_file
        fields = ('id','workflow_id_uplodaed_file','remarks',"file")




class custom_workflow_wise_employee(serializers.ModelSerializer):
    emp_id = custom_employee_table(read_only=True)
    class Meta:
        model = Work_flow_employee_detail
        fields = ('id','workflow_id',"emp_id","role","assignment","progress","status")

class custom_employee_wise_workflows(serializers.ModelSerializer):
    workflow_id = workflow(read_only=True)
    class Meta:
        model = Work_flow_employee_detail
        fields = ('id','workflow_id',"emp_id")

#test upload git
#test upload git2