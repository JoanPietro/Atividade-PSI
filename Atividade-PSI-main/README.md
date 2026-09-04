# Atividade-PSI#

 Livraria MVC

# 1. Camadas do MVC

O Model esta em `models.py`. Ele concentra os dados e as funcoes `buscar_livro`, `resenhas_do_livro` e `buscar_livros`. O Controller esta em `app.py`, que recebe as requisicoes, chama o Model e escolhe os templates. A View esta na pasta `templates/` com arquivos HTML que usam Jinja2. Se a logica de acesso aos dados ficasse dentro das rotas, o Controller ficaria misturado com o Model. Isso dificultaria a manutencao.

# 2. Uso de `url_for`

Usamos `url_for`, por exemplo, em `url_for('livro', livro_id=livro['id'])`. Ele gera a URL a partir do nome da rota. Assim, se o caminho da rota mudar, os links continuam consistentes sem precisar procurar e alterar URLs fixas espalhadas pelos templates.

# 3. Session

A `session` representa o usuario autenticado entre requisicoes. No login, o Controller guarda o nome com `session['usuario']. A rota de resenha verifica essa informacao antes de gravar porque somente clientes logados podem publicar e o nome salvo na resenha deve vir da identidade autenticada.
