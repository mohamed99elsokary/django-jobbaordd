from django.urls import path
from . import api

urlpatterns = [
    path("subject", api.subject_list_api),
    path("users", api.student_list_api),
    # path("users/<int:id>/", api.job_details),
]
