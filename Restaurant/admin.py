from django.contrib import admin

from Restaurant.models import Student, Food, Ticket, Order, StudentTicket


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'sex', 'department')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'date')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('serial_no', 'date', 'is_valid')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('student', 'food', 'ticket', 'quantity', 'date')


class StudentTicketAdmin(admin.ModelAdmin):
    list_display = ('student',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(StudentTicket, StudentTicketAdmin)