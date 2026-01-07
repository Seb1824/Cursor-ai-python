from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Esta aplicación fue creada con ayuda de IA usando Cursor."

if __name__ == '__main__':
    app.run(debug=True)