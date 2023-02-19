class Find():
    def __init__(self, name, grad, fine) -> None:
        self.name = name 
        self.n_sub = grad
        self.grad = grad[fine]
        self.fine = fine
    
    def sole(self):
        x = self.grad
        if x == 4 :
            return "A"
        elif x == 3.5 :
            return "B+"
        elif x == 3 :
            return "B"
        elif x == 2.5 :
            return "C+"
        elif x == 2 :
            return "C"
        elif x == 1.5 :
            return "D+"
        elif x == 1 :
            return "D"
        
    def __str__(self) -> str:
        return f"{self.name} {self.fine} is {self.sole()} "
    

if __name__ == "__main__":
    z = input("enter A-E : ")
    x = input("enter name_sub : ")

    st_name = {
        "A":{"eng":3.5,"math":2,"pro":2.5},
        "B":{"eng":2,"math":3,"pro":3},
        "C":{"eng":4,"math":1,"pro":1.5},
        "D":{"eng":3,"math":2.5,"pro":2},
        "E":{"eng":1,"math":2,"pro":4}
        }

    i = Find(z,st_name[z],x)
    print(i)


