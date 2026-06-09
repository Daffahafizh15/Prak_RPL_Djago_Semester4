from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/mahasiswa/')),
    path('admin/', admin.site.urls),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('akun/', include('akun.urls')),
]