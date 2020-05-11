from django.db import models
from django.utils import timezone
from datetime import datetime


class Shift(models.Model):
    shift_name = models.CharField(max_length=50)
    shift_from = models.TimeField()
    shift_to = models.TimeField()

    def __str__(self):
        return self.shift_name


class QrCode(models.Model):
    emp_code = models.CharField(max_length=100)
    # time = models.TimeField()
    # time = models.DateTimeField(editable=False)
    # time = models.DateTimeField(default=timezone.now)
    scan_date = models.DateField(default=datetime.now)
    scan_time = models.TimeField(default=datetime.now)
    temperature = models.CharField(blank=True, null=True, max_length=50)
    # shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    punch = models.CharField(blank=True, null=True, max_length=50)


class EmployeeData(models.Model):
    emp_code = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=100)
    emp_photo = models.FileField(upload_to='emp_photos/')
