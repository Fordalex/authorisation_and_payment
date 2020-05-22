from django.conf.urls import url
from .views import add_item, input_item

urlpatterns = [
    url(r'^add_item$', add_item, name="add_item"),
    url(r'^input_item$', input_item, name="input_item")
]