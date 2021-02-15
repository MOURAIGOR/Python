from math import sqrt

def bhaskara (a, b, c):
    delta = (b**2) - (4 * a * c)

    if delta > 0:
        x1 =((-b) + sqrt(delta)) / (2 * a)
        x2 =((-b) - sqrt(delta)) / (2 * a)
        print("Os valores é x1 {} e x2 {} " .format (x1 , x2))   
    
    elif delta < 0:
        x = (-b) / 2 * a
        print("Há uma possibilidade de resolução: ", x)
    
    elif delta < 0:
        print ("Não há resolução para raizes negativas")    

bhaskara (1, -5, 6)           

#a = 1, b = -5, c = 6 

#a = 1, b = 0, c = -9 

#a = 5, b = -45, c = 0 

#a = 1, b = -1, c = -12 

#a = 1, b = -6, c = 10 