try:
    class Calculator:
        def __init__(self,no1,no2):
            self.no1=no1
            self.no2=no2
        def add(self):
            result= self.no1+self.no2
            return result
        def sub(self): 
            result=self.no1-self.no2  
            return result 

          #print(F"this is addition of {self.no1} and {self.no2}=",result)
        def mul(self):
            result=self.no1*self.no2
            return result
            #print(F"This is multiplication of {self.no1} and {self.no2} = ",result) 
        def divi(self):
            result=self.no1%self.no2
            return result
            #print(F"This is division of {self.no1} and {self.no2} = ",result)       
    C1=Calculator(eval(input("Enter any number")),eval(input("Enter any number")))
    print(C1.add())    
    print(C1.sub())
    print(C1.mul())
    print(C1.divi())
except Exception as e:
    print("i don't want to appear any error",e)    