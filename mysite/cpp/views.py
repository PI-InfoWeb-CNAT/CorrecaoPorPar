from django.shortcuts import render, redirect
from django.views import View
from .services import ServicoResposta, ServicoCorrecao, ServicoTurma
from .services import ServicoCurso, ServicoAvaliacao
from .models import Avaliacao

## Avalia Resposta View
###############################
class AvaliaRespostaView(View):
    def get(self, request, *args, **kwargs):
        srv = ServicoResposta()
        id_resposta = kwargs.get('id_resposta', '')
        obj = srv.recupera_resposta(id_resposta)
        contexto = {'resposta': obj}
        return render(request, 'cpp/avalia_resposta.html', contexto)

    def post(self, request, *args, **kwargs):
        srv = ServicoCorrecao()
        id_resposta = kwargs.get('id_resposta', '')
        #if request.user.is_authenticated and request.user.aluno:
        id_aluno = 1
        nota = request.POST.get('nota','')
        comentario = request.POST.get('comentario', '')
        id_aval = srv.salvar_correcao(id_resposta, id_aluno, nota, comentario)
        return redirect('/avaliacao/{}/'.format(id_aval))

## Nova Avaliação View
##############################
class NovaAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        srv = ServicoTurma()
        id_turma = kwargs.get('id_turma', '')
        turma = srv.get_turma(id_turma)
        contexto = {'turma': turma, "tipos": Avaliacao.TIPO_CORRECAO}
        # TODO: só será exibido o formulário se o professor logado estiver associado à turma
        return render(request, 'cpp/nova_avaliacao.html', contexto)

    def post(self, request, *args, **kwargs):
        srv = ServicoTurma()
        id_turma = kwargs.get('id_turma', '')
        turma = srv.get_turma(id_turma)
        # TODO: confirmar que o professor logado está associado a turma em questão
        if turma:
            titulo = request.POST.get('titulo', '')
            enunciado = request.POST.get('enunciado', '')
            max_nota = request.POST.get('nota', '')
            tipo_correcao = request.POST.get('correcao', '')
            if titulo and enunciado and max_nota and tipo_correcao:
                id_avaliacao = srv.adiciona_avaliacao(
                    turma, titulo, enunciado, max_nota, tipo_correcao
                )
                if id_avaliacao:
                    return redirect('/avaliacao/{}/'.format(id_avaliacao))

## Lister Cursos View
#############################
class ListarCursosView(View):
    # Listar todas as turmas de todas as disciplinas de todos os cursos
    def get(self, request, *args, **kwargs):
        srv = ServicoCurso()
        list_cursos = srv.get_cursos()
        contexto = {'list_cursos': list_cursos}
        return render(request, 'cpp/lista_tudo.html', contexto)

## Avaliação View
##########################
class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        srv = ServicoAvaliacao()
        id_aval = kwargs.get('id','')
        avaliacao = srv.get_avaliacao(id_aval)
        contexto = {'avaliacao': avaliacao}
        return render(request, 'cpp/avaliacao.html', contexto)