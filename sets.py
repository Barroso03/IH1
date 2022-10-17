import random


  

def sets():
    sample_list_1= []
    sample_list_1= random.sample(range(0,100),80)
    print("sample_list_1:",sample_list_1)
    print("El tipo es:",type(sample_list_1))
    
    set1= set(sample_list_1)
    print("set1:",set1)
    
    
    print("La longitud del set1 es:",len(set1))
    
    if len(set1)==80:
        print("La longitud  sigue siendo 80")
    else:
        print("La longitud no es 80")
    sample_list_2= []
    
    sample_list_2= random.sample(range(0,100),79)
    sample_list_2.append(80)
    print("sample_list_2:",sample_list_2)
    set2 = set(sample_list_2)
    print("set2:",set2)
    print("La longitud del set2 es:",len(set2))
    if len(set2)==80:
        print("La longitud sigue siendo 80")
    else:
        print("La longitud no es 80")
    
    set3=[]
    for i in set1:  
        if i not in set2:
            set3.append(i)
    print("set3:",set3)
    set4=[]
    for i in set2:
        if i not in set1:
            set4.append(i)
    print("set4:",set4)
    
    set5=[]
    for i in set1:
        if i in set2:
            set5.append(i)
    print("set5:",set5)
    
    print("La relacion entre len(set1), len(set2), len(set3), len(set4) y len(set5) es:")
    print("len(set1)=len(set2)")
    print("len(set4)=len(set3)=len(set1)-len(set2)")
    print("len(set5)=len(set4)+len(set3)")
    set6=[]
    
    set6=set3+set5
    print("set6:",set6)
    
    if set1==set6:
        print("set1 y set6 son iguales")
    else:
        print("set1 y set6 no son iguales")
    
    if set2.issubset(set1):
        print("set2 esta contenido en set1")
    else:
        print("set2 no esta contenido en set1")
   
    if set(set3).issubset(set1):
        print("set3 esta contenido en set1")
    else:
        print("set3 no esta contenido en set1")
    
    set7=set1.union(set2)
    print("set7:",set7)
    
    set8=set3+set4+set5
    print("set8:",set8)
    
    if set7==set8:
        print("set7 y set8 son iguales")
    else:
        print("set7 y set8 no son iguales")
   
    set1.pop()
    print("set1 sin el primer elemento:",set1)
    
    list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
    for i in list_to_remove:
        if i in set1:
            set1.remove(i)
    print("set1 sin los valores de list_to_remove:",set1)
sets()

