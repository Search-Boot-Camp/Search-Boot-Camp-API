"""sbc_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include, re_path 
from django.conf.urls import include
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from BootCamp import views
from BootCamp.views import BootCampListAPI, SearchBootCampAPI, BootCampDetailAPI, OptionBootCampAPI, ImageBootCampAPI ,BootCampUpdate
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0
    
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bootcamp/', BootCampListAPI.as_view()),
    path('api/bootcamp/<int:pk>/', BootCampDetailAPI.as_view()),
    path('api/bootcamp/search', SearchBootCampAPI.as_view()),
    path('api/bootcamp/option/', OptionBootCampAPI.as_view()),
    path('api/bootcamp/image/', ImageBootCampAPI.as_view()),
    path('api/bootcamp/update/', BootCampUpdate),
    path('sentry-debug/', trigger_error),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
