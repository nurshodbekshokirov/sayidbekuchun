
from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Sayidbek API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Nurshodbek SHokirov, <nurshodbekshokirov@gmail.com>"),

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register("profillar",ProfilViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0))

]
