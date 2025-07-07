# Documenta��o da API FastAPI para Usu�rios

Esta API permite a cria��o, leitura, atualiza��o e exclus�o de usu�rios. A API � constru�da usando o FastAPI e usa a biblioteca Pydantic para modelagem de dados.

## Depend�ncias

- FastAPI
- Pydantic
- typing

Para instalar as depend�ncias, voc� pode usar pip:

```sh
pip install fastapi pydantic
```

## Modelos de dados

### User

Representa um usu�rio na aplica��o. 

- `id` (int, opcional): um identificador �nico para o usu�rio. Este campo � gerado automaticamente.
- `name` (str): o nome do usu�rio.
- `email` (str): o endere�o de email do usu�rio.
- `password` (str): a senha do usu�rio.

## Endpoints

### POST /users/

Cria um novo usu�rio.

Par�metros: 

- `user` (User): um objeto User.

### GET /users/

Retorna uma lista de todos os usu�rios.

Par�metros:

Nenhum.

### GET /users/{user_id}

Retorna um usu�rio espec�fico.

Par�metros:

- `user_id` (int): o ID do usu�rio que voc� deseja recuperar.

### PUT /users/{user_id}

Atualiza um usu�rio espec�fico.

Par�metros:

- `user_id` (int): o ID do usu�rio que voc� deseja atualizar.
- `user` (User): um objeto User com as novas informa��es.

### DELETE /users/{user_id}

Exclui um usu�rio espec�fico.

Par�metros:

- `user_id` (int): o ID do usu�rio que voc� deseja excluir.

## Exemplos de uso

Para criar um usu�rio, voc� pode enviar uma solicita��o POST para /users/ com um corpo JSON assim:

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secret"
}
```

Para obter todos os usu�rios, voc� pode enviar uma solicita��o GET para /users/.

Para obter um usu�rio espec�fico, voc� pode enviar uma solicita��o GET para /users/{user_id}.

Por exemplo, para obter o usu�rio com o ID 1, voc� enviaria uma solicita��o GET para /users/1.

## Notas importantes

- Todas as solicita��es que interagem com um usu�rio espec�fico (GET, PUT, DELETE) retornar�o um erro 404 se o ID do usu�rio n�o existir.
- A senha dos usu�rios � armazenada como texto simples. Isso � apenas para fins de demonstra��o e n�o deve ser feito em uma aplica��o real.