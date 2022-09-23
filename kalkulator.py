#kalkulator
keuro = 4.26
kusd = 3.89


print("KALKULATOR")

 




 
def dodawanie(x, y):
   return x + y
 
def odejmowanie(x, y):
   return x - y
 
def mnozenie(x, y):
   return x * y
 
def dzielenie(x, y):
   return x / y
 
def pln_euro(x,keuro):
    return x * keuro

def euro_pln(x,keuro):
    return x / keuro

def pln_usd(x,kusd):
    return x * kusd

def usd_pln(x,kusd):
    return x / kusd


  
 
wyjscie = False



while wyjscie == False:
    print("              ")
    print(":Menu:")
    print("A - dodawanie")
    print("B - odejmowanie")
    print("C - mnozenie")
    print("D - dzielenie")
    print("E - wyjscie")
    print("F - pln na euro")
    print("H - euro na pln")
    print("H - pln na usd")
    print("I - usd na pln")
    
  
    choice = input("Wybierz (A/B/C/D/E?F/G/H/I):")


    


  
    if choice == 'E':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (A/B/C/D/E):")




  
    x= float(input("Podaj liczbe: "))


    conditions = ['F','G','H','I']
    if any(conditions) and not all(conditions):
      y = float(input("Podaj liczbe: "))









  
  
    if choice == 'A':
         print(x,"+",y,"=", dodawanie(x,y))
 
    elif choice == 'B':
        print(x,"-",y,"=", odejmowanie(x,y))
 
    elif choice == 'C':
         print(x,"*",y,"=", mnozenie(x,y))

    
    elif choice == 'F':
         print(x,"*",keuro,"=", pln_euro(x,keuro))

    elif choice == 'G':
         print(x,"/",keuro,"=", euro_pln(x,y))

    elif choice == 'H':
         print(x,"*",kusd,"=", pln_usd(x,kusd))

    elif choice == 'I':
         print(x,"/",kusd,"=", usd_pln(x,kusd))



      
    elif choice == 'D':
      if y == 0:  
        import time
        print("uwaga nie da się dzielić przez zero")
        time.sleep(2)
      else:
        print(x,"/",y,"=", dzielenie(x,y))
 
    
    else:
     print("na ma takiej opcji opcje!")