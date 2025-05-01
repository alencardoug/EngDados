import re

def get_employee_name():
    """
    Lê e valida o nome do funcionário.
    Rejeita entradas vazias, com dígitos ou caracteres não alfabéticos (exceto espaços e acentuação).
    """
    while True:
        name = input("Digite o nome do funcionário: ").strip()
        if not name:
            print("❌ O nome não pode ficar vazio. Tente novamente.")
            continue
        # Aceita letras (incluindo acentos) e espaços
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", name):
            print("❌ Nome inválido: só são permitidas letras e espaços. Tente novamente.")
            continue
        return name

def get_salary():
    """
    Lê e valida o salário.
    Rejeita entradas que não sejam números ou que sejam negativas.
    """
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
    """
    Retorna o valor do bônus e a porcentagem aplicada,
    de acordo com a faixa salarial:
      • > 15000 → 20%
      • 10000–15000 → 30%
      • < 10000 → 40%
    """
    if salary > 15000:
        pct = 0.20
    elif salary >= 10000:
        pct = 0.30
    else:
        pct = 0.40
    return salary * pct, pct

def main():
    nome = get_employee_name()
    salario = get_salary()
    bonus, pct = calculate_bonus(salario)
    
    print("\n--- Resultado ---")
    print(f"Funcionário: {nome}")
    print(f"Salário:      R$ {salario:,.2f}")
    print(f"Bônus:        R$ {bonus:,.2f} ({int(pct*100)}%)")

if __name__ == "__main__":
    main()