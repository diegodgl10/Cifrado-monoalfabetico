import os

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
    menu += "1  Reemplzar caracter\n"
    menu += "2  Desacer acciones\n"
    menu += "0  Salir\n"
    while True:
        print(acciones[len(acciones) - 1])
        print("\n")
        print(menu)
        entrada = int(input("> "))
        if entrada == 1:
            entradaV = input("Reemplazar: ")
            entradaV = entradaV.upper()
            entradaN = input("Por: ")
            #entradaN = entradaN.upper()
            entradaN = entradaN.lower()
            acciones = remplazo(acciones, entradaV, entradaN)
            print("\n")
        elif entrada == 2:
            acciones = atras(acciones)
        else:
            return
        os.system('clear') #https://youtu.be/Kmu6rmPQt4c


def conteo():
    palabra = 'GKNKNIMUKFLKHPFOUHAUKHQJUHAUKHQJMUKLUNIKPKOIVFCIZFOAJHCJPMUKHJPTFRIFHIGLUCPFNJFKPFQFOKFUHAUKHQJMUKTFRCFOFNKCJPGIPQKOIJPJPQKOOJOKPNKHUKPQOFHFQUOFCKZFYNKPLKOQFPKGIKNJPKPQOKGKAKNJOKPMUKNKBFPKFCCKAQJOAJHQKGJONKGIOFOTFAIFPUFCOKNKNJOMUKLFOFCIZFPKCFPFHSOKYFAKCKOFOFCJPCFQINJPNKCAJOFZJHPIHJPKAJHPKSUIFKPJPOKPUCQFNJPGIAUKHQJNKEFHQFPGFPPKOIFIHNISHJNKPUHJGROKPKHQIFCFVFAIFIHAFLFAINFNNKIHVKHAIJHCFGFYJONKPSOFAIFMUKLUKNKFEKAQFOFUHCKAQJOAUFHNJFPUPFHPIJPFPIHVJFAIJHKPOKPLJHNKPJCJCFHFNFGFOYWPTKCCKY'
    letras_dic = dict()  #Guarda repetición de letras
    contador = 0 #Caracteres que se repiten
    for letra in palabra: #Por cada letra
        if letra in letras_dic: #Si ya estaba en el dic() significa que se repite
            if letras_dic[letra] == 1: 
                contador += 1 #Se agrega al contador
            letras_dic[letra] += 1 #Continua el conteo
        else:
            letras_dic[letra] = 1 #Si la letra no esta en el diccionario, la agrega
    print(letras_dic)
    print(contador)

def final():
    palabra = 'GK NKNIMUK F LKHPFO UH AUKHQJ UH AUKHQJ MUK LUNIKPK OIVFCIZFO AJH CJP MUK HJP TFRIFH IGLUCPFNJ F KPF QFOKF UH AUKHQJ MUK TFRCFOF NK CJP GIPQKOIJPJP QKOOJOKP NK HUKPQOF HFQUOFCKZF Y NKPLKOQFPK GIKNJP KPQOKGKAKNJOKP MUK NKBFPK FC CKAQJO AJH QKGJO NK GIOFO TFAIF PU FCOKNKNJO MUK LFOFCIZFPK CF PFHSOK Y FAKCKOFOF CJP CFQINJP NKC AJOFZJH PI HJ PK AJHPKSUIF KPJP OKPUCQFNJP GI AUKHQJ NK EFHQFPGFP PKOIF IHNISHJ NK PU HJGROK PKHQIF CF VFAIF IHAFLFAINFN NK IHVKHAIJH CF GFYJO NKPSOFAIF MUK LUKNK FEKAQFO F UH CKAQJO AUFHNJ F PUP FHPIJPFP IHVJFAIJHKP OKPLJHNK PJCJ CF HFNF GFOY W PTKCCKY'
    palabra = palabra.replace('A', 'c')
    palabra = palabra.replace('B', 'j')
    palabra = palabra.replace('C', 'l')
    palabra = palabra.replace('E', 'f')
    palabra = palabra.replace('F', 'a')
    palabra = palabra.replace('G', 'm')
    palabra = palabra.replace('H', 'n')
    palabra = palabra.replace('I', 'i')
    palabra = palabra.replace('J', 'o')
    palabra = palabra.replace('K', 'e')
    palabra = palabra.replace('L', 'p')
    palabra = palabra.replace('M', 'q')
    palabra = palabra.replace('N', 'd')
    palabra = palabra.replace('O', 'r')
    palabra = palabra.replace('P', 's')
    palabra = palabra.replace('Q', 't')
    palabra = palabra.replace('R', 'b')
    palabra = palabra.replace('S', 'g')
    palabra = palabra.replace('T', 'h')
    palabra = palabra.replace('U', 'u')
    palabra = palabra.replace('V', 'v')
    palabra = palabra.replace('W', 'w')
    palabra = palabra.replace('Y', 'y')
    palabra = palabra.replace('Z', 'z')
    #palabra = palabra.upper()
    print(palabra)
#main()
final()
#conteo()