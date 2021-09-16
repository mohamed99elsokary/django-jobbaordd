from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    major = models.ForeignKey(
        "Subject", on_delete=models.CASCADE, related_name="subject_student"
    )

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
