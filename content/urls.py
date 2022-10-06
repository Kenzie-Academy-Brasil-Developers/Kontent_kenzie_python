from django.urls import path

from .views import Api_Class_View


urlpatterns = [
    path('contents/', Api_Class_View.as_view()),
]