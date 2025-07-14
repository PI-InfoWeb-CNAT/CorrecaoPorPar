from django.db import models
from django.contrib.auth.models import User

## Classe Curso
##########################
class Curso(models.Model):
    NIVEL = [
        (1, "Técnico"),
        (2, "Superior de Tecnologia"),
        (3, "Engenharia")
    ]
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=100)
    nivel = models.IntegerField(choices=NIVEL, default=1)
    def __str__(self):
        return self.nome

## Classe Disciplina
###############################
class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

## Classe Professor
#############################
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

## Classe Aluno
##########################
class Aluno(models.Model):
    matricula = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.matricula

## Classe Turma
##########################
class Turma(models.Model):
    nome = models.CharField(max_length=30)
    ativa = models.BooleanField(default=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)
    def __str__(self):
        return self.nome

## Classe Avaliação
##############################
class Avaliacao(models.Model):
    ESTAGIO = [
        (1, "Criada"),
        (2, "Em submissão"),
        (3, "Em correção"),
        (4, "Finalizada"),
    ]
    TIPO_CORRECAO = [
        (1, "Pelo professor"),
        (2, "Pelos pares"),
    ]
    titulo = models.CharField(max_length=30)
    enunciado = models.CharField(max_length=300)
    nota = models.IntegerField(default=100)
    data = models.DateField(auto_now_add=True)
    estagio = models.IntegerField(choices=ESTAGIO, default=1)
    correcao = models.IntegerField(choices=TIPO_CORRECAO, default=2)
    turma = models.ForeignKey(Turma,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

## Classe Correção
#############################
class Correcao(models.Model):
    nota = models.IntegerField()
    comentarios = models.CharField(max_length=200)
    def __str__(self):
        return "Correcao ({})".format(self.id)

## Classe Correção Por Par
###############################
class CorrecaoPorPar(Correcao):
    aluno = models.ForeignKey(Aluno, models.CASCADE)
    def __str__(self):
        return "Correcao por par ({})".format(self.id)

## Classe Professor
#############################
class Resposta(models.Model):
    submissao = models.DateTimeField(auto_now_add=True)
    diagrama = models.ImageField(upload_to='respostas')
    observacao = models.CharField(max_length=200)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    correcao = models.OneToOneField(
        Correcao, on_delete=models.CASCADE,
        null = True, blank = True
    )
    def __str__(self):
        return "Resposta ({})".format(self.id)
    def set_correcao(self, obj_correcao):
        self.correcao = obj_correcao
