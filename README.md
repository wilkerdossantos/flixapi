# FlixAPI

FlixAPI é um backend (API REST) desenvolvido com Django e Django REST Framework para o registro de filmes, gêneros, atores e avaliações.

## Tecnologias Utilizadas

- Python 3.12
- Django
- Django REST Framework (DRF)
- PostgreSQL (ou SQLite para desenvolvimento)
- djangorestframework-simplejwt (Autenticação JWT)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/wilkerdossantos/flixapi.git
cd flixapi
```

### 2. Crie um ambiente virtual e ative-o

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Edite o arquivo `settings.py` para configurar o banco de dados conforme sua necessidade.

Para aplicar as migrações:

```bash
python manage.py migrate
```

### 5. Execute o servidor

```bash
python manage.py runserver
```

A API estará acessível em `http://127.0.0.1:8000/`.

## Endpoints Principais

- `/api/v1/movies/` - Listagem e registro de filmes
- `/api/v1/genres/` - Listagem e registro de gêneros
- `/api/v1/actors/` - Listagem e registro de atores
- `/api/v1/reviews/` - Listagem e registro de avaliações
- `/api/v1/authentication/token/` - Autenticação via JWT

### Exemplo de Uso

**Listar Gêneros:**

```bash
GET /api/v1/genres/
```

## Autenticação e Permissões

A API utiliza autenticação via JWT, gerenciado pelo pacote `djangorestframework-simplejwt`. Os tokens podem ser obtidos pelo endpoint:

```bash
POST /api/v1/authentication/token/
```

Além disso, a API possui controle de permissões, definido no arquivo `flixapi/app/permissions.py`. Esse sistema valida se o usuário tem permissão para acessar determinado recurso, utilizando o próprio sistema de permissões do Django, que pode ser gerenciado pelo Django Admin.

## Testes

Para rodar os testes, utilize o comando:

```bash
python manage.py test
```

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests.

## Autor

[Wilker dos Santos](https://github.com/wilkerdossantos)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

