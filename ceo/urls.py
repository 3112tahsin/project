from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('body.urls')),

    path('admin/', admin.site.urls),

    path(r'jet/', include('jet.urls', 'jet')),
    path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), # Django JET dashboard URLS
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
