from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('mentorados/', include('mentorados.urls')),
    path('', RedirectView.as_view(url='/mentorados/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "mentorados.views.not_found"