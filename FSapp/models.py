from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)


class Batch(models.Model):
    batch_name = models.CharField(max_length=10)
    batch_time = models.TimeField(max_length=10)
    date = models.DateField()


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Register_details(models.Model):
    name = models.CharField(max_length=20)
    DOB = models.DateField(default=0)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='profile')
    occupation = models.CharField(max_length=10)
    consultation_time = models.TimeField(null=True, blank=True)
    required_batch_name = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)
    required_batch_time = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class equipments(models.Model):
    equipments = models.CharField(max_length=20)
    equip_count = models.IntegerField()
    equip_weight = models.IntegerField()


class Instructor(models.Model):

    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='Batch')
    instructor = models.ForeignKey(Register_details, on_delete=models.CASCADE, related_name='Register_details')


class Attendance(models.Model):
    name = models.CharField(max_length=20)
    attendence = models.CharField(max_length=20)
    date = models.DateField()


class Bill(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='user')
    from_date = models.DateField()
    to_date = models.DateField()
    present_days = models.IntegerField()
    due_date = models.DateField()
    bill_status =models.BooleanField(default=False,help_text = "paid")
    amount =models.IntegerField()
    paid_on =models.DateField()

#
#
#
# Physican models
#
#
#
#
class health_details(models.Model):
    name = models.CharField(max_length=20)
    instructor = models.CharField(max_length=20)
    Height = models.IntegerField()
    Weight = models.IntegerField()
    transformation_status = models.CharField(max_length=200)
    medicine_consumption = models.CharField(max_length=200)
    health_issues =  models.CharField(max_length=200)

    def __str__(self):
        return self.name


class first_aid(models.Model):
    first_aid_1 = models.IntegerField()
    first_aid_2 = models.IntegerField()
    first_aid_3 = models.IntegerField()
    first_aid_4 = models.IntegerField()
    cause = models.CharField(max_length=50)

#   work pending
class appoinments(models.Model):
    name = models.CharField(max_length=20)
    physician = models.CharField(max_length=20)
    date = models.DateField()
    approval_status = models.IntegerField(default=0)
#     work pending

class medical_doubts(models.Model):
    name = models.CharField(max_length=20)
    doubts = models.TextField()


class diet(models.Model):
    food = models.CharField(max_length=20)
    time = models.TimeField()
    day = models.DateField(max_length=7)


class modelcomplaints(models.Model):
    name = models.CharField(max_length=20)
    complaints = models.TextField()