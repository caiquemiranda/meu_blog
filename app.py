from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os posts do blog
posts = [
    {
        'titulo': 'Meu primeiro post',
        'autor': 'João',
        'conteudo': 'Este é o meu primeiro post no blog!'
    },
    {
        'titulo': 'Segundo post',
        'autor': 'Maria',
        'conteudo': 'Aqui está o meu segundo post. Espero que gostem!'
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
