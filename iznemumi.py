'''
def divide_numbers():
    try:
        num1=float(input("Ievadiet pirmo skaitli: "))
        num2=float(input("Ievadiet pirmo skaitli: "))
        result=num1 / num2
        print(f"Rezultāts: {result}")
    except ZeroDivisionError:
        print("Kļūda: Dalīšana ar nulli nav atļauta.")
    except ValueError:
        print("Kļūda:Ievadiet, derīgus skaitļus.")
    except Exception as e :
        print(f"Radās neparedzēta kļūda : {e}")
    finally:
        #Izpildās neatkarīgi no kļūdām 
        print("Darbība pabeigta.")
    
divide_numbers()

'''

def read_file():
    try:
        filename=input("Ievadiet faila nosaukumu: ")
        with open(filename,'r') as file :
            #ja fails tiek veiksmīgi atvērts,izdrukājam tā saturu
            content= file.read()
            print("Faila saturs: ")
            print(content)
        #ja fails tiek neveiksmīgi atvērts
    except FileNotFoundError:
        #fails netiek atrasts
        print(f"Nepareizs nosaukums ,tādu failu {filename} nevaram atrast")
    except PermissionError:
        # ja nav piekļuves tiesību failam
        print(f"Kļūda: Nav piekļuves tiesību failam '{filename}'")
    except Exception as e :
        #Vispārējo kļūdu apstrāde,ja rodas cita veida kļūdas
        print(f"Radās neparedzēta kļūda : {e}")     
    
    
    finally:
        #Izpildās neatkarīgi no kļūdām 
        print("Darbība pabeigta.")

read_file()