import django_filters
from .models import *


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Job
        fields = "__all__"
        exclude = ("image", "published_at", "vacancy", "owner", "salary")
