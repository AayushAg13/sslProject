from django.db import models
from .constants import *
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class Faculty(models.Model):
    name = models.CharField(max_length=250, blank=True)

    webmail = models.CharField(max_length=250, unique=True, blank=True)
    department = models.CharField(choices=DEPARTMENT, max_length=250)

    def get_students(self):
        students = []
        for stud in Stud_Faculty_Status.objects.filter(faculty=Faculty.objects.get(webmail=self.webmail)):
            students.append(stud.student)
        return students

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250, blank=True)

    webmail = models.CharField(max_length=250, unique=True, blank=True)
    roll_no = models.IntegerField(default=0)
    hostel = models.CharField(choices=HOSTELS,max_length=250, blank=True)
    department = models.CharField(choices=DEPARTMENT, max_length=250)
    programme = models.CharField(choices=PROGRAMMES, max_length=250, default='B.Tech.')

    hostel_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    hostel_dues = models.BooleanField(default=True)
    hostel_remarks= models.CharField(max_length=1000, blank=True)

    gymkhana_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    gymkhana_dues = models.BooleanField(default=True)
    gymkhana_remarks= models.CharField(max_length=1000, blank=True)

    cc_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    cc_dues = models.BooleanField(default=True)
    cc_remarks= models.CharField(max_length=1000, blank=True)

    library_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    library_dues = models.BooleanField(default=True)
    library_remarks= models.CharField(max_length=1000, blank=True)

    cc_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    cc_dues = models.BooleanField(default=True)
    cc_remarks= models.CharField(max_length=1000, blank=True)

    hod_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    hod_dues = models.BooleanField(default=True)
    hod_remarks= models.CharField(max_length=1000, blank=True)

    finance_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    finance_dues = models.BooleanField(default=True)
    finance_remarks= models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def supervisor_status(self):
        if Stud_Faculty_Status.objects.filter(student=self):
            dept_status = True
            for fac in self.get_faculties():
                status = fac.faculty_approval
                if status is 3 or status is 1:
                    dept_status = False
                    break
            return dept_status
        else:
            return False

    def lab_status(self):
        if Stud_Lab_Status.objects.filter(student=self):
            lab_status = True
            for fac in Stud_Lab_Status.objects.filter(student=self):
                status = fac.lab_dues
                if status is True:
                    lab_status = False
                    break
            return lab_status
        else:
            return False


    #getting faculties related to the student
    def get_faculties(self):
        return Stud_Faculty_Status.objects.filter(student=self)

CHOICES = (
    (1, "Pending"),
    (2, "Approved"),
    (3, "Rejected")
)
class Stud_Faculty_Status(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    faculty_approval = models.IntegerField(choices = CHOICES, default=1)
    faculty_remarks= models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.student.name



class Caretaker(models.Model):
    name = models.CharField(max_length=250, blank=True)

    webmail = models.CharField(max_length=250, unique=True, blank=True)
    hostel = models.CharField(choices=HOSTELS,max_length=250, blank=True)


    def get_students(self):
        return Student.objects.filter(hostel=self.hostel)

    def __str__(self):
        return self.name

class Warden(models.Model):
    name = models.CharField(max_length=250, blank=True)

    webmail = models.CharField(max_length=250, unique=True, blank=True)
    hostel = models.CharField(choices=HOSTELS,max_length=250, blank=True)

    def get_students(self):
        return Student.objects.filter(hostel=self.hostel)

    def __str__(self):
        return self.name

class Assistant_registrar(models.Model):
    name = models.CharField(max_length=250, default='Assi. Registrar')

    webmail = models.CharField(max_length=250, unique=True, blank=True)
    def get_students(self):
        return Student.objects.all()

    def __str__(self):
        return self.name

class HOD(models.Model):
    name = models.CharField(max_length=250, blank=True)

    webmail = models.CharField(max_length=250, unique=True, blank=True)
    department = models.CharField(choices=DEPARTMENT, max_length=250)

    def get_students(self):
        return Student.objects.filter(department=self.department)

    def __str__(self):
        return self.name

class CC(models.Model):
    name = models.CharField(max_length=250, default='Computer Center')

    webmail = models.CharField(max_length=250, unique=True,blank=True)

    def get_students(self):
        return Student.objects.all()

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=250, default='Library')

    webmail = models.CharField(max_length=250, unique=True,blank=True)

    def get_students(self):
        return Student.objects.all()

    def __str__(self):
        return self.name

class Gymkhana(models.Model):
    name = models.CharField(max_length=250, default='Gymkhana')

    webmail = models.CharField(max_length=250, unique=True,blank=True)

    def get_students(self):
        return Student.objects.all()

    def __str__(self):
        return self.name

class OnlineCC(models.Model):
    name = models.CharField(max_length=250, default='OnlineCC Manager')

    webmail = models.CharField(max_length=250, unique=True,blank=True)

    def get_students(self):
        return Student.objects.all()

    def __str__(self):
        return self.name

class SubmitThesis(models.Model):
    name = models.CharField(max_length=250, default='Thesis Manager')

    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def get_students(self):
        return Student.objects.all()
    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=250, default='Finance')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def get_students(self):
        return Student.objects.all()
    def __str__(self):
        return self.name

class DeptAdmin(models.Model):
    name = models.CharField(max_length=250, default='Account')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    department = models.CharField(choices=DEPARTMENT, max_length=250)
    def __str__(self):
        return self.name

class Labs(models.Model):
    name = models.CharField(max_length=250)
    department = models.CharField(choices=DEPARTMENT, max_length=250)
    webmail = models.CharField(max_length=250, blank=True)
    def get_students(self):
        return Student.objects.all()

    def __str__(self):
        return self.name

class Stud_Lab_Status(models.Model):
    lab = models.ForeignKey(Labs,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lab_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    lab_dues = models.BooleanField(default=True)
    lab_remarks= models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.student.name
