from django.shortcuts import render
from .models import *


def send_message(request):
    data = Info.objects.first()
    context = {"data": data}
    return render(request, "contacts/contact.html", context=context)
    pass
