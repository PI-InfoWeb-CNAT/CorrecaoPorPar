from django.shortcuts import render, redirect
from django.views import View
from .models import Resposta, CorrecaoPorPar

class AvaliarRespostaView(View):
    def get(self, request, *args, **kwargs):
        id_resp = kwargs.get('id_resp', '')
        resp = Resposta.objects.get(pk = id_resp)
        contexto = {'resposta': resp}
        return render(
            request, 'cpp/avalia_resposta.html', contexto
        )
    def post(self, request, *args, **kwargs):
        id_resp = kwargs.get('id_resp', '')
        resp = Resposta.objects.get(pk = id_resp)
        # TODO: substituir pelo id do aluno logado
        id_aluno = 2
        nota = request.POST.get('nota', '')
        comentarios = request.POST.get('comentarios', '')
        if (resp and id_aluno and nota):
            cpp = CorrecaoPorPar(aluno_id=id_aluno, nota=nota, comentarios=comentarios)
            cpp.save()
            resp.set_correcao(cpp)
            resp.save()
        return redirect('/avaliacao/{}/'.format(resp.avaliacao.id))