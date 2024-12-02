from django.urls import path

from gestorProductos.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    ]