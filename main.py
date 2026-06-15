from flask import Flask

app = Flask("__main__")

@app.route("/")
def main():
    return "pagina inicial"

if __name__ == "__main__":
    app.run(debug=True)