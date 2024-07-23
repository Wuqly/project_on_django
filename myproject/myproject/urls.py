from django.contrib import admin
from django.urls import path, include
from jewelry import views
from jewelry.views import page_not_found
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jewelry.urls')),
    path('users/', include('users.urls'), namespace='users'),
    
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found