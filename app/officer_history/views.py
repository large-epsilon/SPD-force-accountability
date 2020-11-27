import datetime
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Incident


def index(request):
    return TemplateResponse(request, "officer_history/index.html", {})


def officer_history(request):
    if request.method != "GET":
        return HttpResponse("No")

    serial = int(request.GET.get("serial_num"))
    incidents = Incident.objects.filter(officer_id=serial).order_by(
        "-occured_date_time"
    )
    return TemplateResponse(
        request,
        "officer_history/officer_history.html",
        {"incidents": incidents, "serial": serial},
    )
