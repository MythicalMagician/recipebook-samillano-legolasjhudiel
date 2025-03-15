# recipebook/urls.py
from django.contrib import admin
from django.urls import include, path

from ledger.views import redirect_homepage


urlpatterns = [
    path('', redirect_homepage, name='home'),
    path('', include('ledger.urls', namespace="ledger")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]
