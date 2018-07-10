def text_reader(texto):
    arquivo = open(texto)
    textocompleto = arquivo.read()
    arquivo.close()
    texto1 = textocompleto.split('\n')
    for i in range(len(texto1)):
        print("\n" * 100)
        for j in range(i):
            print(texto1[j])
        print("")
        print("")
        input("PRESSIONE ENTER PARA CONTINUAR LENDO...")
    return textocompleto