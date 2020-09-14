# -*- coding: cp1252 -*-

def basic_ops(operando_1,operando_2,operacion):

        if type(operando_1) == int and type(operando_2) == int and type(operacion) == int:
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
                            print ("Error 3 = OperationOutOfRangeError: la operación ingresada no está dentro de las opciones")
        else:
               print ("Error 1 = TypeError: Valores ingresados no corresponden a números enteros")

def array_ops(operando_1,operando_2,operacion):
        if len(operando_1) == len (operando_2):
                resultado = []
                for i in range(0, len(operando_1) ):
                        if type(operando_1[i]) == int and type(operando_2[i]) == int and type(operacion) == int:
                                if 1 <= operacion <= 4:
                                        a = basic_ops(operando_1[i], operando_2[i] ,operacion)
                                        resultado = resultado + [0]
                                        resultado [i] = a
                                else:
                                        print ("Error 3 = OperationOutOfRangeError: la operación ingresada no está dentro de las opciones")
                                        resultado = None
                                        break
                        else:
                                print ("Error_1 = TypeError: Valores ingresados no corresponden a números enteros")
                                resultado = None
                                break
                return resultado
        else:
                print ("Error_4 = LenError: Los arreglos no son del mismo tamaño")
