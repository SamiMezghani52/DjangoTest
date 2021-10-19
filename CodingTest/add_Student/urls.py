from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayClasses,name='classes-list'),
    path('add/', views.addLine,name="add"),

    path('ajax/levels/', views.load_levels, name="ajax-load-levels"),
    path('ajax/classes/', views.load_classes, name="ajax-load-classes")
]