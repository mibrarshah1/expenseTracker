from django.contrib import admin
from django.urls import path, include
from expenses import views as expense_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("expenses.urls")),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # login/logout/password management
    path("accounts/register/", expense_views.register, name="register"),
]
