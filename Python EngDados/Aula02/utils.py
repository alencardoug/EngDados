import re

def get_employee_name():
    while True:
        name = input("Digite o nome do funcionário: ").strip()
        if not name:
            print("❌ O nome não pode ficar vazio. Tente novamente.")
            continue
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", name):
            print("❌ Nome inválido: só são permitidas letras e espaços. Tente novamente.")
            continue
        return name

def get_salary():
    while True:
        s = input("Digite o salário do funcionário (apenas números): ").strip()
        try:
            salary = float(s)
            if salary < 0:
                print("❌ O salário não pode ser negativo. Tente novamente.")
                continue
            return salary
        except ValueError:
            print("❌ Valor inválido: use apenas dígitos (ponto para decimais). Tente novamente.")

def calculate_bonus(salary):
    if salary > 15000:
        pct = 0.20
    elif salary >= 10000:
        pct = 0.30
    else:
        pct = 0.40
    return salary * pct, pct
