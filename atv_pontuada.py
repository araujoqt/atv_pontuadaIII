import os
os.system("cls || clear")

def autenticar_usuario():
    while True:
        matricula = input("Digite a matrícula do funcionário: ")
        senha = input("Digite a senha do funcionário: ")
       
        if matricula == "123" and senha == "senha123":
            print("Acesso autorizado!\n")
            break
        else:
            print("Matrícula ou senha incorretos. Tente novamente.\n")


def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09 - 113.85
    elif salario <= 4190.83:
        return salario * 0.12 - 189.54
    elif salario <= 8157.41:
        return salario * 0.14 - 318.38
    else:
        return 1142.04


def calcular_irrf(salario, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario - deducao_dependentes

    if base_calculo <= 2259.20:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00


def calcular_vale_transporte(salario, opta_vale):
    if opta_vale.lower() == 's':
        return salario * 0.06
    else:
        return 0


def calcular_vale_refeicao(valor_refeicao):
    return valor_refeicao * 0.20


def calcular_plano_saude(dependentes):
    return dependentes * 150.00


def main():
    autenticar_usuario()

    salario_base = float(input("Digite o salário base (R$): "))
    opta_vale = input("Deseja receber vale transporte? (s/n): ")
    valor_refeicao = float(input("Informe o valor do vale refeição fornecido (R$): "))
    dependentes = int(input("Informe a quantidade de dependentes: "))

    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
    vt = calcular_vale_transporte(salario_base, opta_vale)
    vr = calcular_vale_refeicao(valor_refeicao)
    plano_saude = calcular_plano_saude(dependentes)

    total_descontos = inss + irrf + vt + vr + plano_saude
    salario_liquido = salario_base - total_descontos

    print("\n--- Folha de Pagamento ---")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vt:.2f}")
    print(f"Desconto Vale Refeição: R$ {vr:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

main()