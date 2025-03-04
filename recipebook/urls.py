# recipebook/urls.py
from django.contrib import admin
from django.urls import include, path

from ledger.views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', include('ledger.urls', namespace="ledger")),
    path('admin/', admin.site.urls)
]
