from django.urls import path
from . import views

app_name = 'cpp'
urlpatterns = [
    path(
        'resposta/<int:id_resp>/avaliacao/',
        views.AvaliarRespostaView.as_view(),
        name='avaliacao'
    ),
]