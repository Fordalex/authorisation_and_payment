from django.conf.urls import url, include
from .views import premium

urlpatterns = [
    url(r'^', premium, name="premium")
]