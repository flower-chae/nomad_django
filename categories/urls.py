from django.urls import path
from . import views


urlpatterns = [
    path("", views.Categories.as_view()),
    path("<int:pk>",views.CategoryDetail.as_view()),
]

# 생각
# GET POST /categories
# GET PUT DELETE /categories/1