# recipebook/urls.py
from django.contrib import admin
from django.urls import include, path
from ledger.views import ledger_homepage

urlpatterns = [
    path('', ledger_homepage, name='home'),
    path('', include('ledger.urls', namespace="ledger")),
    path('admin/', admin.site.urls)
]
