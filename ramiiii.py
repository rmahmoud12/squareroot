

def calculate_area(t1,t2,t3): 
    s=(t1+t2+t3)/2 
    HeronArea= (s*(s-t1)*(s-t2)*(s-t3))**0.5 
    return HeronArea

def main():
    hn= int(input("How Many Triangles are there: ")) 

    for i in range(hn) : 
        print("Triangle Number#",(i+1)) 
        t1=float(input("enter side(1) : ")) 
        t2= float(input("enter side(2) : ")) 
        t3= float(input("enter side(3) : ")) 
        HeronArea= calculate_area(t1,t2,t3) 
        sumarea= (t1+t2+t3)
        print("the max area is : ",sumarea)
        print("Total area of the triangle would be : ",HeronArea)
      

main()
    
