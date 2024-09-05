import json


faturamento_json = '''
{
    "faturamento_diario": [0, 100, 200, 150, 0, 300, 400, 0, 500, 0, 0, 600, 700, 0]
}
'''


data = json.loads(faturamento_json)

def calcular_faturamento(data):
    
    faturamento = [dia for dia in data['faturamento_diario'] if dia > 0]
    
  
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    
    
    media_mensal = sum(faturamento) / len(faturamento)
    
  
    dias_acima_media = len([dia for dia in faturamento if dia > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_media


menor, maior, dias_acima_media = calcular_faturamento(data)


print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")

