from rest_framework import serializers
from .models import Company_details,Branches,Departments,Designations,Employeess
from passlib.hash import django_pbkdf2_sha256 as handler
from rest_framework import status



class Company_detailsSerializer(serializers.ModelSerializer):
    company_user_email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=20, min_length=6, write_only=True)

    created_at = serializers.DateTimeField( read_only=True)
    # primary_uuid = serializers.CharField(w=True)
    class Meta:
        model=Company_details
        fields=('id','company','logo','company_user_email','password','description','andriod_app_permisiion','max_accesable_uuid_no','created_at','primary_uuid')

    def validate(self, data):
        if data["company"] and data["company_user_email"]:
            filtered_company = Company_details.objects.filter(company=data["company"])
            filtered_company_user_email = Company_details.objects.filter(company_user_email=data["company_user_email"])
            if filtered_company.exists() or filtered_company_user_email.exists():
                raise serializers.ValidationError(
                    "Already Company Name and Email Exist")
        data["password"]=handler.hash(data["password"])



        return data

    def delete(self, validated_data):
        raise serializers.ValidationError(
            {"message": "Contact Admin .", "status": status.HTTP_400_BAD_REQUEST,"action":'Failed'})


class Branch_details_Serializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=20, min_length=6, write_only=True)
    class Meta:
        model=Branches
        fields=('id','company_id','branch_name','email','password','address','primary_uuid','max_accesable_uuid_no')

    def validate(self, data):
        if data["email"] :
            filtered_company_email = Branches.objects.filter(email=data["email"])
            if filtered_company_email.exists() :
                raise serializers.ValidationError(
                    "Email Already Exist ...")
        data["password"]=handler.hash(data["password"])
        return data

class company_wise_branches_Serializer(serializers.ModelSerializer):
    company_branch_id = Branch_details_Serializer(many=True,read_only=True)
    company = serializers.CharField(read_only=True)
    class Meta:
        model = Company_details
        fields = ('company',"company_branch_id")

class deparments(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id','branch_deparments',"name")

class degignation(serializers.ModelSerializer):
    class Meta:
        model = Designations
        fields = ('id','department_wise_designation',"name")

class branchwise_departments(serializers.ModelSerializer):
    branch_deparments = deparments(many=True, read_only=True)
    id = serializers.CharField(read_only=True)
    branch_name = serializers.CharField(read_only=True)
    class Meta:
        model = Branches
        fields = ('id','branch_name', "branch_deparments",)


class deperment_wise_designations(serializers.ModelSerializer):
    department_wise_designation = degignation(many=True, read_only=True)
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    class Meta:
        model = Departments
        fields = ('id','name','department_wise_designation')

class all_deparments(serializers.ModelSerializer):
    # branch_deparments = serializers.CharField(read_only=True)
    class Meta:
        model = Departments
        fields = ('id','branch_deparments',"name")









class Register_EMPLOYEE_Serializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=14, min_length=6, write_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Employeess
        fields = ['id','company_id','branch_id','deparment_id','designation_id','email', 'username', 'password',"firstname","lastname",'status','created_at','profile_photo']
        # depth=1
    def validate(self, data):
        if not data["username"].isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        if data["email"] and data["username"]:
            email = Employeess.objects.filter(email=data["username"])
            username = Employeess.objects.filter(username=data["email"])
            if email.exists() or username.exists():
                raise serializers.ValidationError(
                    "already username and Email exist")
            data["password"] = handler.hash(data["password"])
        return data

class degignation_2(serializers.ModelSerializer):
    class Meta:
        model = Designations
        fields = ('id',"name")

class custom_employee_table(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    company_id = serializers.CharField(read_only=True)
    branch_id = serializers.CharField(read_only=True)
    employee_id = serializers.CharField(read_only=True)
    # profile_photo = serializers.CharField(read_only=True)

    class Meta:
        model = Employeess
        fields = ['id','company_id','branch_id','deparment_id','designation_id','email', 'username',"firstname","lastname", 'employee_id','status','created_at','profile_photo']
        depth=1

class employee_table_brach_wise(serializers.ModelSerializer):
    branch_id = custom_employee_table(many=True, read_only=True)

    class Meta:
            model = Branches
            fields = ('id', 'branch_name', "branch_id")


class employee_table_department_wise(serializers.ModelSerializer):
    deparment_id = custom_employee_table(many=True, read_only=True)
    id = serializers.CharField(read_only=True)
    # branch_name = serializers.CharField(read_only=True)

    class Meta:
        model = Departments
        fields = ('id', 'name', "deparment_id",)

class employee_table_designation_wise(serializers.ModelSerializer):
    designation_id = custom_employee_table(many=True, read_only=True)

    class Meta:
            model = Designations
            fields = ('id', 'name', "designation_id")



