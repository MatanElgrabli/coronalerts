from django.db import models


class DayData(models.Model):
    date = models.DateField(primary_key=True)


class LabTest(models.Model):
    _id = models.IntegerField(primary_key=True)
    test_date = models.ForeignKey(DayData, on_delete=models.CASCADE)
    result_date = models.DateField()
    corona_result = models.BooleanField()
    lab_id = models.IntegerField()
    test_for_corona_diagnosis = models.BooleanField()
    is_first_Test = models.BooleanField()


class Quarantine(models.Model):
    _id = models.IntegerField(primary_key=True)
    date = models.ForeignKey(DayData, on_delete=models.CASCADE)
    isolated_today_contact_with_confirmed = models.IntegerField()
    isolated_today_abroad = models.IntegerField()
    new_contact_with_confirmed = models.IntegerField()
    new_from_abroad = models.IntegerField()
