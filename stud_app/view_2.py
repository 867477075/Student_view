import json

from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from stud_app.models import Student_Data


def welcome(request):

    return HttpResponse("Welcome to v2 page")


class StudentDetails(APIView):

    def get(self,request):
        student_object = Student_Data.objects.all()

        student_details = {student.roll_no: student.name for student in student_object}

        return Response(student_details)

    def delete(self,request):
        data = json.loads(request.body)
        remove_id = data.get("id")
        breakpoint()
        student_object = Student_Data.objects.get(pk=remove_id)

        if student_object:
            student_object.delete()
            message = {
                "Message": "Record deleted Successfully"
            }

        return Response(message)

    def post(self,request):
        result_data = json.loads(request.body)
        result = Student_Data.objects.create(**result_data)
        result.save()
        data = {
            "Message":"Submitted"
        }

        return Response(data)


