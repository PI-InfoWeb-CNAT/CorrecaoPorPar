from django.urls import path
from . import views

app_name = 'cpp'
urlpatterns = [
    path(
        'resposta/<int:id_resp>/avaliar/',
        views.AvaliarRespostaView.as_view(),
        name = 'avaliar'
    ),
    path(
        'turma/<int:id_turma>/nova-avaliacao/',
        views.NovaAvaliacaoView.as_view(), name='nova-avaliacao'
    ),
]