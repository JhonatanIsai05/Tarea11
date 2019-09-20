def romano_a_arabigo(numero_romano):
    resultado = 0

    valores = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }

    if len(numero_romano) > 0:
        valor_anterior = 0

    for letra in numero_romano:

        if letra in valores:
            valor_actual = valores[letra]
        else:
            print ('Valor invalido:', letra)
            return 'NaN' # NaN: Not A Number

        if valor_anterior >= valor_actual:
            resultado += valor_actual
        else:
            resultado += valor_actual - (2 * valor_anterior)

        valor_anterior = valor_actual

    return resultado

numero_romano = input("Numero Romano: ").upper()
print ("Numero Arabigo:", romano_a_arabigo (numero_romano))
