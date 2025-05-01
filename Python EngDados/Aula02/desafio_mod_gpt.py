from utils import get_employee_name, get_salary, calculate_bonus

def main():
    nome    = get_employee_name()
    salario = get_salary()
    bonus, pct = calculate_bonus(salario)

    print("\n--- Resultado ---")
    print(f"Funcionário: {nome}")
    print(f"Salário:      R$ {salario:,.2f}")
    print(f"Bônus:        R$ {bonus:,.2f} ({int(pct*100)}%)")

if __name__ == "__main__":
    main()