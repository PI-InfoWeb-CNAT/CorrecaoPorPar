from django.shortcuts import render, redirect
from django.views import View
from .models import Resposta, CorrecaoPorPar, Turma, Avaliacao
from django.utils import timezone

class AvaliarRespostaView(View):
    def get(self, request, *args, **kwargs):
        id_resp = kwargs.get('id_resp', '')
        resp = Resposta.objects.get(pk=id_resp)
        contexto = {'resposta': resp}
        return render(request, 'cpp/avalia_resposta.html', contexto)
    
    def post(self, request, *args, **kwargs):
        id_resp = kwargs.get('id_resp', '')
        resp = Resposta.objects.get(pk=id_resp)
        # TODO: alterar para recuperar o id do aluno logado
        id_aluno = 2
        nota = request.POST.get('nota', '')
        comentario = request.POST.get('comentario', '')
        if (resp and id_aluno and nota):
            cpp = CorrecaoPorPar(
                aluno_id=id_aluno, nota=nota, comentarios=comentario 
            )
            cpp.save()
            resp.set_correcao(cpp)
            resp.save()
        return redirect('/avalicao/{}/'.format(resp.avaliacao.id))

## Nova Avaliação View
##############################
class NovaAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        id_turma = kwargs.get('id_turma', '')
        turma = Turma.objects.get(pk=id_turma)
        contexto = {'turma': turma, "tipos": Avaliacao.TIPO_CORRECAO}
        # TODO: só será exibido o formulário se o professor logado estiver associado à turma
        return render(request, 'cpp/nova_avaliacao.html', contexto)

    def post(self, request, *args, **kwargs):
        id_turma = kwargs.get('id_turma', '')
        turma = Turma.objects.get(pk=id_turma)
        # TODO: confirmar que o professor logado está associado a turma em questão
        if turma:
            titulo = request.POST.get('titulo', '')
            enunciado = request.POST.get('enunciado', '')
            max_nota = request.POST.get('nota', '')
            tipo_correcao = request.POST.get('correcao', '')
            agora = timezone.now().date
            if titulo and enunciado and max_nota and tipo_correcao:
                aval = Avaliacao(
                    titulo=titulo, enunciado=enunciado, turma=turma,
                    correcao=tipo_correcao, nota=max_nota, data=agora 
                )
                aval.save()
                return redirect('/avaliacao/{}/'.format(aval.id))