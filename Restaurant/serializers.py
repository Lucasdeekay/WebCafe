from rest_framework import serializers

from Restaurant.models import Order, Ticket, Food, Student, StudentTicket


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        field = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        field = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = '__all__'


class StudentTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTicket
        field = '__all__'