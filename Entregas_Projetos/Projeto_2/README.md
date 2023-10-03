```
Nome: Rafael Carvalho Junior Araújo
Matrícula: 222021817
```
# Projeto 2

### Introdução
O segundo projeto tinha como objetivo aprofundar o conhecimento em Orientação a Objetos e Python. Na atividade foi solicitada a implementação do pseudocódigo do Projeto 1 na linguagem Python, mas como eu já o havia implementado, decidi criar uma API e um ambiente de teste para verificar a funcionalidade do meu Projeto 1

### Melhorias
Na nossa biblioteca spaceShapes foram adicionados os métodos
```python
update()
getType()
getKey()
```

- O método ``update()`` tem como objetivo atualizar os dados dos Objetos.
- O método ``getType()`` tem como objetivo devolver o tipo do objeto, que será utilizado mais na frente para a manipulação da nossa API.
- E por último, o identificador dos nossos objetos, o ``getKey()``, que tem como objetivo fornecer uma chave única para os nossos objetos poderem ser manipulados por requisições HTTP.

### Cartesian Board
A biblioteca do ``CartesianBoard`` é responsável por gerar nosso conjunto de formas. Nele é possível gerar novas formas, atualizar, deletar e gerar uma lista de todas elas.

Esta biblioteca é fundamental para o funcionamento da nossa API, pois é com ela que nós manipulamos tudo.

### API de armazenamento e manipulação de formas
Aqui nós temos uma API simples, um ``CRUD``, que tem como objetivo criar um objeto do tipo ``CartesianBoard``, e adicionar as formas do Projeto 1 via requisições HTTP.

Foi utilizado o framework ``FastAPI`` junto com o ``Uvicorn`` para testar a aplicação. Para instalá-los basta executar o comando:

```bash
$pip install "fastapi[all]"
```

Para testar os métodos da API, foi utilizado o aplicativo ``Postman``, que facilita os testes durante o desenvolvimento da API.

Os endpoints foram configurados da seguinte forma:

#### Create
```
http://xxx.xxx.xxx.x/shapes/add/{shape_type}
```

Onde o shape_type é do tipo string e pode receber os seguintes valroes: ``Ponto, Triangulo, Quadrado, Circulo e Reta``.<br>
Embora no link só tenha uma entrada, shape_type, é importante resaltar que essa entrada deve ser acompanhada com um arquivo JSON com as configurações do Objeto. Por exemplo na criação de um objeto do tipo ponto na origem:

```json
{
    "x" : 0,
    "y" : 0
}
```
Para a criação de um objeto do tipo Círculo:
```json
{
    "p" : [0, 0],
    "raio" : 10
}
```

#### Read
Para a leitura dos Objetos, basta acessar:
```
http://xxx.xxx.xxx.x/shapes/
```

Que será devolvida uma lista JSON com os dados de todos os objetos do CartesianSpace.
#### Update
A atualização funciona de forma parecida com a criação, é preciso anexar um JSON à requisição com os dados que queremos mudar, mas para isso precisaremos da chave do nosso objeto, que obtemos na requisição de leitura acima. Para alterar os dados de um objeto, basta acessar:
```
http://xxx.xxx.xxx.x/shapes/update/{shape_key}
```

Com o seguinte anexo para mudar o raio

```json
{
    "raio" : 99
}
```

#### Delete
Para deletar é simples, basta fazer a requisição
```
http://xxx.xxx.xxx.x/shapes/del/{shape_key}
```

com a key do objeto para ele ser deletado do nosso CartesianSpace.

### Conclusão

Com este projeto eu consegui aprofundar meus conhecimentos na utilizando os quatro pilares da Orientação a Obejtos, aonde foi claro a aplicação. Também pude estudar um pouco sobre desenvolvimento de API's utilizando o framework ``fastAPI``.