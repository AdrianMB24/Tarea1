# -*- coding: cp1252 -*-
def basic_ops(operando_1,operando_2,operacion):
        if operacion == 1:
            resultado = operando_1 + operando_2
            return resultado
        elif operacion == 2:
            resultado = operando_1 - operando_2
            return resultado
        elif operacion == 3:
            resultado = operando_1 & operando_2
            return resultado
        elif operacion == 4:
            resultado = operando_1 | operando_2
            return resultado
        else:
            print ("operación inválida")

def array_ops(operando_1,operando_2,operacion):
    if len(operando_1) == len (operando_2):
        resultado = []
        for i in range(0, len(operando_1) ):
            a = basic_ops(operando_1[i], operando_2[i] ,operacion)
            resultado = resultado + [0]
            resultado [i] = a
        return resultado
    else:
        print ("Los arreglos no son del mismo tamaño")
