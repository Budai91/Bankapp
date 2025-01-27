'''
En bankapplikation där användaren kan göra olika val som uttag, insättning, visa saldo, ta lån och avsluta programmet.

Features:
1: visa balans/konto #funktion
2: Sätta in pengar #funktion
3: Ta ut pengar #funktion
4: starta/stäng av appen
6: Visa återstående saldo efter uttag.
7: färgad text för balans

'''

saldo = 0.00 #Utångs saldo, behövs för uträkningar av saldo.

while True :
    x = input("Hej!\nVänligen välj 1-5:\n 1 Uttag.\n 2 Insättning.\n 3 Saldo.\n 4 Lån.\n 5 Avsluta.") #Variabel för att välja alternativ.
    if x == '1' : #if-statement
        uttag = float(input ("Hur många kronor vill du ta ut:? \n")) #variabel för uttag.
        if uttag > saldo:
            print  ("=======================================")
            print ("\033[31mDu har inte nog med pengar på kontot\033[0m") #om uttag är större än saldo
            print  ("=======================================")

        else:
            saldo -= uttag #räknar ut saldo efter uttag
            print  ("=======================================")
            print (f"Du har tagit ut {uttag:.2f}kr.") #visar hur mycket pengar du tagit ut med hjälp av en f-sträng
            print  ("=======================================")

    elif x == '2' :
        print  ("=======================================")
        insättning = float(input("Hur många kronor vill du sätta in:?\n")) #Frågar användaren hur mycket hen vill sätta in.
        print  ("=======================================")
        saldo += insättning #Räknar ut vad saldo blir efter insättning.
        print (f"Du har satt in {insättning:.2f}kr.") #Utskrift av insättning med hjälp av en f-sträng.
        print  ("=======================================")

    elif x == '3' :
       print  ("=======================================")
       print(f"\033[32mDitt saldo är {saldo:.2f}kr.\033[0m") #Utskrift av saldo med hjälp av en f-sträng.
       print  ("=======================================")

    elif x == '4' :
         print  ("=======================================")
         lån = float(input("Ange mängd kronor du vill du låna?")) #Frågar användaren hur mycket hen vill låna.
         print  ("=======================================")
         saldo += lån #Räknar ut vad saldo blir efter lån.
         print  ("=======================================")
         print (f"Du har lånat {lån:.2f}kr.") #Utskrift av lånad summa med hjälp av en f-sträng.
         print  ("=======================================")

    elif x == '5' :
        logga_ut = (input("Vill du logga ut: ja/nej?")) #Input för att logga ut (eller stanna kvar).
        if  logga_ut == 'nej' :
            print  ("=======================================")
            print("Du är fortfarande inloggad")
            print  ("=======================================")
        if logga_ut == 'ja' :
                print  ("=======================================")
                print ("Du är utloggad. Ha en trevlig dag!")
                print  ("=======================================")
                break
                
    else :
        print  ("=======================================")
        print("Ogiltigt val, vänligen försök igen") #För ogilitga val.
        print  ("=======================================")






