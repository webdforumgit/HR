from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Apprizals
from .serializers import apprizal
from permisiion.permission import BlocklistPermission


class Apprizalview(viewsets.ModelViewSet):
    queryset = Apprizals.objects.all()
    serializer_class = (apprizal)
    permission_classes = [BlocklistPermission ]





# @permission_classes([BlocklistPermission])
@api_view(['GET', 'POST'])
def index(request):
    if BlocklistPermission.has_permission(BlocklistPermission,request,request.method):
        if request.method == 'POST' and request.data:
            # permission_classes =
            print(BlocklistPermission.has_permission(request.data["li"],request.method))
            return Response({"message": "Got some data!", "data": request.data,"status":status.HTTP_200_OK})


        else:
            max_count=Apprizals.objects.all().count()
            if max_count > int(request.data["ll"]):
                queryset = Apprizals.objects.filter(emp_id=request.data['emp_id'])[int(request.data['ll']):int(request.data["hl"])]
                serialzer = apprizal(queryset, many=True)
                return Response({"message": serialzer.data, "status": status.HTTP_200_OK})
            else:
                return Response({"message": "No new data", "status": status.HTTP_204_NO_CONTENT})
    else:
        return Response({"message": "authentication problem", "status": status.HTTP_200_OK})


@api_view(['GET', 'POST'])
def employee_apprizal(request,id):
    if BlocklistPermission.has_permission(BlocklistPermission,request,request.method):
        if request.method == 'POST' and request.data:
            max_count=Apprizals.objects.all().count()
            if int(request.data["ll"])==0:
                queryset = Apprizals.objects.filter(emp_id=id)[int(request.data['ll']):int(request.data["hl"])]
                serialzer = apprizal(queryset, many=True)
                if queryset.exists():
                    return Response({"message": serialzer.data, "status": status.HTTP_200_OK})
                else:
                    return Response({"message": "No Apprizal Submitted Yet", "status": status.HTTP_204_NO_CONTENT})
            elif max_count > int(request.data["ll"]):
                queryset = Apprizals.objects.filter(emp_id=id)[int(request.data['ll']):int(request.data["hl"])]
                serialzer = apprizal(queryset, many=True)
                return Response({"message": serialzer.data, "status": status.HTTP_200_OK})
            else:
                return Response({"message": "No More Apprizal Found", "status": status.HTTP_204_NO_CONTENT})
    else:
        return Response({"message": "authentication problem", "status": status.HTTP_200_OK})