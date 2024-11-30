from django.contrib import admin
from .models import Customer, ServiceRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number')
    search_fields = ('user__username', 'account_number')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('request_type', 'status')
    search_fields = ('customer__user__username', 'customer__account_number', 'description')
    readonly_fields = ('created_at', 'updated_at')