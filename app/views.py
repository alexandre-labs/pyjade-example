from . import app
from flask import render_template, request


@app.route('/')
def main():
    return 'Leia o código fonte do views.py... é tão simples. =]'


@app.route('/jinja')
@app.route('/jade')
def jinja_vs_jade():
    # utiliando uma lista, podemos testar condicionais e loops...
    nomes = ['Foo', 'Bla', 'Bar', 'Bleh']
    # selecionamos o arquivo de acordo com o path do request
    # e.g http://localhost:5000/jinja -> "/jinja" é o path
    if 'jade' in request.path:
        return render_template('example2.jade', nomes=nomes)
    return render_template('example2.html', nomes=nomes)


@app.route('/jinja/macros')
@app.route('/jade/macros')
@app.route('/jade/macros-no-safe')
def macros():

    # dicionario para exemplo com macro
    dados = {
        'Foo': ['Python', 'Open Source', 'Hacking'],
        'Bar': ['Saída', 'Retrato', 'Funcional'],
        'Blah': ['Ideia', 'Mozilla', 'Incompletude']
    }

    if 'jade' in request.path:
        # renderizar arquivo sem a função safe
        # para exemplificar...
        if 'macros-no-safe' in request.path:
            return render_template('example3-no-safe.jade', dados=dados)
        return render_template('example3.jade', dados=dados)
    return render_template('example3.html', dados=dados)
