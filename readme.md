# Kanvas

Descrição: Uma inspirada no sistema canvas de controle de atividades Canvas utilizado na Kenzie Academy. Podemos criar usuário com até 3 perfis, Estudante, Facilitador e Instrutor com permissões diferentes.
Criar cursos e matricular estudantes, que podem submeter tarefas e terem essas avaliadas por supervisores.

## Como Rodar?

### Linguagens necessárias:
- Tenha o Python instalado na sua máquina
- O banco de dados utilizado é o sqlite3, já instalado pelo django, não se preocupe com isso

###  Instalando
1 - Após baixar esta aplicação usando o GIT CLONE do seguinte repositrório:

$ git clone https://gitlab.com/brunovcg/q4-s1-e2-kanvas

2 - Entre na pasta:

$ cd /Q4-S1-E1\ /-\ /Kanvas

3 - Inicie um ambiente virtual com o comando no terminal:

$ python -m venv venv

4 - Inicialize o ambiente virtual

$ source venv/bin/activate

5 - Instale as dependências do projeto com o comando:

$ pip install -r requirements.txt

(esse comando instalará o django e o djangorestframework)

6 - Rodar as migrations:

$ ./manage.py makemigrations

7 - Inicialize o servidor:

$ python manage.py runserver


## Erros e exceções:
Essa aplicação trata os erros permissão e autenticação, cursos e atividades com o mesmo nome, busca de usuarios, cursos, atividades ou submissões que não existem.

## Permissões

Quando faltar um token o seguinte erro é mostrado

```json
{
    "detail": "Invalid token."
}

```

Quando existe um token mas este não é de um dos tipos permitidos:

```json
{
    "detail": "You do not have permission to perform this action."
}

```

## Utilização das Rotas

### POST /api/accounts/ - Criar Usuaários

Permissão: Qualquer request, não necessita de token

os campos is_staff e is_superuser definem as permissões:

Estudante: is_staff = False and is_superuser = False
Facilitador: is_staff = True and is_superuser = False
Instrutor: is_staff = True and is_superuser = True

#### exemplo Request

```json
{
    "username": "student",
    "password": "1234",
    "is_superuser": false,
    "is_staff": false
}
```

#### Response

##### STATUS 201_CREATED

```json
{
    "id": 1,
    "username": "student",
    "is_superuser": false,
    "is_staff": false
}
```

##### STATUS 409_CONFLICT

```json
{"user already exists"}
```

### POST /api/login/ - fazendo login

Permissão: Qualquer request, não necessita de token

#### exemplo Request
```json
{
    "username": "student",
    "password": "1234",
}
```

#### Reponse

##### STATUS 200_OK

```json
{
    "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

Esse token deve ser usado nas rotas que pedem autenticação e permissão, da seguinte maneira:

No HEADER da requisição:
```
     KEY                        Value
Content-Type                application/json     
Authorization           Token <digite_o_token>
```

### POST /api/courses/ - criando um curso:
Permissão: Instrutor

#### exemplo Request
```json
{
    "name": "Node"
}
```

#### Response

##### 201_CREATED

```json
{
    "id": 1,
    "name": "Node",
    "users": []
}
```
##### 404_BAD_REQUEST

Se o nome do curso já existir

```json
{"error': 'Course with this name already exists"}
```

### PUT /api/courses/<int:course_id>/ - Atualizando o nome do curso

Permissão: Instrutor

#### exemplo Request
```json
{
    "name": "Node2"
}
```

#### Response

##### 200_OK

```json
{
    "id": 1,
    "name": "Node2",
    "users": []
}
```
##### 404_BAD_REQUEST

Se o curso não existir

```json
{"error": "invalid course_id"}
```
##### 409_Conflict

Se o nome do curso já existir

```json
{"error": "Course with this name already exists"}
```


### PUT /api/courses/<int:course_id>/registrations/- atualizando a lista de estudantes matriculados em um curso

Esse endpoint vai receber "user_ids" que vai atualizar a lista corrente de alunos, ATENÇÃO, não é adicionado, mas a lista de alunos do curso passa a ser exatamente a lista passada, sobrescrevendo o que havia antes. Só usuários com ID de estudante podem ser matriculados

Permissão: Instrutor

#### Exemplo Request

```json
{
    "user_ids": [3, 4, 5]
}
```

#### Response

##### 200_OK

```json
{
    "id": 1,
    "name": "Node",
    "users": [
        {
        "id": 3,
        "username": "student1"
        },
        {
        "id": 4,
        "username": "student2"
        },
        {
        "id": 5,
        "username": "student3"
        }
    ]
}
```

##### 400_BAD_REQUEST

Quando algum usuário não for aluno:

```json
{
    "errors": "Only students can be enrolled in the course."
}
```

##### 404_NOT_FOUND

Quando o curso não existir na base:

```json
{
    "errors": "invalid course_id"
}
```

Quando algum aluno não existir na base:

```json
{
    "errors": "invalid user_id list"
}
```

### GET /api/courses/ - obtendo a lista de cursos e alunos

Permissão: Qualquer request, não necessita de token

#### Exemplo request

Não possui body

#### Response

##### 200_OK
```json
[
    {
        "id": 1,
        "name": "Node",
        "users": [
            {
                "id": 3,
                "username": "student1"
            }
        ]
    },
    {
        "id": 2,
        "name": "Django",
        "users": []
    },
    {
        "id": 3,
        "name": "React",
        "users": []
    }
]
```

### GET /api/courses/<int:course_id>/ - filtrando a lista de cursos por um id

Permissão: Qualquer request, não necessita de token

#### Exemplo Request

Não tem body

GET /api/courses/1/ - endpoint exemplo

#### response

##### 200_OK

```json
{
    "id": 1,
    "name": "Node",
    "users": [
        {
            "id": 3,
            "username": "student1"
        }
    ]
}
```

##### 404_NO_FOUND

Caso não haja courso com o ID no banco de

```json
{
    "errors": "invalid course_id"
}
```

### DELETE /api/courses/<int:course_id>/ - deletar cursos

Permissão: Instrutor

#### exemplo Request

Não possui body

Endpoin EXEMPLO: DELETE /api/courses/1/ 

#### Response

##### 209 NO_CONTENT

Sem contrúdo

##### 404 NOT_FOUND

Caso não haja courso com o ID no banco de

```json
{
    "errors": "invalid course_id"
}
```

### POST /api/activities/ - criando uma atividade`

