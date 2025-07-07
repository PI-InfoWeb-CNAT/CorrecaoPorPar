# CDU011. Avaliar trabalho de colega 

- **Ator principal**: Aluno (avaliador)
- **Atores secundários**: (nenhum)
- **Resumo**: Um aluno recebe a incumbência de avaliar o diagrama de um colega, para o qual irá atribuir uma nota e um comentário (opcional).
- **Pré-condição**: 
  - aluno (avaliador) logado no sistema;
  - trabalho enviado corretamente na janela de submissão;
  - jenala de correção aberta pelo professor.
- **Pós-Condição**: 
  - correção do trabalho submetida e persitida. 

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - Aluno é convidado a avaliar o trabalho de um colega e clicar em um link | |  
| 1 - Aluno clica no link para avaliar trabalho |  |
|  | 2 - Sistema exibe o diagrama a ser avaliado e um formulário contendo nota e comentário |
| 3 - Avaliador preenche o formulário e envia a avaliação |  |
|  | 4 - Sistema informa que a avaliação foi registrada com sucesso ao retornar para a página inicial da avaliação |

## Fluxo Alternativo I - Avaliador não informa a nota
| Ações do ator | Ações do sistema |
| :-----------: |:---------------: | 
|  | 4.1 - Sistema informa que a nota é inválida e exibe novamente a tela de submissão de correção (retorna ao passo 2 do fluxo principal) |

## Fluxo Alternativo II - Avaliador informa nota negativa ou maior que 100
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 4.2 - Sistema informa que a nota precisar estar entre 0 e 100 e exibe novamente a tela de submissão de correção (retorna ao passo 2 do fluxo principal) |  

## Diagrama de Interação (Sequência)

### DSS

![Diagrama de Sequência do Sistema](./DSS.png)

### Sequência - Etapa 1

![Etapa 1 do diagrama de sequência](./etapa%201.png)

### Sequência - Etapa 2

![Etapa 2 do diagra de sequência](./etapa%202.png)

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...