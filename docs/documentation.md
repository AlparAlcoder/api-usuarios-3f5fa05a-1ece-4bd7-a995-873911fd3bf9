# Documentação da API FastAPI para Usuários

Esta API permite a criação, leitura, atualização e exclusão de usuários. A API é construída usando o FastAPI e usa a biblioteca Pydantic para modelagem de dados.

## Dependências

- FastAPI
- Pydantic
- typing

Para instalar as dependências, você pode usar pip:

```sh
pip install fastapi pydantic
```

## Modelos de dados

### User

Representa um usuário na aplicação. 

- `id` (int, opcional): um identificador único para o usuário. Este campo é gerado automaticamente.
- `name` (str): o nome do usuário.
- `email` (str): o endereço de email do usuário.
- `password` (str): a senha do usuário.

## Endpoints

### POST /users/

Cria um novo usuário.

Parâmetros: 

- `user` (User): um objeto User.

### GET /users/

Retorna uma lista de todos os usuários.

Parâmetros:

Nenhum.

### GET /users/{user_id}

Retorna um usuário específico.

Parâmetros:

- `user_id` (int): o ID do usuário que você deseja recuperar.

### PUT /users/{user_id}

Atualiza um usuário específico.

Parâmetros:

- `user_id` (int): o ID do usuário que você deseja atualizar.
- `user` (User): um objeto User com as novas informações.

### DELETE /users/{user_id}

Exclui um usuário específico.

Parâmetros:

- `user_id` (int): o ID do usuário que você deseja excluir.

## Exemplos de uso

Para criar um usuário, você pode enviar uma solicitação POST para /users/ com um corpo JSON assim:

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secret"
}
```

Para obter todos os usuários, você pode enviar uma solicitação GET para /users/.

Para obter um usuário específico, você pode enviar uma solicitação GET para /users/{user_id}.

Por exemplo, para obter o usuário com o ID 1, você enviaria uma solicitação GET para /users/1.

## Notas importantes

- Todas as solicitações que interagem com um usuário específico (GET, PUT, DELETE) retornarão um erro 404 se o ID do usuário não existir.
- A senha dos usuários é armazenada como texto simples. Isso é apenas para fins de demonstração e não deve ser feito em uma aplicação real.