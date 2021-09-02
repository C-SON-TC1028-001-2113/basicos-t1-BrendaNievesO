def main():
    #escribe tu código abajo de esta línea
    a = int(input('Calificacion de la primera materia: ')) 

    b = int(input('Calificacion de la segunda materia: ')) 

    c = int(input('Calificacion de la tercera materia: ')) 

    d = int(input('Calificacion de la cuarta materia: ')) 
    promedio = (a+b+c+d)/4 
    print ("Promedio del alumno: "+str(promedio))

if __name__ == '__main__':
    main()
