def process(INDICE: int, SOMA: int, k: int) -> int:
    while k < INDICE:
        k = k + 1
        SOMA = SOMA + k
    return SOMA

#print(process(13, 0, 0)) # SOMA = 91


def fibonacci(n: int) -> int:
   x = 0
   y = 1
   fib = y
   while fib < n:
       fib = x + y
       x =  y
       y = fib   
   return fib == n 
#print(fibonacci(4))



    
def read_file():
    import json
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for row in data:
           
            valores = float(row["valor"])
            
        min_value = (min(valores))
        max_value = max(valores)
        print('b',min_value)
        
print(read_file())  
        
            
            
        
        
           
            
    
            

def revert_string(string):
    return string[::-1]
print(revert_string('teste'))






    
        
