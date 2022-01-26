from rest_framework import viewsets

from Restaurant.models import Student, Food, Ticket, Order, StudentTicket
from Restaurant.serializers import StudentSerializer, FoodSerializer, TicketSerializer, OrderSerializer, \
    StudentTicketSerializer


class StudentAPIView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class FoodAPIView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class TicketAPIView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class OrderAPIView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class StudentTicketAPIView(viewsets.ModelViewSet):
    serializer_class = StudentTicketSerializer
    queryset = StudentTicket.objects.all()