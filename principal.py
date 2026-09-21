from Centinela import Tratamiento
import os
import pickle

def menu():
    print("1.Cargar Tratamientos: ")
    print("2.Mostrar Resultados: ")
    print("0.Salir")
    print()


def load(vector):
    text = open("tratamientos.csv")
    text.readline()

    for line in text:
        if line[-1] == "\n":
            line = line[:-1]
        data = line.split(",")
        dni = data[0]
        nombre = data[1]
        apellido = data[2]
        codigo = data[3]
        monto_base = data[4]
        complejidad = data[5]
        id_algoritmo = data[6]

        tratamiento = Tratamiento(dni, nombre, apellido, codigo, monto_base, complejidad, id_algoritmo)
        vector.append(tratamiento)


def cont(vector):
    n = len(vector)
    contador = 0
    for i in range(n):
        contador += 1
    print("r1.1: ",contador)


def complex(vector):
    n = len(vector)
    cont = 0
    for i in range(n):
        if vector[i].complejidad == "A":
            cont += 1
    supreme = cont*[0]
    pos = 0
    for i in range(n):
        if vector[i].complejidad == "A":
            supreme[pos] = vector[i].lastname
            pos += 1
    for i in range(len(supreme)):
        if i == 4:
            print("r1.2: ",supreme[i])


def ultimate(vector):
    n = len(vector)
    porcentaje_extra = 0
    suma_fija = 0
    monto_final = 0
    monto_extra = 0
    a = 0
    for i in range(n):
        if vector[i].id_algoritmo == 1:
            if vector[i].monto_base > 60000:
                porcentaje_extra = (vector[i].codigo[4:]*vector[i].monto_base)/100
                if vector[i].complejidad == "A" and vector[i].codigo[0] != "U":
                    suma_fija = vector[i].monto_base / 2
                else:
                    suma_fija = 0
                monto_final = vector[i].monto_base + porcentaje_extra + suma_fija
            else:
                monto_final = vector[i].monto_base
        if vector[i].id_algoritmo == 2:
            if "A" <= vector[i].codigo <= "P":
                porcentaje_extra = (vector[i].codigo[4:] * vector[i].monto_base) / 100
            else:
                if vector[i].complejidad == "A":
                    a = vector[i].codigo[4:]
                    porcentaje_extra = a * 2
                else:
                    porcentaje_extra = vector[i].monto_base * 0.15
            monto_final = vector[i].monto_base + porcentaje_extra
        if vector[i].id_algoritmo == 3:
            if vector[i].complejidad == "A":
                monto_extra = (30 * vector[i].monto_base) / 100
            if "A" <= vector[i].codigo <= "L":
                monto_extra += 20000
            elif "M" <= vector[i].codigo <= "P":
                monto_extra += 15000 + (5000 *)
            else:
                monto_extra = (vector[i].monto_base * 10) / 100
            if monto_extra > 60000:
                monto_extra = 60000
            monto_final = vector[i].monto_base + monto_extra
        else:
            monto_final = vector[i].monto_base

    return monto_final


def promedio(vector):
    n = len(vector)
    diferencias = 0
    for i in range(n):
        monto_final = ultimate(vector)
        diferencias += monto_final - vector[i].monto_base
    diferencia_promedio = diferencias / n
    print("r2.1: ", diferencia_promedio)

def main():
    vector = []
    op = -1
    while op != 0:
        menu()
        print("--"*90)
        op = int(input("Ingrese opción: "))
        print()
        if op == 1:
            load(vector)
            cont(vector)
            complex(vector)
            print()
        elif op == 2:
            promedio(vector)


if __name__ == '__main__':
    main()
    print(".....")

