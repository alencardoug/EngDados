# Import relativo: sobe um nível (.) para o pacote `utils`

from .utils.validators import get_employee_name, get_salary

# Como descrito, com a configuração no __init.py__ o from pode ser apenas .utils
# from .utils import get_employee_name, get_salary
# mas não funcionou a linha acima

def calculate_bonus(salary):
    if salary > 15000:
        pct = 0.20
    elif salary >= 10000:
        pct = 0.30
    else:
        pct = 0.40
    return salary * pct, pct

def main():
    nome = get_employee_name()
    salario = get_employee_name() if False else get_salary()  # só um exemplo de chamada
    bonus, pct = calculate_bonus(salario)

    print(f"\nFuncionário: {nome}")
    print(f"Salário:     R$ {salario:,.2f}")
    print(f"Bônus:       R$ {bonus:,.2f} ({int(pct*100)}%)")

if __name__ == "__main__":
    main()
