from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/support')
def support():
    return render_template("support.html")


@app.route('/license')
def license():
    return render_template("license.html")


@app.route('/documents')
def documents():
    return render_template("documents.html")

# Блок с адресами и новостями [НАЧАЛО]
@app.route('/achievements')
def achievements():
    return render_template("achievements.html")


@app.route('/griboyedova7')
def griboyedova7():
    return render_template("griboyedova7.html")


@app.route('/griboyedova7a')
def griboyedova7a():
    return render_template("griboyedova7a.html")


@app.route('/emlyutina38')
def emlyutina38():
    return render_template("emlyutina38.html")


@app.route('/lenina9')
def lenina9():
    return render_template("lenina9.html")


@app.route('/stdmitrova57')
def stdmitrova57():
    return render_template("stdmitrova57.html")


@app.route('/stdmitrova53')
def stdmitrova53():
    return render_template("stdmitrova53.html")


@app.route('/fokina4')
def fokina4():
    return render_template("fokina4.html")


# Блок с адресами и новостями [КОНЕЦ]


# @app.route('/iindex')
# def iindex():
#     return render_template("iindex.html")




@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == '__main__':
    app.run(debug=True)
