from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
    path('profile/', views.user_profile, name='user_profile'),

]