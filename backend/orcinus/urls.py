from django.urls import path

from . import views

urlpatterns = [
    path('Letter/', views.LetterView.as_view()),
    path('Sailor/', views.SailorView.as_view()),
    path('Orcinus/', (views.Orcinus.as_view())),
]
