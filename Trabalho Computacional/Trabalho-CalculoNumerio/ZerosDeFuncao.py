import math as mt
import sympy as sp
from colorama import Fore, Style, init

init(autoreset=True)

def print_header(title):
    print(f"\n{Fore.CYAN + Style.BRIGHT}===== {title} ====={Style.RESET_ALL}")

def print_table_header(headers):
    print(Fore.YELLOW + "\t".join(headers) + Style.RESET_ALL)

def print_row(row):
    print("\t".join(map(lambda x: f"{x:.6f}" if isinstance(x, float) else str(x), row)))

# --------------------------------------------------------
# MÉTODOS NUMÉRICOS
# --------------------------------------------------------

def Bissecao(a, b, delta, n, exp_str):
    iteracao = []
    count = 0
    if abs(a - b) < delta:
        return a, count
    while abs(a - b) > delta and count < 50:
        count += 1
        meio = (a + b) / 2.0
        fInicio = funcao(a, exp_str)
        fMeio = funcao(meio, exp_str)
        iteracao.append((count, a, b, meio, fMeio))
        if fInicio * fMeio < 0:
            b = meio
        else:
            a = meio
    return meio, iteracao


def MIL(a, delta, n, exp_str, equac_equiv):
    iteracao = []
    count = 0
    while count < n:
        f = funcao(a, exp_str)
        var = funcao(a, equac_equiv)
        iteracao.append((count, a, var, f))
        if abs(f) < delta or abs(var - a) < delta:
            break
        a = var
        count += 1
    return a, iteracao


def Newton(a, delta, n, exp_str):
    iter = []
    x = sp.Symbol('x')
    exp = sp.sympify(exp_str)
    exp_deriv = sp.diff(exp, x)
    f = sp.lambdify(x, exp, 'math')
    f_linha = sp.lambdify(x, exp_deriv, 'math')
    count = 0
    while count < n:
        fa = f(a)
        fpa = f_linha(a)
        if fpa == 0:
            break
        novo = a - fa / fpa
        iter.append((count, a, novo, fa))
        if abs(novo - a) < delta or abs(fa) < delta:
            break
        a = novo
        count += 1
    return a, iter


def Secante(a, b, delta, n, exp_str):
    iteracoes = []
    f = lambda x: funcao(x, exp_str)
    count = 0
    while count < n:
        fa, fb = f(a), f(b)
        if fb - fa == 0:
            break
        var = b - (fb * (b - a)) / (fb - fa)
        iteracoes.append((count, a, b, var, f(var)))
        if abs(var - b) < delta or abs(f(var)) < delta:
            break
        a, b = b, var
        count += 1
    return a, iteracoes


def Regula_falsi(a, b, delta, n, exp_str):
    iteracoes = []
    f = lambda x: funcao(x, exp_str)
    fa, fb = f(a), f(b)
    count = 0
    while count < n:
        try:
            var = (a * fb - b * fa) / (fb - fa)
            fvar = f(var)
            iteracoes.append((count, a, b, var, fvar))
            if abs(fvar) < delta or abs(b - a) < delta:
                break
            if fa * fvar < 0:
                b = var
                fb = fvar
            else:
                a = var
                fa = fvar
            count += 1
        except ZeroDivisionError:
            print("Divisao por 0 encontrada")
    return var, iteracoes


def funcao(variavel, exp_str):
    x = sp.Symbol('x')
    exp_real = sp.sympify(exp_str)
    funcao_real = sp.lambdify(x, exp_real, 'math')
    return funcao_real(variavel)

# --------------------------------------------------------
# I/O DE ARQUIVOS
# --------------------------------------------------------

def lerArquivos(nomeArquivo):
    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read().strip()
    except FileNotFoundError:
        print(Fore.RED + "❌ ARQUIVO NAO ENCONTRADO")
        return ""


def salvar_resultados(nome_saida, resultados):
    with open(nome_saida, 'w', encoding='utf-8') as f:
        for metodo, dados in resultados.items():
            f.write(f"===== {metodo} =====\n")
            f.write("Iter\tValores...\n")
            for linha in dados[1]:
                f.write("\t".join(map(str, linha)) + "\n")
            f.write(f"\nRaiz aproximada: {dados[0]}\n\n\n")
    print(Fore.GREEN + f"\n💾 Resultados salvos em {nome_saida}\n")

# PROGRAMA PRINCIPAL

def main():
    entrada = lerArquivos(r'c:\Users\Windows 10\Documents\Ciência da Computação\4 período\Calc Num\Trabalho Computacional\Trabalho-CalculoNumerio\entrada.txt')
    if not entrada:
        return

    a, b, delta, n, funcao_str, equac_equiv = entrada.split(";")
    a, b, delta, n = float(a), float(b), float(delta), int(n)

    resultados = {
        "Bissecao": Bissecao(a, b, delta, n, funcao_str),
        "MIL (Ponto Fixo)": MIL(a, delta, n, funcao_str, equac_equiv),
        "Newton-Raphson": Newton(a, delta, n, funcao_str),
        "Secante": Secante(a, b, delta, n, funcao_str),
        "Regula Falsi": Regula_falsi(a, b, delta, n, funcao_str)
    }

    for metodo, dados in resultados.items():
        print_header(metodo)
        print_table_header(["Iter", "Valores..."])
        for linha in dados[1]:
            print_row(linha)
        print(f"{Fore.GREEN}→ Raiz aproximada: {dados[0]:.8f}\n")

    salvar_resultados("saida.txt", resultados)
    print(Fore.CYAN + "✅ Execução concluída com sucesso!\n" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