Permissão: Instrutor

#### Exemplo Request

```json
{
    "title": "Kenzie Pet",
    "points": 10
}
```


#### response

##### 201_CREATED
```json
{
    "id": 1,
    "title": "Kenzie Pet",
    "points": 10,
    "submissions": []
}
```

##### 400_BAD_REQUEST

```json
{"error": "Activity with this name already exists"}

```

### GET /api/activities/ - listando atividades

Permissão: Instrutor ou Facilitador

#### Exemplo request

Sem Body

#### response

##### 200_OK

```json
[
    {
        "id": 1,
        "title": "Kenzie Pet",
        "points": 10,
        "submissions": [
            {
                "id": 1,
                "grade": 10,
                "repo": "http://gitlab.com/kenzie_pet",
                "user_id": 3,
                "activity_id": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "Kanvas",
        "points": 10,
        "submissions": [
            {
                "id": 2,
                "grade": 8,
                "repo": "http://gitlab.com/kanvas",
                "user_id": 4,
                "activity_id": 2
            }
        ]
    },
 
]
```

### PUT /api/activities/<int:activity_id>/ - atualizando uma atividade

Permissão: Instrutor ou Facilitador

### Exemplo request

```json
{
    "title": "Kenzie Pet2",
    "points": 11
}
```

#### response

##### 201_CREATED
```json
{
    "id": 1,
    "title": "Kenzie Pet2",
    "points": 11,
    "submissions": []
}
```

##### 400_BAD_REQUEST

```json
{"error": "Activity with this name already exists"}

```

### POST /api/activities/<int:activity_id>/submissions/ - fazendo submissão de uma atividade

Permissão: Estudante

#### Exemplo de request

```json
{
    "grade": 10,
    "repo": "http://gitlab.com/kenzie_pet"
}
```

obs: a grade sempre será criada como null pois não é o estudante que faz a avaliaão da nota.

#### Response

##### 201_CREATED


```json
{
    "id": 7,
    "grade": null,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
}
```

### PUT /api/submissions/<int:submission_id>/ - editando a nota de uma submissão 

Permissão: Facilitador ou Instrutor

#### exemplo Request

```json
{
    "grade": 10
}
```
#### reponse

##### 200_OK

```json
{
    "id": 3,
    "grade": 10,
    "repo": "http://gitlab.com/kenzie_pet",
    "user_id": 3,
    "activity_id": 1
}
```

### GET /api/submissions/ - listando submissões

Permissões - Estar logado

Esse endpoint terá a resposta de acordo com o token de que tipo de usuário está logado.

Caso seja Estudante, somente suas submissões serão exibidas, se for facilitador ou instrutor, todas serão.

#### Exmeplo Request

Sem corpo



#### Response

sendo o estudante 4 por exemplo:

##### 200_OK
```json
[
    {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
    },
    {
        "id": 5,
        "grade": null,
        "repo": "http://gitlab.com/kmdb2",
        "user_id": 4,
        "activity_id": 1
    }
]
```

sendo um porfessor ou facilitador:

##### 200_OK
```json
[
    {
        "id": 1,
        "grade": 10,
        "repo": "http://gitlab.com/kenzie_pet",
        "user_id": 3,
        "activity_id": 1
    },
    {
        "id": 2,
        "grade": 8,
        "repo": "http://gitlab.com/kanvas",
        "user_id": 4,
        "activity_id": 2
    },
    {
        "id": 3,
        "grade": 4,
        "repo": "http://gitlab.com/kmdb",
        "user_id": 5,
        "activity_id": 3
    },
    {
        "id": 4,
        "grade": null,
        "repo": "http://gitlab.com/kmdb2",
        "user_id": 5,
        "activity_id": 3
    }
]
```
