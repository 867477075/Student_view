from django.http import JsonResponse
import json

from Stud_project.serializers import StudentSerializer

from stud_app.models import Student_Data


def student_details(request):
    if request.method == 'GET':
        result = Student_Data.objects.all()
        result = StudentSerializer(result,many=True)
        return JsonResponse(result.data, safe=False)

    elif request.method == 'POST':
        result_data = json.loads(request.body)

        result = StudentSerializer(data=result_data)
        if result.is_valid():
            result.save()
            messsage = {
            "Massage":"SUBMIT"

            }
        else:
            messsage = {
            "Massage": result.errors

            }
        return JsonResponse(messsage, safe=True)