from django.urls import path
from .views import Email, Key

app_name = "authentication"

urlpatterns = [
    path('auth/', Email.as_view()),
    path('key/', Key.as_view()), 
]
