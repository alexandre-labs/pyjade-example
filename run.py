from app import app

# exibe erros
app.debug = True

# recarrega os arquivos quando houver alterações
app.use_reload = True

# faz a mágica, extensão .jade
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
