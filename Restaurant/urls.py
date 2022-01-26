from django.urls import path, include

from Restaurant import views
from rest_framework import routers
from .api_views import StudentAPIView, TicketAPIView, OrderAPIView, FoodAPIView, StudentTicketAPIView

app_name = 'Cafeteria'

router = routers.DefaultRouter()
router.register('student', StudentAPIView)
router.register('food', FoodAPIView)
router.register('ticket', TicketAPIView)
router.register('order', OrderAPIView)
router.register('student-ticket', StudentTicketAPIView)

urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.student_registration, name="student_registration"),
    path('meal', views.meal_menu, name="meal_menu"),
    path('display-ticket', views.display_tickets, name="display_tickets"),
    path('generate-ticket', views.ticket_generator, name="ticket_generator"),
    path('generate-ticket/create', views.create_tickets, name="create_tickets"),
    path('confirm-order', views.confirm_order, name="confirm_order"),
    path('confirm-order/accept/<int:order_id>', views.accept_order, name="accept_order"),
    path('confirm-order/decline/<int:order_id>', views.decline_order, name="decline_order"),
    path('logout', views.log_out, name="logout"),
    path('api', include(router.urls))
]
