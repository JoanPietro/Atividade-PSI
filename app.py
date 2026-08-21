from flask import Flask, redirect, render_template, request, session, url_for
import models

app = Flask(__name__)
app.secret_key = "chave-da-livraria"

@app.route("/")
def index():
	query = request.args.get("q", "").strip()
	livros = models.buscar_livros(query)
	return render_template("index.html", livros=livros, query=query)


@app.route("/livro/<int:livro_id>")
def livro(livro_id):
	livro_encontrado = models.buscar_livro(livro_id)
	if livro_encontrado is None:
		return "Livro não encontrado", 404

	resenhas = models.resenhas_do_livro(livro_id)
	return render_template(
		"livro.html", livro=livro_encontrado, resenhas=resenhas
	)
