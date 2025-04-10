# routes
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import path, include
from core.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'records', MedicalRecordViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),  # routes : /auth/users/, /auth/users/me/
    path('auth/', include('djoser.urls.jwt')),  # routes : /auth/jwt/create/, /auth/jwt/refresh/
]

