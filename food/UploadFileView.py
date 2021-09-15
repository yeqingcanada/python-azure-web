from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json
import csv
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from food.models import Departments,Employees
from food.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
def UploadFile(request):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method=='POST':
        print('----------------0------------------')
        file=request.FILES['myFile']
        print('----------------1------------------')
        decoded_lines = file.read().decode('utf-8-sig').splitlines()
        print('----------------2------------------')
        csvReader = csv.DictReader(decoded_lines)
        print('----------------3------------------')
        for rows in csvReader:
            # rows['DepartmentId'] = int(rows['DepartmentId'])
            department_data = json.dumps(rows)
            print(department_data)
            department_serializer = DepartmentSerializer(data=json.loads(department_data))
            print(department_serializer)
            if department_serializer.is_valid():
                department_serializer.save()
                print(rows['DepartmentId'])

    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)