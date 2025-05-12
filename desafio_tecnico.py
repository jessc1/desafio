def process(INDICE: int, SOMA: int, k: int) -> int:
    while k < INDICE:
        k = k + 1
        SOMA = SOMA + k
    return SOMA

print(process(13, 0, 0)) # SOMA = 91


def fibonacci(n: int) -> int:
   x = 0
   y = 1
   fib = y
   while fib < n:
       fib = x + y
       x =  y
       y = fib   
   return fib == n 
print(fibonacci(4))



    
def read_file() -> str:
    import json
    results = []
    with open('dados.json', 'r') as file:
        data = json.load(file)
        for row in data:
            dias = int(row["dia"])            
            valor = float(row["valor"])
            result = {"dia": dias, "valor": valor}
            results.append(result)
        min_value = min(results, key=lambda data: data['valor'])
        max_value = max(results, key=lambda data: data['valor'])
       
    return f"O mínimo valor é: {min_value['valor']} e o máximo valor é: {max_value['valor']:.2f}"       
       
print(read_file())               

def revert_string(string):
    return string[::-1]
print(revert_string('teste'))






    
        
