def maioresIguaisA10(x):
    if (x < 10):
        return x
        
    
    else:
        print(x)
        maioresIguaisA10(x - 1)

maioresIguaisA10(23)