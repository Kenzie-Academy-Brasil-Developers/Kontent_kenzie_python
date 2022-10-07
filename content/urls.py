from django.urls import path

from .views import Api_Class_View, Api_Class_View_by_id,Api_Class_View_by_title


urlpatterns = [
    path('contents/', Api_Class_View.as_view()),
    path('contents/<content_id>', Api_Class_View_by_id.as_view()),
    path('contents/filter/', Api_Class_View_by_title.as_view()),
]