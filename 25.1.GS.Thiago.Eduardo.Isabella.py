tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []

criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

qtd = int(input("Insira a quantidade de desastres registrados: "))

for i in range(qtd):
  print(f"\n Desastre {i+1}")
    
  tipos_desastres.append(input("Tipo de desastre: "))
  paises.append(input("País: "))
  cidades.append(input("Cidade: "))
  bairros.append(input("Bairro: "))
  ruas.append(input("Rua: "))



while True:
  total = int(input("Total de Afetados: "))
  crianca = int(input("Numero de Crinças Afetadas: "))
  adulto = int(input("Numero de Adultos Afetadas: "))
  idoso =  int(input("Numero de Idosos Afetados: "))
  mobilidade_red = int(input("Numero de Pessoas com Mobilidade Reduzida: "))
  ferido = int(input("Numero de feridos: "))

  soma = crianca + adulto + idoso + mobilidade_red + ferido

 

  if soma == total:
    total_afetados.append(total)
    criancas.append(crianca)
    adultos.append(adulto)
    idosos.append(idoso)
    mobilidade_reduzida.append(mobilidade_red)
    feridos.append(ferido)
    break
  else:
    print("A soma das categorias nao bateram , Tente Novamente Por Favor ")
