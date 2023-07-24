data_usuario = input("Informe uma data a partir de 1500 (dd/mm/aaaa): ")

#divisao das informacoes
dia, mes, ano = data_usuario.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)

#valor do ano
ultimos_digitos_ano = ano % 100

if ultimos_digitos_ano <= 3:
    valor_ano_final = ultimos_digitos_ano

else: 
    valor_ano_cheio = (ultimos_digitos_ano // 4) + (ultimos_digitos_ano - ((ultimos_digitos_ano // 7) * 7))
    valor_ano_final = (valor_ano_cheio - ((valor_ano_cheio // 7) *7))

#valor do mes
if mes == 1: 
    valor_mes = 1
if mes == 2: 
    valor_mes = 4
if mes == 3: 
    valor_mes = 4
if mes == 4: 
    valor_mes = 0
if mes == 5: 
    valor_mes = 2
if mes == 6: 
    valor_mes = 5
if mes == 7: 
    valor_mes = 0
if mes == 8: 
    valor_mes = 3
if mes == 9: 
    valor_mes = 6
if mes == 10: 
    valor_mes = 1
if mes == 11: 
    valor_mes = 4
if mes == 12: 
    valor_mes = 6

#seculo
ano_string = str(ano)
primeiros_algarismos_ano = ano_string[:2]
seculo = int(primeiros_algarismos_ano) + 1

if (seculo - ((seculo // 4) *4)) == 0: 
    valor_seculo = 0
elif (seculo - ((seculo // 4) *4)) == 1: 
    valor_seculo = 6
elif (seculo - ((seculo // 4) *4)) == 2: 
    valor_seculo = 4
elif (seculo - ((seculo // 4) *4)) == 3: 
    valor_seculo = 2

#valida bissexto
def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#calculo
soma_valores = (dia + valor_mes + valor_ano_final + valor_seculo)
if eh_bissexto(ano):
    soma_valores = (soma_valores - 1)

dia_semana = (soma_valores - ((soma_valores // 7) * 7))

#print dia da semana
if dia_semana == 0:
    print("O dia {} é um sábado".format (data_usuario))
if dia_semana == 1:
    print("O dia {} é um domingo".format (data_usuario))
if dia_semana == 2:
    print("O dia {} é uma segunda-feira".format (data_usuario))
if dia_semana == 3:
    print("O dia {} é uma terça-feira".format (data_usuario))
if dia_semana == 4:
    print("O dia {} é uma quarta-feira".format (data_usuario))
if dia_semana == 5:
    print("O dia {} é uma quinta-feira".format (data_usuario))
if dia_semana == 6:
    print("O dia {} é uma sexta-feira".format (data_usuario))
