import time

def start():
    print("""Doktor není ze Země, je to Pán času z planety Gallifrey. Páni času byli považováni za jednu z nejstarších a
    nejmocnějších ras ve vesmíru. V minulosti šli Páni času do války s rasou zvanou Dáleci a prohráli.
    Jedinému Doktorovi se podařilo utéct díky jeho stroji času zvanému TARDIS.""")
    print("\n")
    time.sleep(5)
    print("Doktor si myslí, že je poslední svého druhu, ale v legendách se píše o někom zvaném Vládce, prý také Pán času, který uvázl na pohřebišti Dáleků, planetě Minoris.")
    print("\n")
    time.sleep(5)
    print("Tvým úkolem v této hře je Vládce najít.")
    print("\n")
    time.sleep(5)
    print("Hra se ovládá čísly 1 nebo 2")
    print("\n")

    print("Jakým směrem se chceš vydat?")
    print("1. planeta Minoris")
    print("2. zůstaneš ve svojí Tardis, protože chceš být sám")

    volba = input("Zadej číslo pro směr, kterým chceš pokračovat:")

    if volba == "1":
        openclose()
       
        najitTardis()
        

    elif volba == "2":
        zustanivtardis()

    else:
        neplatnahodnota()
        start()

def najitTardis():
    print("Nezbývá ti nic, než se pokusit najít Tardis pomocí mrtvých Dáleků.")
    print("Jak se zachováš?")
    print("1. Vyrobíš si loď z mrtvých Dáleků a budeš Tardis pronásledovat")
    print("2. Neuděláš nic a zůstaneš sám na planetě navždy")
    volba2 = input("Pro co se rozhodneš?:")

    if volba2 == "1":
        pronasledovat()
        
    elif volba2 == "2":
        zustanivtardis()
    else:
        neplatnahodnota()

def pronasledovat():
    print("Úspěšně jsi vyrobil loď a začal jsi Tardis pronásledovat")
    print("Blížíš se k planetě Burundy a vidíš že řidič Tardis nad ní ztrácí kontrolu a řítí se směrem k zemi.")
    print("Tardis se zřítila a vidíš, jak z ní kdosi vylézá, zaparkoval si svojí loď a jdeš se podívat.")
    print("Je to určitě Vládce, protože Páni času se vždy cítí, když jsou u sebe blízko")
    print("Jak se zachováš?")
    print("1. Poběžíš k němu ho pozdravit a řict mu, že jsi také Pán času. ")
    print("2. Ukradneš Tardis nazpět a uletíš mu.")
    volba3 = input("Pro co se rozhodneš?:")


    if volba3 == "1":
        pozdraveni()
        
     
        
    elif volba3 == "2":
        uletel()
        
      
def uletel():
    print("Uletěl jsi Vládci, a jelikož jsis vzal klíčky od své lodi vyrobené z Dáleků, Vládce se nemůže dostat z planety pryč.")
    print("Vládce umřel na vyhladovění, protože planeta Burundy je jen poušť")
    print("I když si Vládce našel, tak si ho nakonec zabil, kvůli tomu se tvůj úkol považuje za neúspěch.")
    odznova2 = input("Chceš si zahrát znovu?[ANO]/[NE]")
    if odznova2 == "ano":
            start()
    else:
            print("KONEC")
def pozdraveni():
       print("Šel jsi Vládce pozdravit")
       print("Oba jste byli velmi štastní, že vidíte dalšího Pana času")
       print("Odletěli jste spolu v Tardis a žili jste spolu šťastně až do smrti")
       odznova3 = input("Chceš si zahrát znovu?[ANO]/[NE]")
       if odznova3 == "ano":
            start()
       else:
            print("KONEC")
    

def openclose():
    print("Dorazil jsi na planetu Minoris ve svojí Tardis, vystoupil jsi a vidíš, že je všude mrtvo")
    print("Necháš svůj stroj času odemčený nebo ho zamkneš?")
    print("1. Nechám ji odemčenou.")
    print("2. Nechám ji zamčenou")
    volba1 = input("Pro co se rozhodneš?:")

    if volba1 == "1":
            odemcena()
    elif volba1 == "2":
        zamcena()
        
    else:
        neplatnahodnota()
def odemcena():
    print("Nechal jsi svoji TARDIS odemčenou, a když ses od ní vzdaloval, někdo k ní přiběhl a ukradl ti ji.")
    print("Nikdo jiný než Páni času s TARDIS létat neumí, musí to být Vládce!")
def zamcena():
    print("Zamkl jsi svoji TARDIS, a když ses od ní vzdaloval, někdo k ní přiběhl, otevřel ji kouzelným klíčem a ukradl ti ji.")
    print("Nikdo jiný než Páni času kouzelný klíč nemají, musí to být Vládce!")


def zustanivtardis():
    print("Doktor umřel sám ve věku 1360 let.")
    odznova = input("Chceš začít odznova?[ANO]/[NE]")
    if odznova == "ano":
        start()
    else:
        print("KONEC")
def neplatnahodnota():
    print("neplatná hodnota, prosím začněte odznovu")
    time.sleep(2)
    start()

start()