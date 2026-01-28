inp = int(input())
l1 = [1,2,3]
for num in l1:
    if inp == num:
        print( "V")
    else:    
        if inp % 3 == 0 and inp % 2 == 0 :
            print("x")
        else:
            print("v")
    
        