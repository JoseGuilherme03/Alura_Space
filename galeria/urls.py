from django.urls import path
from galeria.views import index, galeria


urlpatterns = [
        path("", index),
        path("imagem/", galeria)
]