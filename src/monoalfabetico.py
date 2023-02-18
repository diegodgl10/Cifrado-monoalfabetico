def atras(acciones):
    if len(acciones) > 1:
        acciones.pop(len(acciones) - 1)
    return acciones

def remplazo(acciones, viejo, nuevo):
    actualizado = acciones[len(acciones) - 1]
    if viejo in actualizado:
        acciones.append(actualizado.replace(viejo, nuevo))
    return acciones

def main():
    string = "GK NKNIMUK F LKHPFO UH AUKHQJ UH AUKHQJ MUK LUNIKPK OIVFCIZFO AJH CJP MUK HJP TFRIFH IGLUCPFNJ F KPF QFOKF UH AUKHQJ MUK TFRCFOF NK CJP GIPQKOIJPJP QKOOJOKP NK HUKPQOF HFQUOFCKZF Y NKPLKOQFPK GIKNJP KPQOKGKAKNJOKP MUK NKBFPK FC CKAQJO AJH QKGJO NK GIOFO TFAIF PU FCOKNKNJO MUK LFOFCIZFPK CF PFHSOK Y FAKCKOFOF CJP CFQINJP NKC AJOFZJH PI HJ PK AJHPKSUIF KPJP OKPUCQFNJP GI AUKHQJ NK EFHQFPGFP PKOIF IHNISHJ NK PU HJGROK PKHQIF CF VFAIF IHAFLFAINFN NK IHVKHAIJH CF GFYJO NKPSOFAIF MUK LUKNK FEKAQFO F UH CKAQJO AUFHNJ F PUP FHPIJPFP IHVJFAIJHKP OKPLJHNK PJCJ CF HFNF GFOY W PTKCCKY"
    acciones = [string]
    menu = "OPCIONES\n"
    menu += "1  Desacer acciones\n"
    menu += "2  Reemplzar caracter\n"
    menu += "0  Salir\n"
    while True:
        print(acciones[len(acciones) - 1])
        print("\n")
        print(menu)
        entrada = int(input("> "))
        if entrada == 1:
            acciones = atras(acciones)
        elif entrada == 2:
            entradaV = input("Reemplazar: ")
            entradaV = entradaV.upper()
            entradaN = input("Por: ")
            entradaN = entradaN.upper()
            acciones = remplazo(acciones, entradaV, entradaN)
            print("\n")
        else:
            return

main()
