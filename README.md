# Comparador de Textos 🔍

Este projeto é uma ferramenta gráfica desenvolvida em Python para comparar textos de forma eficiente, utilizando uma interface intuitiva. Ele destaca as diferenças entre dois textos, como alterações, adições e remoções, ignorando espaços e acentuações para oferecer uma análise mais precisa.

## Funcionalidades

- **Comparação de Textos**: Compara duas versões de texto e destaca as diferenças encontradas.
- **Ignora Caracteres Especiais**: O comparador não considera espaços em branco extras ou acentuações como alterações, focando apenas em mudanças significativas.
- **Destaque de Alterações**:
  - **Removido**: Linhas que foram removidas do texto original são exibidas em vermelho.
  - **Adicionado**: Linhas adicionadas no novo texto são exibidas em verde.
  - **Detalhes**: Detalhes sobre modificações específicas são exibidos em azul.
- **Interface Gráfica Intuitiva**: Desenvolvido com Tkinter, o aplicativo apresenta uma interface amigável com abas para navegação.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca utilizada para criar a interface gráfica.
- **difflib**: Biblioteca para destacar as diferenças entre os textos.
- **unicodedata**: Para normalizar e remover acentuação dos textos comparados.

## Como Usar

1. Insira o texto 1 e o texto 2 nas respectivas áreas de entrada.
2. Clique no botão "Comparar Textos".
3. Visualize as diferenças no painel de resultados.

## Contribuição

Se você tiver sugestões de melhorias ou novas funcionalidades, fique à vontade para enviar uma pull request ou abrir uma issue.

## Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para obter detalhes.
