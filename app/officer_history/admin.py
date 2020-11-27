import csv
import datetime
import io

from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    def get_urls(self):
        super_urls = super().get_urls()
        urls = [
            path("upload_csv/", self.admin_site.admin_view(self.upload_csv_view)),
        ]
        return urls + super_urls

    def upload_csv_view(self, request):
        if request.method == "GET":
            return self.upload_csv_view_get(request)
        elif request.method == "POST":
            return self.upload_csv_view_post(request)
        return HttpResponse("What are you even doing? Stop it.")

    def upload_csv_view_get(self, request):
        context = dict(self.admin_site.each_context(request),)
        return TemplateResponse(
            request, "officer_history/admin/upload_csv.html", context
        )

    def upload_csv_view_post(self, request):
        csv_data = request.POST.get("csv", "")
        reader = csv.DictReader(
            io.StringIO(csv_data),
            fieldnames=[
                "ID",
                "Incident_Num",
                "Incident_Type",
                "Occured_date_time",
                "Precinct",
                "Sector",
                "Beat",
                "Officer_ID",
                "Subject_ID",
                "Subject_Race",
                "Subject_Gender",
            ],
        )

        total_saved = 0
        for row in reader:
            date = datetime.datetime.strptime(
                row["Occured_date_time"], "%m/%d/%Y %I:%M:%S %p"
            )
            Incident(
                incident_num=row["Incident_Num"],
                incident_type=row["Incident_Type"],
                occured_date_time=date.strftime("%Y-%m-%d %H:%M:%S"),
                precinct=row["Precinct"],
                sector=row["Sector"],
                beat=row["Beat"],
                officer_id=int(row["Officer_ID"]),
                subject_id=int(row["Subject_ID"]),
                subject_race=row["Subject_Race"],
                subject_gender=row["Subject_Gender"],
            ).save()
            total_saved += 1

        return HttpResponse("Added {} incidents".format(total_saved))
