import app
import json

# Leitura dos dados do arquivo JSON
json_data_path = "./data.json"
with open(json_data_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Gere o README
readme_content = app.endpoint_readme_build(data)

# Escreva o README no arquivo de saída
output_path = "./output.md"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(readme_content)

print(f"README gerado com sucesso! Salvo em: {output_path}")
