```
Nome: Rafael Carvalho Junior Araújo
Matrícula: 222021817
```
# Projeto 3
![Ludo](https://www.toy-factory.ca/wp-content/uploads/600-LUDO-GOKI-2-56914.jpg)
## Introdução
O terceiro projeto tem como meta a elaboração de um planejamento detalhado para a implementação de um jogo, empregando a linguagem de modelagem UML como ferramenta principal. Optou-se por criar uma versão alternativa do clássico jogo ``Ludo``, limitada a apenas dois jogadores para simplificar o desenvolvimento. Ao longo do projeto, foi necessário criar diagramas de classes, diagramas de caso de uso e, quando apropriado, diagramas de fluxo de dados, a fim de visualizar e estruturar eficazmente os componentes do jogo.

## Classes
Ao planejar meu projeto eu notei que ele tinha aspectos de uma arquitetura MVC, onde existem algumas Classes Modelos como ``Player`` ou ``Pawn``, Classes Controladoras como o ``Universe``, e Classes Visualizadoras como o ``Board``. Assim, foi separado em sete Classes onde será desenvolvida toda a lógica do jogo.
- Player
- Pawn
- Dice
- Universe
- Board
- Menu
- DataBase


### Player
A Classe Player traz informações sobre o Jogador, tais como seus Peões, seu score, nickname e cor, e também mais algumas funções para manipular suas informações.

### Pawn
Está é uma Classe simples que apenas armazena a posição do Peão para ser utilizado por algumas outras entidades. Criei esta Classe ela pode facilitar a adição de novos atributos ao Peão.

### Dice
Está é a Classe responsável por simular um Dado de seis faces.

### Universe
Uma Classe Controladora que manipula tudo que ocorre dentro do jogo, desde Menus até a chamada de operações do Banco de Dados.

### Board
View responsável por imprimir o tabuleiro e todas as informações dele.

### Menu
Manipula as telas do Menu até começar uma partida nova.

## Conclusão
Neste projeto, a modelagem do jogo Ludo utilizando UML permitiu a criação de uma estrutura clara e organizada, com classes bem definidas para representar as diferentes partes do jogo. A abordagem MVC facilitou a separação de responsabilidades e a compreensão do sistema. Essa modelagem serve como uma base sólida para o desenvolvimento futuro do jogo, adicionando funcionalidades e refinamentos, tornando-o jogável. O projeto demonstrou a importância da modelagem e design orientado a objetos na criação de sistemas complexos de forma estruturada e eficiente compreensão do sistema. Essa modelagem serve como uma base sólida para o desenvolvimento futuro do jogo, adicionando funcionalidades e refinamentos, tornando-o jogável.