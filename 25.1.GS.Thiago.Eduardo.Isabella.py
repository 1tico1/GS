# EDUARDO VEIGA RM 561575
# ISABELLA MATTAR RM 562481
# THIAGO ULRYCH RM565929

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


print(f"\nTotal de desastres registrados: {qtd}")

total_criancas = 0
total_adultos = 0
total_idosos = 0
total_mob = 0
total_feridos = 0
total_geral = 0

for i in range(qtd):
    total_criancas += criancas[i]
    total_adultos += adultos[i]
    total_idosos += idosos[i]
    total_mob += mobilidade_reduzida[i]
    total_feridos += feridos[i]
    total_geral += total_afetados[i]


categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores = [total_criancas, total_adultos, total_idosos, total_mob, total_feridos]

maior_valor = valores[0]
indice_maior = 0

for i in range(1, len(valores)):
    if valores[i] > maior_valor:
        maior_valor = valores[i]
        indice_maior = i

categoria_mais_afetada = categorias[indice_maior]


maior_afetados = total_afetados[0]
indice_mais_grave = 0

for i in range(1, qtd):
    if total_afetados[i] > maior_afetados:
        maior_afetados = total_afetados[i]
        indice_mais_grave = i


print("\nRelatório Final")

print(f"\nQuantidade Total de Desastres Registrados: {qtd}")

print("\nTotal de pessoas afetadas por categoria:" +
      f"\nCrianças: {total_criancas}" +
      f"\nAdultos: {total_adultos}" +
      f"\nIdosos: {total_idosos}" +
      f"\nMobilidade reduzida: {total_mob}" +
      f"\nFeridos: {total_feridos}")

print(f"\nCategoria mais afetada: {categoria_mais_afetada}")
print(f"Total geral de pessoas afetadas: {total_geral}")

print("\nLocal do desastre mais grave (com maior número de vítimas):" +
      f"\nTipo: {tipos_desastres[indice_mais_grave]}" +
      f"\nRua: {ruas[indice_mais_grave]}" +
      f"\nBairro: {bairros[indice_mais_grave]}" +
      f"\nCidade: {cidades[indice_mais_grave]}" +
      f"\nPaís: {paises[indice_mais_grave]}")
