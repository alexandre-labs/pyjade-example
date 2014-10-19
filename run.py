from app import app

app.debug = True
app.use_reload = True
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
