from django.db import models
from django.utils import timezone


class Student(models.Model):
    student_id = models.CharField(max_length=15, null=False, blank=False)
    full_name = models.CharField(max_length=250, null=False, blank=False)
    sex = models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female')], null=False, blank=False)
    department = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.full_name


class Food(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    stock = models.IntegerField()
    date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    serial_no = models.CharField(max_length=12)
    date = models.DateTimeField(null=False, blank=False)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.serial_no}"


class Order(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False, blank=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField()
    date = models.DateTimeField(null=False, blank=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food} - {self.quantity}"


class StudentTicket(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    ticket = models.ManyToManyField(Ticket)

    def __str__(self):
        return f"{self.student} - {self.ticket}"
