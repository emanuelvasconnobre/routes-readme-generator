import json
from method import method_builder

# Variável para "Nenhum(a)"
none_placeholder = "Nenhum(a)"


def read_template(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_readme(data, endpoint_template):
    endpoints_section = ""
    for endpoint in data.get("endpoints", []):
        examples_section = endpoint_template.format(
            path=endpoint["path"],
            description=endpoint["description"],
            allow_methods=", ".join(endpoint.get("allow_methods", [none_placeholder])),
            url=f"`{endpoint.get('url', none_placeholder)}`",
            examples_section=method_builder(endpoint["request_methods"]),
        )

        endpoints_section += examples_section

    return endpoints_section


# Leitura do template de arquivo
endpoint_template_path = "./endpoint_template.txt"
endpoint_template = read_template(endpoint_template_path)

# Leitura dos dados do arquivo JSON
json_data_path = "./data.json"
with open(json_data_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Gere o README
readme_content = generate_readme(data, endpoint_template)

# Escreva o README no arquivo de saída
output_path = "./output.md"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(readme_content)

print(f"README gerado com sucesso! Salvo em: {output_path}")
