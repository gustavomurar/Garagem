from django.contrib import admin
from django.urls import include, path
from core.models.acessorio import Acessorio
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet
from core.views import AcessorioViewSet, CorViewSet, ModeloViewSet, UserViewSet, VeiculoViewSet

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r"acessorio", AcessorioViewSet, basename='acessorios')
router.register(r"cores", CorViewSet, basename='cores')
router.register(r"modelos", CorViewSet, basename='modelos')


urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
