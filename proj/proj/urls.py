from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('hermes_admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
]
handler404 = 'core.views.page_not_found'
handler403 = 'core.views.csrf_failure'