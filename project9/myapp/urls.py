from django.urls import path

from . import views

urlpatterns = [
    path('menu_card/', views.menu_by_id),
]
