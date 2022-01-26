import string
import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from Restaurant.forms import LoginForm, ValidateTicketForm, OrderForm, StudentForm, FoodForm
from Restaurant.models import Student, StudentTicket, Food, Order, Ticket

random = random.Random()


def index(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                ticket_id = form.cleaned_data['ticket_id']
                student_id = form.cleaned_data['student_id'].upper()
                food_name = form.cleaned_data['food_name']
                quantity = form.cleaned_data['quantity']

                current_food = get_object_or_404(Food, name=food_name)

                if current_food.stock < quantity:
                    messages.error(request, "Quantity of {current_food.name} left is {current_food.quantity}")
                    return HttpResponseRedirect(reverse('Cafeteria:home'))
                elif current_food.stock == 0:
                    messages.error(request, "Meal unavailable")
                    return HttpResponseRedirect(reverse('Cafeteria:home'))

                all_student = Student.objects.all()
                for student in all_student:
                    if student_id == student.student_id:
                        current_student = get_object_or_404(Student, student_id=student_id)
                        current_student.save()
                        break
                else:
                    messages.error(request, "Student does not exist")

                all_ticket = Ticket.objects.all()
                for ticket in all_ticket:
                    if ticket_id == ticket.serial_no:
                        current_ticket = get_object_or_404(Ticket, serial_no=ticket_id)
                        current_ticket.save()

                        if not current_ticket.is_valid:
                            messages.error(request, "Ticket already used")
                            return HttpResponseRedirect(reverse('Cafeteria:home'))
                        elif (timezone.now() - current_ticket.date) > timezone.timedelta(hours=24):
                            messages.error(request, "Ticket already outdated")
                            return HttpResponseRedirect(reverse('Cafeteria:home'))
                        break

                else:
                    messages.error(request, "Ticket does not exist")

                current_student_ticket = get_object_or_404(StudentTicket, student=current_student)
                current_student_ticket.save()

                for ticket in current_student_ticket.ticket.all():
                    if ticket_id == ticket.serial_no:
                        current_order = Order.objects.create(student=current_student, food=current_food,
                                                             ticket=current_ticket, quantity=quantity,
                                                             date=timezone.now())
                        current_order.save()
                        return render(request, 'restaurant/confirm_order.html', {'current_order': current_order})
                else:
                    messages.error(request, "Ticket input is not allocated to the student")
                    return HttpResponseRedirect(reverse('Cafeteria:home'))
        else:
            form = OrderForm()
        return render(request, 'restaurant/order.html', {'form': form})
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None and not user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Cafeteria:home'))
                else:
                    messages.error(request, "Invalid login details")
                    return HttpResponseRedirect(reverse('Cafeteria:home'))

        else:
            form = LoginForm()
        return render(request, 'restaurant/index.html', {'form': form})


def confirm_order(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        messages.success(request, "Meal successfully ordered")
        return render(request, 'restaurant/confirm_order.html')
    else:
        messages.error(request, "Kindly login please")
        return HttpResponseRedirect(reverse('Cafeteria:home'))


def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_verified = True
    order.ticket.is_valid = False
    order.ticket.save()
    order.save()

    food = order.food
    food.stock -= order.quantity
    food.save()

    current_student_ticket = get_object_or_404(StudentTicket, student=order.student)
    current_student_ticket.ticket.remove(order.ticket)
    current_student_ticket.save()

    return HttpResponseRedirect(reverse('Cafeteria:home'))


def decline_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return HttpResponseRedirect(reverse('Cafeteria:home'))


def student_registration(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data['full_name'].strip().upper()
                student_id = form.cleaned_data['student_id'].strip().upper()
                sex = form.cleaned_data['sex'].strip()
                department = form.cleaned_data['department'].strip().upper()
                all_student = Student.objects.all()
                for student in all_student:
                    if student_id == student.student_id:
                        messages.error(request, "Student already exists, kindly input the correct information")
                        return HttpResponseRedirect(reverse('Cafeteria:student_registration'))
                else:
                    Student.objects.create(full_name=full_name, student_id=student_id, sex=sex, department=department)
                    messages.success(request, "Student successfully registered")
                    return HttpResponseRedirect(reverse('Cafeteria:home'))

        else:
            form = StudentForm()
        return render(request, 'restaurant/register.html', {'form': form})
    else:
        messages.error(request, "Kindly login please")
        return HttpResponseRedirect(reverse('Cafeteria:home'))


def meal_menu(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if request.method == 'POST':
            form = FoodForm(request.POST)
            if form.is_valid():
                food_name = form.cleaned_data['food_name']
                stock = form.cleaned_data['stock']

                all_food = Food.objects.all()
                for food in all_food:
                    if food_name == food.name:
                        messages.error(request, "Meal already available in the menu")
                        return HttpResponseRedirect(reverse('Cafeteria:meal_menu'))
                else:
                    Food.objects.create(name=food_name, stock=stock, date=timezone.now())
                    messages.success(request, "Meal added successfully")
                    return HttpResponseRedirect(reverse('Cafeteria:meal_menu'))

        else:
            form = FoodForm()
        return render(request, 'restaurant/meal_menu.html', {'form': form})
    else:
        messages.error(request, "Kindly login please")
        return HttpResponseRedirect(reverse('Cafeteria:home'))


def ticket_generator(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return render(request, 'restaurant/ticket_generator.html')
    else:
        messages.error(request, "Kindly login please")
        return HttpResponseRedirect(reverse('Cafeteria:home'))


def create_tickets(request):
    all_students = Student.objects.all()
    all_tickets = Ticket.objects.all()
    for student in all_students:
        current_student_ticket = StudentTicket.objects.create(student=student)
        NUMBER_OF_TICKETS = 0
        while NUMBER_OF_TICKETS < 2:
            serial_no = ''.join([random.choice(string.digits) for i in range(10)])
            for ticket in all_tickets:
                if serial_no == ticket.serial_no:
                    break
            else:
                ticket = Ticket.objects.create(serial_no=serial_no, date=timezone.now())
                current_student_ticket.ticket.add(ticket)
                NUMBER_OF_TICKETS += 1

    messages.success(request, "Tickets successfully generated")
    return HttpResponseRedirect(reverse('Cafeteria:home'))


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Cafeteria:home'))


def error_400(request, exception):
    return render(request, 'restaurant/error_page.html')


def error_403(request, exception):
    return render(request, 'restaurant/error_page.html')


def error_404(request, exception):
    return render(request, 'restaurant/error_page.html')


def error_500(request):
    return render(request, 'restaurant/error_page.html')
