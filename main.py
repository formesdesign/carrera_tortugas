import turtle
import random
# el random es la llibreria que genera numeros aleatoris

class Circuit():
#per als corredors creem una llista vuida
    corredors =[]
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ("blue", "orange", "green", "red")
#definirem la pantalla, dimensions, bgcolor(color de fons)     
    def __init__(self, width, height):        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 -20
        
        self.__createRunners()
        
    def __createRunners(self):
        
#creem els corredor en una etiqueta i deferenciarlos. penup(no pinta la linea)
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])

            self.corredors.append(new_turtle)
            
    def competir(self):
        hihaGuanyador = False
        
        while not hihaGuanyador:
            for tortuga in self.corredors:
                avance = random.randint(1,6)
                tortuga.fd(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hihaGuanyador = True
                    print ("La tortugueta de color {} ha guanyat".format(tortuga.color()[0]))
                    break

        
if __name__ == "__main__":
    circuit = Circuit(640, 480)
    circuit.competir()