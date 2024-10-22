from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/servicio-a', methods=['GET'])
def servicio_a():
    return jsonify({"mensaje": "Respuesta desde Servicio A"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)