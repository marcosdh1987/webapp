from django.urls import path
from .views import HomeView, dashboardView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', dashboardView.as_view(), name='dashboard'),
]