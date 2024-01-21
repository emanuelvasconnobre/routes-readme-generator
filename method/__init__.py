import json

method_request_template = """
```http
{method} {url}
Content-Type: application/json
{headers}

{body}
```
"""


def method_request(method: str, url: str, body: dict, headers: list[str]):
    return method_request_template.format(
        method=method,
        url=url,
        body=json.dumps(body, ensure_ascii=False, indent=2),
        headers="\n".join(headers),
    )


method_response_case_template = """
#### Caso: `{name}`

```http 
Status code: {status}

Content-Type: application/json
{headers}

{body}
```
"""


def method_responses(responses: list[dict]):
    result = ""

    for response in responses:
        result += response_case(
            name=response["name"],
            status=response["status"],
            headers=response["headers"],
            body=response["body"],
        )

    return result


def response_case(name: str, status: int, headers: list[str], body: dict):
    return method_response_case_template.format(
        name=name,
        status=status,
        headers="\n".join(headers),
        body=json.dumps(body, ensure_ascii=False, indent=2),
    )


method_template = """
## Método {method}:

### Exemplo de Requisição:

{request_section}

### Exemplo de Resposta:

{response_section}
"""


def method_builder(method_data: list[dict]):
    result = ""

    for method in method_data:
        request_section = method_request(
            method=method["method"],
            body=method["request_details"]["body"],
            headers=method["request_details"].get("headers", []),
            url=method["request_details"]["url"],
        )

        response_section = method_responses(method["response_cases"])

        result += method_template.format(
            method=method["method"],
            request_section=request_section,
            response_section=response_section,
        )

    return result
