from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcular_tempo():
    if request.method == "POST":
        try:
            # Recebe os valores da distância e velocidade
            distancia = float(request.form["distancia"])
            velocidade = float(request.form["velocidade"])

            # Calcula o tempo de viagem
            tempo = distancia / velocidade

            return render_template("index.html", tempo=tempo, distancia=distancia, velocidade=velocidade)
        except ValueError:
            # Caso o usuário insira valores inválidos
            return render_template("index.html", erro="Por favor, insira valores válidos para distância e velocidade.")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
