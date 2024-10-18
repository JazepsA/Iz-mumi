class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def perimeter(self):
        p=self.height * 2 + self.width * 2
        print("Perimetrs ir :",p)
        return p
    
    def area(self):
        a=self.height * self.width
        print("Laukums ir :",a)
        return a
 
def parbauda():
    while   True:
        try:
            
                height=int(input("Ievadiet augstumu:"))
                
                width=int(input("Ievadiet platumu:"))
                if  height > 0 or width > 0 :
                    f1=Rectangle(height,width)
                    print(f"Jusu perimetrs ir : {f1.perimeter()} un laukums: {f1.area()} ")
                    break
                else:
                    print("Ievadiet pozitivu sk ")
        except ValueError:
            pass


parbauda()


#def izvada():   
    #print(f"Jusu figuras laukums ir {perimeter()}")




