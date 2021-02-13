from django.urls import include, path
from hrmanagement import settings
from . import views
# from .views import
from rest_framework import routers
from .views import Apprizalview

router = routers.DefaultRouter()
router.register(r'employee-apprizal',Apprizalview)


urlpatterns = [
    path('', include(router.urls)),
    path('index',views.index ,name='index'),
    path('employee-apprizals/<int:id>/',views.employee_apprizal ,name='index'),

]