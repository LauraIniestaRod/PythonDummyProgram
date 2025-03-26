"""
Este módulo contiene la funcionalidad principal del programa.
Realiza la suma y resta de números y lo muestra
"""

from flask import Flask, jsonify
from script import add, subtract

app = Flask(__name__)


@app.route("/")
def home():
    """Este método se encarga de mostrar el resultado
    de operaciones matemáticas"""
    a, b = 10, 5  # Valores de ejemplo
    sum_result = add(a, b)
    sub_result = subtract(a, b)

    response = {
        "addition": f"{a} + {b} = {sum_result}",
        "subtraction": f"{a} - {b} = {sub_result}",
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
