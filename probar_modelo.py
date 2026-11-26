# Importamos la clase desde nuestro archivo modelo_sensor
from modelo_sensor import LecturaSensor

def ejecutar_pruebas_unitarias():

    # Caso 1: Lectura en rango Bptimo (5.e c)
    lectura_optima = LecturaSensor("LOTE-01", 5.0, 85.0)


    # assert: Instruccion de Python que comprueba si una condicign es verdadera;
    # si es falsa, detiene el programa y lanza un mensaje de error.
    assert lectura_optima.estado_conservacion == "OPTIMO", "Error: Deberga resultar OPTIMO"


    # Caso 2: Temperatura por encima del 1fnite (9.2 c)
    lectura_calor = LecturaSensor("LOTE-02", 9.2, 80.0)
    assert lectura_calor.estado_conservacion == "ALERTA: RIESGO DE DESCOMPOSICION", "Error en alerta de calor"


    # Caso 3: Temperatura por debajo del 1fnite (1.5 Ec)
    lectura_frio = LecturaSensor("LOTE-03", 1.5, 90.0)
    assert lectura_frio.estado_conservacion == "ALERTA: RIESGO DE CONGELAMIENTO", "Error en alerta de frio"

    # Caso 4: Verificacign de estructura del diccionario
    diccionario_resultado = lectura_optima.convertir_a_diccionario()


    # isinstance(): Funcion de Python que comprueba si una variable pertenece a un tipo de dato especfico
    assert isinstance(diccionario_resultado, dict), "Error: El resultado debe ser un diccionario"
    assert "estado" in diccionario_resultado, "Error: Falta la clave 'estado' en el diccionario"

    # print(): Funcion de Python para mostrar mensajes en la consola
    print("=========================================================")
    print(">>> TODAS LAS PRUEBAS UNITARIAS PASARON EXITOSAMENTE (4/4) <<< ")
    print("=========================================================")

if __name__== "_main_":
    ejecutar_pruebas_unitarias()