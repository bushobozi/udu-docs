from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from blog import views  # Ensure views are imported correctly

# Swagger API Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="UDU Docs API",
        default_version='v1',
        description="API documentation for Uganda Democratic Union",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bushobozibushivan@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Router for ViewSets (Ensure UserViewSet & GroupViewSet exist in views.py)
router = routers.DefaultRouter()
# Uncomment these lines if UserViewSet and GroupViewSet exist in `views.py`
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # Swagger and ReDoc URLs
    path('swagger.<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Django Admin URL
    path('admin/', admin.site.urls),

    # API Endpoints
    path('', include(router.urls)),  # Only include if router has registered views
    path('udu/api/v1/', include('blog.urls')),

    # DRF Authentication URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
