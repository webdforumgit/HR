from django.urls import include, path
from hrmanagement import settings
from . import views
# from .views import
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Workflow,Work_flow_employee_detail_ModelViewSet,Uplodaed_files,Workflow_employee_APIView,Workflow_APIView,PostView

router = routers.DefaultRouter()
router.register(r'Work-flow',Workflow)
router.register(r'Work-flow-employee-wise',Work_flow_employee_detail_ModelViewSet)
router.register(r'Uplodaed-files',Uplodaed_files)


urlpatterns = [
    path('', include(router.urls)),
    path('index',views.index ,name='index'),
    path('add-employee-to-workflow/',Workflow_employee_APIView.as_view()),
    path('retrive-employee-workflow-wise/<int:workflow_id>/',Workflow_employee_APIView.as_view()),
    path('brachwise-Workflow/',Workflow_APIView.as_view()),
    path('documents-employee-wise/',views.documents_employee_wise ,name='documents-employee-wise'),
    path('update-role-assigment/<int:pk>/',views.update_role_assigment ,name='update-role-assigment'),
    path('employee-wise-workflows/<int:pk>/',views.employee_wise_workflows ,name='employee-wise-workflows'),
    path('upload-file/<str:filename>/',PostView.as_view()),
    path('update-progress/<int:pk>/',views.update_progress ,name='update-role-assigment'),


]
