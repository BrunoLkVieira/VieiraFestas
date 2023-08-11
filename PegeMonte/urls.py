from django.urls import path
from .views import Homepage, Detalhestema, Pesquisa

urlpatterns =[
    path("", Homepage.as_view()),
    path("<int:pk>", Detalhestema.as_view(), name="detalhestema"),
    path("pesquisa/", Pesquisa.as_view(), name="pesquisa"),
]
