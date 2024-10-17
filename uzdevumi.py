class Calculator:
    def __init__(self,pirmais,otrais):
        self.pirmais=pirmais
        self.otrais=otrais

    def saskatisana(self):
        s= self.pirmais + self.otrais
        print("Saskaitisanas rezultats",s)
        return s
       
    def atnemsana(self):
        a= self.pirmais - self.otrais
        print("Atnemsanas rezultats",a)
        return a 

    def reizinasana(self):
        r= self.pirmais * self.otrais
        print("Rezinajums ir ",r)
        return r
    
    def dalisana(self):
        try:
            d= self.pirmais / self.otrais
            print("Rezinajums ir ",d)
            return d
        except ZeroDivisionError:
            print("Kļūda: Dalīšana ar nulli nav atļauta.")
        except Exception as e :
            print(f"Radās neparedzēta kļūda : {e}")
        finally:
        #Izpildās neatkarīgi no kļūdām 
            print("Darbība pabeigta.")

def get_valid_number(Calculator):
    while True:
        try:
            return float(input(Calculator))
        except ValueError:
            print("Kļūda :ievadiet derigu skaitli ")
def main():
    print("Laipni lūdzam programmā!")
    #pieprasa lietotajam ievadit divus sk
    num1=get_valid_number("Ievadie pirmo sK:")
    num2=get_valid_number("Ievadie otro sK:")

    calc= Calculator(num1,num2)

    print(f"Saskaitisana: {calc.saskatisana()}")
    print(f"Atnemsana: {calc.atnemsana()}")
    print(f"Reizinasana: {calc.reizinasana()}")
    print(f"Dalisana: {calc.dalisana()}")

main()





'''
p1=Calculator(10,0)
p1.saskatisana()
p1.atnemsana()
p1.reizinasana()
p1.dalisana()
'''

