from django.http import HttpResponse,request,JsonResponse

from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Company_details,Branches,Departments,Designations,Employeess
from .serializers import Company_detailsSerializer,Branch_details_Serializer,\
    company_wise_branches_Serializer,deparments,degignation,branchwise_departments,deperment_wise_designations,all_deparments,Register_EMPLOYEE_Serializer,\
    employee_table_brach_wise,employee_table_department_wise,employee_table_designation_wise,custom_employee_table
from passlib.hash import django_pbkdf2_sha256 as handler
from django.http import Http404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST' and request.data:
        print("psot")
        return Response({"message": "Got some data!", "data": request.data,"status":status.HTTP_200_OK})
    else:
        return Response({"message":"No Data Given to post","status":status.HTTP_204_NO_CONTENT})
    return Response({"message": "Hello, world!"})


# api_view strat
class Company_detail_crud(APIView):


    def hash_rawpassword(self, password):
        hashed_password = handler.hash(password)
        return hashed_password
#     """
#     Retrieve, update or delete a snippet instance.
#     """

    def post(self, request, format=None):
        serializer = Company_detailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data['logo']:
                print(request.data['logo'])

            return Response({"message": serializer.data, "status": status.HTTP_201_CREATED,"action":'Data Inserted Successfully'})
        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})


    def get_object(self, pk):
        try:
            return Company_details.objects.get(pk=pk)
        except Company_details.DoesNotExist:
            raise Http404


    def get(self, request, pk,  format=None):
        Company_details = self.get_object(pk)
        serializer = Company_detailsSerializer(Company_details)
        return Response({"message": serializer.data, "status": status.HTTP_200_OK, "action":'Data Fetched Successfully' })

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Company_detailsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": serializer.data, "status": status.HTTP_200_OK, "action":'Data Updated Successfully' })
        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    def delete(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Contact Admin .", "status": status.HTTP_400_BAD_REQUEST,"action":'Failed'})


class Branch_details_APIView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

    def post(self, request, format=None):
        serializer = Branch_details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": serializer.data, "status": status.HTTP_201_CREATED,"action":'Data Inserted Successfully'})
        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})


    def get_object(self, pk):
        try:
            return Branches.objects.get(pk=pk)
        except Company_details.DoesNotExist:
            raise Http404


    def get(self, request, pk,  format=None):
        Company_details = self.get_object(pk)
        serializer = Branch_details_Serializer(Company_details)
        return Response({"message": serializer.data, "status": status.HTTP_200_OK, "action":'Data Fetched Successfully' })

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Branch_details_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": serializer.data, "status": status.HTTP_200_OK, "action":'Data Updated Successfully' })
        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    def delete(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Contact Admin .", "status": status.HTTP_400_BAD_REQUEST,"action":'Failed'})

class employee_register(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     queryset = Employeess.objects.all()
#     serializer_class = (Register_EMPLOYEE_Serializer)
    def post(self, request, format=None):
        serializer = Register_EMPLOYEE_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = Employeess.objects.get(email=user_data['email'])
            current_site = get_current_site(request).domain
            relativeLink = '/verify_email'
            absolute_url = 'http://' + current_site + relativeLink + "?id=" + str(user.id)
            # email_body = "Hi " + user.username + "use the link to verify your email \n" + absolute_url
            # data = {'email_body': email_body, "email_subject": "Verify Mail ", "email_to": user.email}
            print(absolute_url)
            return Response({"message": serializer.data, "status": status.HTTP_201_CREATED,"action":'Data Inserted Successfully'})
        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

class verify_email(APIView):
    #     """
    #     Retrieve, update or delete a snippet instance.
    #     """
    #     queryset = Employeess.objects.all()
    #     serializer_class = (Register_EMPLOYEE_Serializer)
    def get(self, request):
        id = self.request.query_params.get('id', None)
        print(self.request.query_params)
        try:
            user = Employeess.objects.filter(id=id)
            if user.exists():
                user = Employeess.objects.get(id=id)
                if user.is_verified == False:
                    user.is_verified = True
                    user.is_active = True
                    total_employee_count = Employeess.objects.filter(company_id_id=user.company_id_id, is_verified=True)
                    company_detail = Company_details.objects.get(id=user.company_id_id)
                    user_id = user.id
                    if len(total_employee_count) < 9:
                        empid = '00' + str(len(total_employee_count) + 1)
                    elif len(total_employee_count) < 99:
                        empid = '0' + str(len(total_employee_count) + 1)
                    else:
                        empid = str(len(total_employee_count) + 1)
                    employee_id = company_detail.company + '/' + empid
                    user.employee_id = employee_id
                    user.save()
                    return Response({'success': 'Successfully activated', 'Employee_ID': employee_id},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Accout Already Verified'}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)



# api_view end

# Model View strat
class Company_details_View(viewsets.ModelViewSet):
    queryset = Company_details.objects.all()
    serializer_class = (Company_detailsSerializer)

class all_Branch_details(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = (Branch_details_Serializer)

class company_wise_branches(viewsets.ModelViewSet):
    queryset = Company_details.objects.all()
    serializer_class = (company_wise_branches_Serializer)

class deparments(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = (deparments)

class all_deparments(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = (all_deparments)

class degignations(viewsets.ModelViewSet):
    queryset = Designations.objects.all()
    serializer_class = (degignation)

class branchwise_departments(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = (branchwise_departments)

class deperment_wise_designation(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = (deperment_wise_designations)


class Register_EMPLOYEE(viewsets.ModelViewSet):
    queryset = Employeess.objects.all()
    serializer_class = (Register_EMPLOYEE_Serializer)
# Model View end

#custom Api
@api_view(['POST'])
def company_login(request):
    email = request.data['email']
    password = request.data['password']
    snippet=Company_details.objects.get(company_user_email=email)
    serializer = Company_detailsSerializer(snippet)
    if snippet and handler.verify(password, snippet.password):
        return Response({"message": "successfully logged in", "data": serializer.data,"status":status.HTTP_200_OK})
    else:
        return Response({"message":"Invalid Credential","status":status.HTTP_400_BAD_REQUEST})
def validateEmail( email ):
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False
def get_object(pk):
    try:
        return Branches.objects.filter(pk=pk)
    except Company_details.DoesNotExist:
        raise Http404
        return Response({"message": "Branch Does Not Exist", "status": status.HTTP_400_BAD_REQUEST})
@api_view(['POST'])
def branch_login_company(request,pk):
    my_custom_headers = request.headers.get('My-Custom-Header')
    email = request.data['email']
    if validateEmail(my_custom_headers) and my_custom_headers==email:
        print(str(my_custom_headers))
        snippet = Branches.objects.get(pk=pk)
        serializer = Branch_details_Serializer(snippet)
        if snippet.email == email:
            return Response({"message": "successfully logged in", "data": serializer.data,"status":status.HTTP_200_OK})
        else:
            return Response({"message":"Invalid Credential","status":status.HTTP_400_BAD_REQUEST})
    else:
        return Response({"message": "Access control issue", "status": status.HTTP_400_BAD_REQUEST})






@api_view(['POST'])
def employee_table(request):
    if 'designation_id' in request.data:
        try:
            snippet = Designations.objects.get(id=request.data["designation_id"])
            serializer = employee_table_designation_wise(snippet)
            print("ok1")
            return Response(
                {"message": "Employee Fetched Deparment Wise", "data": serializer.data, "status": status.HTTP_200_OK})
        except :
            return Response({"message": "No data Found", "status": status.HTTP_400_BAD_REQUEST})

    if 'deparment_id' in request.data:
        try:

            snippet = Departments.objects.get(id=request.data['deparment_id'])
            serializer = employee_table_department_wise(snippet)
            print("ok2")
            return Response(
                {"message": "Employee Fetched Deparment Wise", "data": serializer.data, "status": status.HTTP_200_OK})
        except :
            return Response({"message": "No data Found", "status": status.HTTP_400_BAD_REQUEST})

    if 'branch_id' in request.data:
        try:
            print("ok3")
            snippet = Branches.objects.get(id=request.data['branch_id'])
            serializer = employee_table_brach_wise(snippet)
            return Response(
                {"message": "Employee Fetched Deparment Wise", "data": serializer.data, "status": status.HTTP_200_OK})
        except :
            return Response({"message": "No data Found", "status": status.HTTP_400_BAD_REQUEST})



    return Response({"message": "Fetal Error", "status": status.HTTP_400_BAD_REQUEST})






@api_view(['POST'])
def employee_login(request):
    email = request.data['email']
    password = request.data['password']
    snippet=Employeess.objects.get(email=email)
    serializer = Register_EMPLOYEE_Serializer(snippet)
    if snippet and handler.verify(password, snippet.password):
        return Response({"message": "successfully logged in", "data": serializer.data,"status":status.HTTP_200_OK})
    else:
        return Response({"message":"Invalid Credential","status":status.HTTP_400_BAD_REQUEST})


@api_view(['PUT'])
def update_employee_status(request,pk):
    # try:
    status_updated=request.data["status"]
    snippets =Employeess.objects.filter(pk=pk).update(status=status_updated)
    return Response(
        {"message": "Updated", "status": status.HTTP_200_OK, "action": 'Updated Successfully'})
    # except:
    #     return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})
