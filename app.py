from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'Título do Artigo 1',
            'content': 'Conteúdo do Artigo 1...'
        },
        {
            'title': 'Título do Artigo 2',
            'content': 'Conteúdo do Artigo 2...'
        },
        {
            'title': 'Título do Artigo 3',
            'content': 'Conteúdo do Artigo 3...'
        },
        {
            'title': 'Título do Artigo 4',
            'content': 'Conteúdo do Artigo 4...'
        },
        {
            'title': 'Título do Artigo 5',
            'content': 'Conteúdo do Artigo 5...'
        },
        {
            'title': 'Título do Artigo 6',
            'content': 'Conteúdo do Artigo 6...'
        }
    ]

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
