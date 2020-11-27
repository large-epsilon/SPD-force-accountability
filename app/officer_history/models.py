from django.db import models

# A single use of force incident.
class Incident(models.Model):
    incident_num = models.CharField(max_length=50)
    incident_type = models.CharField(max_length=50)
    occured_date_time = models.DateTimeField()
    precinct = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    beat = models.CharField(max_length=50)
    officer_id = models.IntegerField()
    subject_id = models.IntegerField()
    subject_race = models.CharField(max_length=50)
    subject_gender = models.CharField(max_length=50)
