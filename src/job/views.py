from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import *
from django.db import connections


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    total = job_list.count()
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"jobs": page_obj, "total": total, "myfilter": myfilter}
    return render(request, "job/job_list.html", context=context)


def job_details(request, name):
    name = name.replace("-", " ")
    job_details = Job.objects.get(title=name)
    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form = ApplyForm()
    context = {"job": job_details, "form": form}
    return render(request, "job/job_details.html", context=context)


@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            """for i in range(100000):
                cursor = connections["default"].cursor()
                cursor.execute(
                    "INSERT INTO job_job(title , job_type  , description  , published_at  , vacancy  ,salary  ,experience  , image  ,category_id  , owner_id ) VALUES( %s , %s,%s , %s,%s , %s,%s , %s,%s , %s )",
                    [
                        "title",
                        "full time",
                        "cvbcbg",
                        "2021-07-08 18:39:43.845457",
                        "1",
                        "6",
                        "1",
                        "jobs/None_jVy3J9J.png",
                        "5",
                        "9",
                    ],
                )"""

            return redirect(reverse("jobs:job_list"))

    else:
        form = JobForm()
    context = {"form": form}
    return render(request, "job/add_job.html", context=context)
