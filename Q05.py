texto_salto = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
saltos_do_atleta = [0.0, 0.0, 0.0, 0.0, 0.0]
melhor_salto = pior_salto = media_saltos = 0
atleta = input("Atleta: ")

if atleta != '':
    for c in range(0, 5):
        saltos_do_atleta[c] = float(input(f"{texto_salto[c]} salto: "))

    saltos_do_atleta.sort()
    melhor_salto = max(saltos_do_atleta)
    pior_salto   = min(saltos_do_atleta)
    media_saltos = (saltos_do_atleta[1] + saltos_do_atleta[2] + saltos_do_atleta[3])/3    

    # Exibindo os resultados
    print("="*30)
    print(f"Melhor salto............: {melhor_salto}")
    print(f"Pior salto..............: {pior_salto}")
    print(f"Media dos demais saltos.: {media_saltos:.2f}\n")
    print("Resultado final: ")
    print(f"{atleta}: {media_saltos:.2f}")
else:
    print('Informe o nome do atleta') 
 
atletas = []
while True:
    nome = input(
        "Digite o nome do atleta (ou enter para encerrar o programa): ")
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhor_salto": 0,
        "pior_salto": 0,
    }
    for i in range(5):
        atleta.get("saltos").append(
            float(input(f"Distância do {i+1}º salto: "))
        )
    atleta.get("saltos").sort()  # ? Ordena a lista
    atleta["pior_salto"] = atleta.get("saltos").pop(0)
    atleta["melhor_salto"] = atleta.get("saltos").pop()
    atleta["media"] = sum(atleta.get("saltos")) / 3
    print(
        f"\nMelhor salto: {atleta.get('melhor_salto'):.1f} m"
        f"\nPior salto: {atleta.get('pior_salto'):.1f} m"
        f"\nMédia dos demais saltos: {atleta.get('media'):.1f} m\n"
    )
    atletas.append(atleta)

print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")