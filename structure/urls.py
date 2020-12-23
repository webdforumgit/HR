from django.urls import include, path
from hrmanagement import settings
from . import views
from .views import Company_details_View,Company_detail_crud,all_Branch_details,company_wise_branches,\
    deparments,degignations,branchwise_departments,deperment_wise_designation,all_deparments,Register_EMPLOYEE,employee_table,employee_register,verify_email

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'company-details',Company_details_View)
router.register(r'Branch_details_View',all_Branch_details)
router.register(r'company-wise-branches',company_wise_branches)
router.register(r'department',deparments)
router.register(r'designations',degignations)
router.register(r'branchwise-departments',branchwise_departments)
router.register(r'deperment-wise-designation',deperment_wise_designation)
router.register(r'all-deparments',all_deparments)
# router.register(r'verify-email',verify_email)


urlpatterns = [
    path('', include(router.urls)),
    path('index',views.index ,name='index'),
    path('company_login',views.company_login ,name='company_login '),
    path('employee_table',views.employee_table ,name='employee_table '),
    path('branch_login_company/<int:pk>/',views.branch_login_company ,name='branch_login_company '),
    path(r'register_company_details/', views.Company_detail_crud.as_view()),
    path(r'company_details/<int:pk>/', views.Company_detail_crud.as_view()),
    path(r'register_Branch_details/', views.Branch_details_APIView.as_view()),
    path(r'Branch_details/<int:pk>/', views.Branch_details_APIView.as_view()),
    path(r'employee_register/', views.employee_register.as_view()),
    path(r'verify_email/', views.verify_email.as_view()),
    path('employee-login/',views.employee_login ,name='employee-login'),
    path('update-employee-status/<int:pk>/',views.update_employee_status ,name='employee-login'),




]
# urlpatterns = format_suffix_patterns(urlpatterns) employee_login
