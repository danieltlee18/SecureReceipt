from django.urls import path
from .views import receipt_list, receipt_create, category_list, account_list, create_category


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", receipt_create, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
    path("categories/create/", create_category, name="create_category")
]
