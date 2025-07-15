# CDU004. Abrir sessão de avaliação 

- **Ator principal**: Professor
- **Atores secundários**: não possui 
- **Resumo**: Um professor a partir da página referente a uma turma de uma dada disciplina clica em um botão para criar avaliação. Preenche um formulário com as informações da avaliação e ao final visualiza a página da avaliação, a qual conterá um botão para o estágio seguinte - abrir a janela de submissão.
- **Pré-condição**:
  - Professor devidamente associado a turma em questão;
  - Professor devidamente logado no sistema.
- **Pós-Condição**:
  - Avaliação cadastrada com sucesso e apta a ser visualizada pelos alunos.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - Um professor de uma dada turma, a partir da página da turma, clica em um botão para criar uma avaliação ("/turma/<int:id>/nova-avaliacao/"). | |  
| | 1 - O sistema exibe um formulário para o cadastramento de uma nova avaliação, contendo os campos: enunciado, nota, tipo de correção (pelo professor ou pelos pares). |
| 2 - O professor preenche e submete o formulário. | |
| | 3 - Após a validação dos dados é criada e persistida a nova avaliação, na sequência é apresentada a página da avaliação que acabou de ser criada. Também é apresentada uma mensagem confirmando o sucesso na criação da avaliação. | 

## Fluxo Alternativo I - URL acessada por um professor não vinculado à turma
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 1.1 - O sistema exibe uma página de erro informando que apenas o professor vinculado à turma é quem pode cadastrar avaliações para a turma. |

## Fluxo Alternativo II - Campos inválidos ou omitidos no formulário de criação de avaliação
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 3.1 - O sistema retorna ao formulário de cadastramento de avaliação (passo 1 do fluxo principal), incluindo uma mensagem informando que campos necessários foram informados erradamente ou omitidos no preenchimento. |

## Fluxo Alternativo III - Algum problema impediu o salvamento da nova avaliação
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 3.2 - O sistema exibe uma página de erro informando que houve um problema que impediu o salvamento da avaliação e pede que o professor tente novamente posteriormente. |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...