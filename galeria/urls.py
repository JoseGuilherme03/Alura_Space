from django.urls import path
from galeria.views import buscar, index, galeria


urlpatterns = [
    path("", index, name="index"),
    path("imagem/<int:foto_id>", galeria, name="imagem"),
    path("buscar", buscar, name="buscar")
]
