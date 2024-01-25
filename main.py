from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/resultado", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        opcion = request.form.get("opcion")
        #return "Opcion seleccionada: {}".format(opcion)
        if opcion == "sum":
            return "La suma de {} + {} = {}".format(num1, num2, str(int(num1) + int(num2)))
        else: 
            if opcion == "res":
                return "La resta de {} - {} = {}".format(num1, num2, str(int(num1) - int(num2)))
            else:
                if opcion == "mul":
                    return "La multiplicacion de {} * {} = {}".format(num1, num2, str(int(num1) * int(num2)))
                else: 
                    if opcion == "div":
                        return "La division de {} / {} = {}".format(num1, num2, str(int(num1) / int(num2)))
                    else:
                        return "Seleccione una operacion primero."
    
    else:
        return '''
            <form action="/resultado" method="POST">
                <label>N1</label>
                <input type="text" name="n1"></input><br>
                <label>N2</label>
                <input type="text" name="n2"></input><br>
                <input type="submit">

                <input type="radio" name="opcion" value="sum">Suma
                <input type="radio" name="opcion" value="res">Resta
                <input type="radio" name="opcion" value="div">Division
                <input type="radio" name="opcion" value="mul">Multiplicacion
            </form>
            '''


@app.route("/operabas")
def operabas():
    return render_template("operabas.html")


if __name__ == "__main__":
    app.run(debug=True)