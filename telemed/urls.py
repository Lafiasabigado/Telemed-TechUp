# routes
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import path, include
from core.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Telemed API",
        default_version='v1',
        description="Documentation de l'API Telemed",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'records', MedicalRecordViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', TemplateView.as_view(template_name='swagger/swagger-ui.html'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),  # routes : /auth/users/, /auth/users/me/
    path('auth/', include('djoser.urls.jwt')),  # routes : /auth/jwt/create/, /auth/jwt/refresh/
]

