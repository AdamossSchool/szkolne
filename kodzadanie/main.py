alfabet = 'aAąĄbBcCćĆdDeEęĘfFgGhHiIjJkKlLłŁmMnNńŃoOóÓpPqQrRsSśŚtTuUvVwWxXyYzZźŹżŻ'

tekst_start =""
tekst_wy =""
znak     =""
przes    = 0
indx     = 0



while(1):
    tekst_start = input("Podaj tekst: ")
    if tekst_start == "" :
        break
    przes    = int(input("Podaj klucz: "))
    tekst_wy = ""

    for znak in tekst_start:
        indx = alfabet.find(znak)

        if indx != -1 :
            tekst_wy += alfabet[ (indx + przes) % len(alfabet) ]
        else:
            tekst_wy += znak

    print("Tekst zaszyfrowany to: " + tekst_wy)