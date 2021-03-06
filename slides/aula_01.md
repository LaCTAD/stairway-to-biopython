# Introdução

.footer: <span class=left>Felipe Bidu – felipe@felipevr.com</span> <span class=right><a href=https://github.com/fbidu>github.com/fbidu</a></span>

---

# Oi, eu sou o Bidu

- felipe@felipevr.com
- [github.com/fbidu](https://github.com/fbidu)
- Ciência da Computação – UNICAMP
- Arquiteto de Infraestrutura no [Poppin](https://poppin.app/)

---

# Python

- Permite que você foque mais no seu problema do que em detalhes de código
- Amplo suporte de bibliotecas para as mais diversas funções
- Comunidade de desenvolvedores bastante ativa
- Diversas conferências legais

---

# Mas, Python não é mais lento que [C/PERL/FORTRAN/Java/...]?

.fx: interlude

---

# É difícil comparar de forma justa linguagens diferentes

.fx: interlude

---

## É difícil comparar de forma justa linguagens diferentes
1. Qual algoritmo sendo testado?

---

## É difícil comparar de forma justa linguagens diferentes

1. Qual algoritmo sendo testado?
2. Ele é mais intensivo em uso de CPU, de RAM ou de I/O?

---

## É difícil comparar de forma justa linguagens diferentes

1. Qual algoritmo sendo testado?
2. Ele é mais intensivo em uso de CPU, de RAM ou de I/O?
3. Qual a proficiência do desenvolvedor em escrever na linguagem X e na Y?

---

# Eficiência de projeto é diferente de eficiência de código!

.fx: interlude

---

# Imprimindo `"hello, world"` através de concatenação de strings

.fx: interlude

---

# Em C

    !C
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    int main() {
        char* x = strdup("hello");
        char* y = strdup(" world");
        char* z = (char*)malloc(strlen(x) + strlen(y) + 1);
        strcpy(z, x);
        strcat(z, y);
        printf(z);
        printf("\n");
        free(x);
        free(y);
        free(z);
        return 0;
    }

---

## Em Python

    !python
    x = "hello"
    y = " world"
    z = x + y
    print(z)

---

## Qual seu objetivo com programação?

1. Escrever código?
2. Analisar um conjunto de informações e chegar num resultado?

---

## Analisando Dados

Suponha um cenário hipotético em que em C seu código demoraria 24h
para executar e, em Python, uma semana

---

## Analisando Dados

...mas o código em C levaria 1 mês para ser escrito e corrigido. O código
em Python, 2 dias

---

## Analisando Dados

No fim das contas, para você ir do 0 até os seus resultados, C custou
pouco mais de 1 mês

---

## Analisando Dados

Python levou 8 dias.

---

# Eficiência de projeto é diferente de eficiência de código!

.fx: interlude

---

## Analisando Dados

P.S.: Dados hipotéticos mas bastante embasados na minha experiência com
projetos assim!

---

# Jupyter

1. [Jupyter](https://jupyter.org/)
2. [Challenges in irreproducible research](https://www.nature.com/collections/prbfkwmwvz)
3. [AAAS: Machine learning 'causing science crisis'](https://www.bbc.com/news/science-environment-47267081)
4. [Nuvem dos Candidatos](https://nbviewer.jupyter.org/github/fbidu/nuvem-candidatos/blob/master/passo_a_passo.ipynb)
5. [Jupyter Paper Template](https://github.com/pinga-lab/paper-template)
6. [10 Simple Rules](https://arxiv.org/pdf/1810.08055.pdf)
7. [Installing Jupyter](https://jupyter.readthedocs.io/en/latest/install.html)

---

# Obrigado!
