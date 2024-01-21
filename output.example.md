## /health
### Descrição:
Este Endpoint tem como objetivo mostrar a saúde da API, se está disponível para uso. Retorna uma resposta descrevendo a saúde do sistema.

### Métodos HTTP:
- GET

### URL:
- ``http://localhost:8080/v1/health``


## Método GET:

### Exemplo de Requisição:


```http
GET http://localhost:8080/v1/health
Content-Type: application/json

{}
```


### Exemplo de Resposta:


#### Caso: `SUCCESS`

```http 
Status code: 200

Content-Type: application/json
X-health: GOOD

{
  "situation": "healthy",
  "details": null
}
```

#### Caso: `DATABASE_FAIL`

```http 
Status code: 500

Content-Type: application/json
X-health: corromped

{
  "situation": "failure",
  "details": {
    "database": "corromped"
  }
}
```


