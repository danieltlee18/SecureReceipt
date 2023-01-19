from django.urls import path
from .views import receipt_list, receipt_create


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", receipt_create, name="create_receipt")
]
