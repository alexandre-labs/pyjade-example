from . import app
from flask import render_template, request


@app.route('/')
def main():
    return 'Olá, eu sou os códigos <del>feios</del> utilizados como exemplos\
nesse <a href="http://alexandre.github.io"> blog post</a> =]'


@app.route('/jinja')
@app.route('/jade')
def jinja_vs_jade():
    nomes = ['Foo', 'Bla', 'Bar', 'Bleh']
    if 'jade' in request.path:
        return render_template('example2.jade', nomes=nomes)
    return render_template('example2.html', nomes=nomes)


@app.route('/jinja/macros')
@app.route('/jade/macros')
@app.route('/jade/macros-no-safe')
def macros():

    dados = {
        'Foo': ['Python', 'Open Source', 'Hacking'],
        'Bar': ['Saída', 'Retrato', 'Funcional'],
        'Blah': ['Ideia', 'Mozilla', 'Incompletude']
    }
    if 'jade' in request.path:
        if 'macros-no-safe' in request.path:
            return render_template('example3-no-safe.jade', dados=dados)
        return render_template('example3.jade', dados=dados)
    return render_template('example3.html', dados=dados)
