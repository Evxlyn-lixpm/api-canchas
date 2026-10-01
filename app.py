from flask import Flask, jsonify

app = Flask(__name__)

canchas = [
    {
        "id": 1,
        "fecha": "2026-10-02",
        "hora": "10:00",
        "estado": "Disponible",
        "tipo_cancha": "Cancha sintética",
        "precio": 60,
        "duracion": "1 hora"
    },
    {
        "id": 2,
        "fecha": "2026-10-02",
        "hora": "12:00",
        "estado": "Reservada",
        "tipo_cancha": "Cancha sintética",
        "precio": 60,
        "duracion": "1 hora"
    },
    {
        "id": 3,
        "fecha": "2026-10-02",
        "hora": "15:00",
        "estado": "Disponible",
        "tipo_cancha": "Cancha techada",
        "precio": 70,
        "duracion": "1 hora"
    },
    {
        "id": 4,
        "fecha": "2026-10-03",
        "hora": "09:00",
        "estado": "Disponible",
        "tipo_cancha": "Cancha sintética",
        "precio": 60,
        "duracion": "1 hora"
    },
    {
        "id": 5,
        "fecha": "2026-10-03",
        "hora": "18:00",
        "estado": "Reservada",
        "tipo_cancha": "Cancha techada",
        "precio": 70,
        "duracion": "1 hora"
    }
]


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API Cancha Fútbol funcionando correctamente"
    })


@app.route("/api/canchas")
def obtener_canchas():
    return jsonify(canchas)


@app.route("/api/canchas/<int:id>")
def obtener_cancha(id):
    for cancha in canchas:
        if cancha["id"] == id:
            return jsonify(cancha)

    return jsonify({
        "error": "Cancha no encontrada"
    }), 404


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))