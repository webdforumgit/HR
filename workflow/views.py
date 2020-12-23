from django.http import HttpResponse,request,JsonResponse

from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import workflow,work_flow_employee_detail,uploded_file,custom_workflow_wise_employee,custom_employee_wise_workflows
from .models import Work_flow,Work_flow_employee_detail,Uplodaed_file
from datetime import date,timedelta
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser
import base64
# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST' and request.data:
        return Response({"message": "Got some data!", "data": request.data,"status":status.HTTP_200_OK})
    else:
        return Response({"message":"No Data Given to post","status":status.HTTP_204_NO_CONTENT})



class Workflow_employee_APIView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

    def post(self, request, format=None):
        serializer = work_flow_employee_detail(data=request.data)
        if serializer.is_valid(request.data):
                serializer.save()
                return Response({"message": serializer.data, "status": status.HTTP_201_CREATED,"action":'Data Inserted Successfully'})
        return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    def get(self, request,workflow_id, format=None):
        try:
            snippet = Work_flow_employee_detail.objects.filter(workflow_id=workflow_id)
            serializer = custom_workflow_wise_employee(snippet,many=True)
            return Response({"message": serializer.data,"status": status.HTTP_200_OK, "action":'Data Fetched Successfully' })
        except:
            return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})


class Workflow_APIView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     "

    def post(self, request, format=None):
        try:
            today = date.today()
            yesterday = today - timedelta(days=0)
            samples = Work_flow.objects.filter(dead_line__lte=today,is_done=False).update(status = "PENDING")
            snippets = Work_flow.objects.filter(branch_wise_workflow=request.data["branch_wise_workflow"],is_done=False).order_by('-dead_line').reverse()
            serializer = workflow(snippets,many=True)
            return Response(
                {"message": serializer.data, "status": status.HTTP_200_OK, "action": 'Data Inserted Successfully'})
            # return Response({"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
        except:
            return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})




class Workflow(viewsets.ModelViewSet):
    queryset = Work_flow.objects.all()
    serializer_class = (workflow)

class Work_flow_employee_detail_ModelViewSet(viewsets.ModelViewSet):
    queryset = Work_flow_employee_detail.objects.all()
    serializer_class = (work_flow_employee_detail)

class Uplodaed_files(viewsets.ModelViewSet):
    queryset = Uplodaed_file.objects.all()
    serializer_class = (uploded_file)



@api_view(['POST'])
def documents_employee_wise(request):
    try:
        snippets = Uplodaed_file.objects.filter(workflow_id_uplodaed_file=request.data["workflow_id_uplodaed_file"])
        serializer = uploded_file(snippets, many=True)
        return Response(
            {"message": serializer.data, "status": status.HTTP_200_OK, "action": 'Data Inserted Successfully'})
    except:
        return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})

@api_view(['POST'])
def update_role_assigment(request,pk):
    try:
        role=request.data["role"]
        assignment = request.data["assignment"]
        snippets = Work_flow_employee_detail.objects.filter(pk=pk).update(role=role,assignment=assignment)
        return Response(
            {"message": "Updated", "status": status.HTTP_200_OK, "action": 'Data Inserted Successfully'})
    except:
        return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})

@api_view(['GET'])
def employee_wise_workflows(request,pk):
    try:
        today = date.today()
        samples = Work_flow.objects.filter(dead_line__lte=today, is_done=False).update(status="PENDING")
        snippets = Work_flow_employee_detail.objects.filter(emp_id=pk,
                                            ).order_by("workflow_id").reverse()
        serializer = custom_employee_wise_workflows(snippets, many=True)
        return Response(
            {"message": serializer.data, "status": status.HTTP_200_OK, "action": 'Data Inserted Successfully'})
    except:
        return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})


from django.core.files.storage import FileSystemStorage
class PostView(APIView):
    parser_classes = (FileUploadParser,)
    def post(self, request,filename, format=None):
        # try:
            # data=request.headers.get("My-Custom-Header").split("/")
            # Uplodaed_file.objects.create(workflow_id_uplodaed_file_id=data[0],remarks=data[1],file=request.FILES["file"])
            # return Response({"message": "File Uploded", "status": status.HTTP_200_OK})
        fs = FileSystemStorage()
        file = fs.save(filename, request.FILES["file"])
        data = request.headers.get("My-Custom-Header").split("/")
        Uplodaed_file.objects.create(workflow_id_uplodaed_file_id=data[0], remarks=data[1], file=file)
        return Response({"message": "File Uploded", "status": status.HTTP_200_OK})
    # except:
    #         return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})


@api_view(['POST'])
def update_progress(request,pk):
    try:
        progress=request.data["progress"]
        snippets = Work_flow_employee_detail.objects.filter(pk=pk).update(progress=progress)
        return Response(
            {"message": "Updated", "status": status.HTTP_200_OK, "action": 'Updated Successfully'})
    except:
        return Response({"message": "Bad Request", "status": status.HTTP_400_BAD_REQUEST})