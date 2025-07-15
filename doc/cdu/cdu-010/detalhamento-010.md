# CDU010. Submeter diagrama 

- **Ator principal**: Aluno
- **Atores secundários**: não possui	 
- **Resumo**: Um aluno estando acessando a página de uma avaliação, percebe que foi exebido um formulário para submissão de um diagrama contendo uma resposta válida para o enunciado da avaliação. Após a submissão ele continua na página da avaliação, onde é exibida uma mensagem de sucesso na submissão, na qual ele irá aguardar a próxima etapa da avaliação.
- **Pré-condição**:
  - Aluno vinculado a turma específica para qual foi postada a avaliação;
  - Aluno devidamente logado no sistema;
  - Aluno estar com a página da avaliação aberta;
  - A página da avaliação necessitará ficar sendo recarregada de 10 em 10 segundos.
- **Pós-Condição**:
  - Resposta do aluno (logado) devidamente persistida.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 0 - Estando com a página da avaliação em aberto, (após um dado recarregamento) é exibido um formulário que permitirá ao aluno submeter um diagrama em resposta ao enunciado da avaliação, além de algum comentário opcional que deseje fazer. |  
| 1 - O aluno seleciona o arquivo contendo a sua resposta e registra algum comentário, se desejar, e submete a sua resposta. | |
| | 2 - O sistema retorna à página da avaliação, com a indicação que a resposta já foi enviada pelo aluno em questão e que este deve aguardar a próxima etapa da avaliação, que será aberta pelo professor. |

## Fluxo Alternativo I - Formulário de resposta com dados inválidos ou omitidos
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: |   
| | 2.1 - O sistema retorna a exibir a página da avaliação com o formulário para a resposta (retornando ao passo 0 do fluxo principal), incluindo uma mensagem indicando a inclusão de respostas inválidas ou omitidas. |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...