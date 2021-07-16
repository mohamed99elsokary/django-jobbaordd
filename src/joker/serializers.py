from rest_framework import serializers
from .models import *


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class Subjectserializer(serializers.ModelSerializer):
    # teachers = Studentserializer(source="student_set", many=True)

    class Meta:
        model = Subject
        fields = "__all__"
