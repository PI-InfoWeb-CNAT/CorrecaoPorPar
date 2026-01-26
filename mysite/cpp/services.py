from django.utils import timezone
from .models import Resposta, CorrecaoPorPar, Turma, Avaliacao, Curso

## Serviço Resposta
########################
class ServicoResposta():
    def recupera_resposta(self, id_resposta):
        obj = Resposta.objects.get(pk = id_resposta)
        return obj
    
## Serviço Correção
########################
class ServicoCorrecao():
    def salvar_correcao(self, id_resp, id_aluno, nota, comentario):
        srv = ServicoResposta()
        resp = srv.recupera_resposta(id_resp)
        if (resp and nota):
            novo = CorrecaoPorPar(
                aluno_id=id_aluno, nota=nota, comentarios=comentario
            )
            novo.save()
            resp.set_correcao(novo)
            resp.save()
        return resp.avaliacao.id

## Serviço Turma
#####################
class ServicoTurma():
    def get_turma(self, id_turma):
        turma = Turma.objects.get(pk = id_turma)
        return turma
    def adiciona_avaliacao(self, turma, titulo, enunciado, max_nota, tipo_correcao):
        # Fluxo principal: é presumido que o professor logado seja o responsável
        # pela turma em questão
        agora = timezone.now().date
        aval = Avaliacao(
            titulo=titulo, enunciado=enunciado, correcao=tipo_correcao, 
            nota=max_nota, turma=turma, data=agora, 
        )
        aval.save()
        return aval.id
    
## Serviço Curso
#####################
class ServicoCurso():
    def get_cursos(self):
        return Curso.objects.all()
    

## Serviço Avaliação
#########################
class ServicoAvaliacao():
    def get_avaliacao(self, id_avaliacao):
        return Avaliacao.objects.get(pk = id_avaliacao)