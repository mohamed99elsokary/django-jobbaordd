from django.shortcuts import render
from job.models import *


def home(request):
    job_list = Job.objects.all().order_by("-id")[:6]
    total = Job.objects.count()
    jobs_in_categoris = {}
    categories = Category.objects.all().order_by("-id")[:8]

    context = {
        "total": total,
        "job_list": job_list,
        "categories": categories,
    }
    return render(request, "home/index.html", context=context)
