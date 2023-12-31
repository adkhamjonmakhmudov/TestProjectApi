from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Test Project Api",
        default_version='v1',
        description="Backend API for Testing",
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('api/v1/', include('apps.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Include the rest_framework authentication URLs
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
