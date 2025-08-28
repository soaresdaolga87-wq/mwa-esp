from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/pedido", methods=["GET"])
def pedido():
    dados = {
        "nome": "João Manuel",
        "bairro": "Namiteca",
        "latitude": -15.105,
        "longitude": 39.280
    }
    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
