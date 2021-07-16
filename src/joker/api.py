from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(["GET"])
def student_list_api(request):
    students = Student.objects.all()
    data = Subjectserializer(students, many=True).data
    return Response({"data": data, "status": 1000})


@api_view(["GET"])
def subject_list_api(request):
    subjects = Subject.objects.all()

    for subject in subjects:
        subject = subject.subject_student.all()

    data = Subjectserializer(subjects, many=True).data
    return Response({"data": data, "status": 1000})
