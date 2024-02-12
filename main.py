from flask import Flask, render_template, request
from math import sqrt
import formulario
import formulario_resistencia

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout3_Resistencia.html")


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

@app.route("/distancia", methods=["GET","POST"])
def distancia():

    formularioClass = formulario.DistanciaForm(request.form)
    p1c1 = ''
    p2c1 = ''
    p1c2 = ''
    p2c2 = ''
    resultado = ''
   
    if request.method == 'POST':
        
        p1c1 = formularioClass.p1c1.data
        p2c1 = formularioClass.p2c1.data
        p1c2 = formularioClass.p1c2.data
        p2c2 = formularioClass.p2c2.data
        resultado = sqrt(pow((p1c2 - p1c1), 2) + pow((p2c2 - p2c1), 2))


       
        print("Punto 1 Coordenada 1: {}".format(p1c1))
        print("Punto 2 Coordenada 1: {}".format(p2c1))
        print("Punto 1 Coordenada 2: {}".format(p1c2))
        print("Punto 2 Coordenada 2: {}".format(p2c2))
        print("Resultado: {}".format(resultado))
        

    return render_template("distancia.html", form = formularioClass, p1c1=p1c1, p2c1=p2c1, p1c2=p1c2, p2c2=p2c2, resultado=resultado)



@app.route("/Resistencia", methods = ["POST", "GET"])
def resistencia():
    ResistenciaClass = formulario_resistencia.Resistencia(request.form)
    color1 = ''
    color2 = ''
    color3 = ''
    tolerancia =''
    valor = ''
    valorMin = ''
    valorMax = ''
    tipoTol = ''
    colorT1 = ''
    colorT2 = ''
    colorT3 = ''
    Ccolor1 = ''


    if request.method == "POST":
        color1 = ResistenciaClass.color1.data
        color2 = ResistenciaClass.color2.data
        color3 = ResistenciaClass.color3.data
        tolerancia = ResistenciaClass.tolerancia.data

        valor = int(color1+color2) * int(color3)

        if tolerancia == "Oro":
            tipoTol = "Oro 5%"
            CcolorT = "gold"
            valorMax = valor+ (valor * 0.05)
            valorMin = valor- (valor * 0.05)
        else:
            tipoTol = "Plata 10%"
            CcolorT = "silver"
            valorMax = valor+ (valor * 0.10)
            valorMin = valor- (valor * 0.10)     

        print("Color 1: {}".format(color1))
        print("Color 2: {}".format(color2))
        print("Color 3: {}".format(color3))
        print("Color tolerancia: {}".format(tolerancia))
        print("Valor: {}".format(valor))
        print("Tolerancia tipo {}".format(tipoTol))
        print("Valor Maximo: {}  Valor minimo: {}".format(valorMax, valorMin))

        
        if color1 == "0":
            colorT1 = "Negro"
            Ccolor1 = 'Black; color: White'
        elif color1 == "1":
            colorT1 = "Cafe"
            Ccolor1 = "Brown; color: White"
        elif color1 == "2":
            colorT1 = "Rojo"
            Ccolor1 = "Red"
        elif color1 == "3":
            colorT1 = "Naranja"
            Ccolor1 = "Orange"
        elif color1 == "4":
            colorT1 = "Amarillo"
            Ccolor1 = "Yellow"
        elif color1 == "5":
            colorT1 = "Verde"
            Ccolor1 = "Green; color: White"
        elif color1 == "6":
            colorT1 = "Azul"
            Ccolor1 = "Blue; color: White"
        elif color1 == "7":
            colorT1 = "Violeta"
            Ccolor1 = "Violet"
        elif color1 == "8":
            colorT1 = "Gris"
            Ccolor1 = "Gray; color: White"
        else:
            colorT1 = "Blanco"
            Ccolor1 = "White"
        

        if color2 == "0":
            colorT2 = "Negro"
            Ccolor2 = 'Black; color: White'
        elif color2 == "1":
            colorT2 = "Cafe"
            Ccolor2 = "Brown; color: White"
        elif color2 == "2":
            colorT2 = "Rojo"
            Ccolor2 = "Red"
        elif color2 == "3":
            colorT2 = "Naranja"
            Ccolor2 = "Orange"
        elif color2 == "4":
            colorT2 = "Amarillo"
            Ccolor2 = "Yellow"
        elif color2 == "5":
            colorT2 = "Verde"
            Ccolor2 = "Green; color: White"
        elif color2 == "6":
            colorT2 = "Azul"
            Ccolor2 = "Blue; color: White"
        elif color2 == "7":
            colorT2 = "Violeta"
            Ccolor2 = "Violet"
        elif color2 == "8":
            colorT2 = "Gris"
            Ccolor2 = "Gray; color: White"
        else:
            colorT2 = "Blanco"
            Ccolor2 = "White"


        if color3 == "1":
            colorT3 = "Negro"
            Ccolor3 = 'Black; color: White'
        elif color3 == "10":
            colorT3 = "Cafe"
            Ccolor3 = "Brown; color: White"
        elif color3 == "100":
            colorT3 = "Rojo"
            Ccolor3 = "Red"
        elif color3 == "1000":
            colorT3 = "Naranja"
            Ccolor3 = "Orange"
        elif color3 == "10000":
            colorT3 = "Amarillo"
            Ccolor3 = "Yellow"
        elif color3 == "100000":
            colorT3 = "Verde"
            Ccolor3 = "Green; color: White"
        elif color3 == "1000000":
            colorT3 = "Azul"
            Ccolor3 = "Blue; color: White"
        elif color3 == "10000000":
            colorT3 = "Violeta"
            Ccolor3 = "Violet"
        elif color3 == "100000000":
            colorT3 = "Gris"
            Ccolor3 = "Gray; color: White"
        else:
            colorT3 = "Blanco"
            Ccolor3 = "White"

    return render_template("Resistencia.html", form =ResistenciaClass, color1 = color1,
                             color2= color2, color3 = color3, tolerancia = tolerancia, 
                             tipoTol = tipoTol, valor = valor, valorMax = valorMax, 
                             valorMin = valorMin, colorT1 = colorT1, Ccolor1 = Ccolor1,
                              colorT2 = colorT2, Ccolor2 = Ccolor2, colorT3 = colorT3, Ccolor3 = Ccolor3,
                              CcolorT = CcolorT)


if __name__ == "__main__":
    app.run(debug=True)