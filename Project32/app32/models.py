from django.db import models


class EmpModel(models.Model):
    Emp_ID = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Phone_No = models.IntegerField()
    Email_ID = models.CharField(max_length=100)

    def __str__(self):
        return self.Email_ID


class RoleModel(models.Model):
    RoleID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class DeptModel(models.Model):
    DeptID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class RoomModel(models.Model):
    RoomID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Facility = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class FacilityModel(models.Model):
    FacilityID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class PersonModel(models.Model):
    aadhar = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.pname


class PassportModel(models.Model):
    pno = models.IntegerField(primary_key=True)
    p_details = models.OneToOneField(PersonModel, on_delete=models.CASCADE)
