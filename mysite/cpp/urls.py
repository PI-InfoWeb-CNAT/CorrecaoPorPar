from django.urls import path
from . import views

app_name = 'cpp'
urlpatterns = [
    path(
        'avaliacao/<int:id>/',
        views.AvaliacaoView.as_view(), name='avaliacao'
    ),
    path(
        'resposta/<int:id_resposta>/avalia/', 
        views.AvaliaRespostaView.as_view(), name='avalia'
    ),
    path(
        'turma/<int:id_turma>/nova-avaliacao/',
        views.NovaAvaliacaoView.as_view(), name='nova-avaliacao'
    ),
    path(
        '', # INICIALMENTE a página inicial será a listagem geral 
        views.ListarCursosView.as_view(), name='lista-tudo'
    ),
]