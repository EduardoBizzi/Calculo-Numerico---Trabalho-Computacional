🧮 Métodos Numéricos – Cálculo de Raízes

Este projeto implementa os principais métodos numéricos para aproximação de raízes de funções reais.
O programa lê os parâmetros de um arquivo de entrada, executa os métodos e exibe os resultados formatados no terminal e em um arquivo de saída.

📚 Métodos Implementados

O programa contém cinco métodos clássicos de cálculo de raízes:

Método	Descrição
Bisseção	Divide repetidamente o intervalo ao meio até encontrar a raiz com a precisão desejada.
Ponto Fixo (MIL)	Utiliza uma função equivalente 
𝑔
(
𝑥
)
g(x) para aproximar a raiz a partir de um valor inicial.
Newton-Raphson	Usa a derivada da função para encontrar a raiz com convergência rápida.
Secante	Similar a Newton, mas dispensa o uso da derivada.
Regula Falsi	Método iterativo que combina Bisseção e Secante, garantindo convergência.
⚙️ Estrutura do Projeto
📂 Trabalho-CalculoNumerico/
├── main.py              # Código principal com todos os métodos
├── entrada.txt          # Arquivo de entrada com os parâmetros e funções
├── saida.txt            # Gerado automaticamente com os resultados
└── README.md            # Este arquivo

📥 Formato do Arquivo de Entrada

O programa lê um arquivo chamado entrada.txt com os parâmetros separados por ponto e vírgula ;, na seguinte ordem:

a;b;delta;n;f(x);g(x)

📘 Exemplo:
0;1;0.0001;50;x**3 - 9*x + 3;(9*x - 3)**(1/3)


a, b: intervalo inicial

delta: tolerância (erro máximo)

n: número máximo de iterações

f(x): função principal

g(x): função equivalente (apenas usada no método do ponto fixo)

▶️ Como Executar

Instale as dependências:

pip install sympy colorama


Coloque o arquivo entrada.txt no mesmo diretório do código.

Execute o programa:

python main.py


O programa:

Mostrará os resultados no terminal (coloridos).

Gerará automaticamente o arquivo saida.txt com todas as iterações e raízes aproximadas.

💾 Exemplo de Saída no Terminal
===== Bissecao =====
Iter    Valores...
1       0.0     1.0     0.5     -1.375
2       0.0     0.5     0.25    0.765625
...
→ Raiz aproximada: 0.33789062


E o arquivo saida.txt conterá todas as tabelas de iterações para cada método.

🧠 Bibliotecas Utilizadas
Biblioteca	Função
math	Operações matemáticas básicas
sympy	Cálculo simbólico e derivadas
colorama	Cores no terminal (formatação visual)
🧩 Organização Interna do Código

print_header, print_table_header, print_row: funções auxiliares de formatação

funcao(): converte a expressão matemática em função real

lerArquivos(): lê a entrada

salvar_resultados(): gera o arquivo de saída

Cada método (Bissecao, MIL, Newton, Secante, Regula_falsi) retorna:

A raiz aproximada

Uma lista de iterações com os valores intermediários

✅ Exemplo de Execução Completa
Entrada:
0;1;0.0001;50;x**3 - 9*x + 3;(9*x - 3)**(1/3)

Saída (saida.txt):
===== Bissecao =====
Iter    Valores...
1   0.0 1.0 0.5 -1.375
2   0.0 0.5 0.25 0.765625
...
Raiz aproximada: 0.337890625

===== Newton-Raphson =====
Iter    Valores...
0   0.5 0.341269841  -1.375
...
Raiz aproximada: 0.337928728

✨ Autor

Eduardo Barbero Bizzi Rodrigues
Curso: Ciência da Computação – 4º Período
Disciplina: Cálculo Numérico
