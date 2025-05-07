'''
Crie um programa que 
faça uma contagem regressiva de 5 até 1 usando while, e exiba “Lançar!” no final.
'''
def surpresa():
    num = 5
    while num >= 1:
        print(f"{num}...")
        input("Aperte Enter!")
        num -= 1
    input("Uau, você foi rápida!!")
    input("Sabe qual é a surpresa?")
    input("VOCÊ VAI SE SURPREENDER")
    input("QUASE LÁÁÁÁ...")
    print("Lançar! AHAHA VOCÊ FOI MUITO OTÁRIO AKAKAKAKAK ")

surpresa()