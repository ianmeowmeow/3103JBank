from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    variable = "test"
    return render_template('index.html', testvariable=variable)


if __name__ == "__main__":
    app.run()
