from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
Job_TYPE = [("full time", "full time"), ("part time", "part time")]


def image_upolad(instance, filename):
    imagename, extension = filename.rsplit(".")
    return f"jobs/{instance.id}.{extension}"


def portfolio_upolad(instance, filename):
    portfolioname, extension = filename.rsplit(".")
    return f"portfolios/{instance.id}.{extension}"


class Job(models.Model):
    owner = models.ForeignKey(
        User, related_name="job_owner", on_delete=models.CASCADE, null=False
    )
    title = models.CharField(max_length=100, null=True)
    # location
    job_type = models.CharField(max_length=15, choices=Job_TYPE, null=True)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to=image_upolad, default="")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25, null=True)

    def calculateJobs(self):
        return Job.objects.filter(category=self).count()

    votes = property(calculateJobs)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(
        "Job", related_name="apply_job", on_delete=models.CASCADE, default=""
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to=portfolio_upolad, default="")
    coverletter = models.TextField(max_length=500)
    applyed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
