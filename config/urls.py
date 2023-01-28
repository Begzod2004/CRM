from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Omax API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
       # token
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('admin/', admin.site.urls, name='admin'),
   path('api/', include('app.urls')),
   path('swagger/', schema_view),

   path('super_admin/', include('super_admin.urls'))
   
]