from bs4 import BeautifulSoup
import csv
import requests

fake_news = {
    ['política']: [
        "https://lupa.uol.com.br/jornalismo/categoria/pol%C3%ADtica",
        "https://politica.estadao.com.br/blogs/estadao-verifica/"
    ],
    ['presidenciáveis']: "https://lupa.uol.com.br/jornalismo/categoria/presidenci%C3%A1veis",
    ['tse']: "https://lupa.uol.com.br/jornalismo/categoria/tse",
    ['livre']: "https://www.aosfatos.org/noticias/checamos/falso/",
    ['ciência']: "https://www.boatos.org/ciencia",
    ['brasil']: "https://www.boatos.org/brasil",
    ['esporte']: "https://www.boatos.org/esporte",
    ['política']: "https://www.boatos.org/politica",
    ['entretenimento']: "https://www.boatos.org/entretenimento",
    ['saúde']: "https://www.boatos.org/saude",
    ['tecnologia']: "https://www.boatos.org/tecnologia",
    ['mundo']: "https://www.boatos.org/mundo",
    ['religião']: "https://www.boatos.org/religiao",
    ['conspiracoes']: "https://www.e-farsas.com/secoes/conspiracoes",
    ['dinheiro']: "https://www.e-farsas.com/secoes/dinheiro"
}

real_news = {
    ['brasil']: [
        "https://www.metropoles.com/brasil",
        "https://www.estadao.com.br/brasil/"
    ],
    ['entretenimento']: "https://www.metropoles.com/entretenimento",
    ['saude']: [
        "https://www.metropoles.com/saude",
        "https://www.estadao.com.br/saude/",
        "https://g1.globo.com/saude/"
    ],
    ['esporte']: "https://www.metropoles.com/esportes",
    ['politica']: [
        "https://www1.folha.uol.com.br/poder/",
        "https://www.estadao.com.br/politica/",
        "https://g1.globo.com/politica/"
    ],
    ['economia']: [
        "https://www1.folha.uol.com.br/mercado/",
        "https://www.estadao.com.br/economia/",
        "https://g1.globo.com/economia/"
    ],
    ['mundo']: [
        "https://www1.folha.uol.com.br/mundo/",
        "https://www.estadao.com.br/brasil/",
        "https://g1.globo.com/mundo/"
    ],
    ['cotidiano']: "https://www1.folha.uol.com.br/cotidiano/",
    ['educacao']: [
        "https://www.estadao.com.br/educacao/",
        "https://g1.globo.com/educacao/"
    ],
    ['cultura']: [
        "https://www1.folha.uol.com.br/ilustrada/",
        "https://www.estadao.com.br/cultura/"
    ],
    ['esporte']: [
        "https://www1.folha.uol.com.br/esporte/",
        "https://esportes.estadao.com.br/"
    ],
    ['ciencia']: "https://g1.globo.com/ciencia/",
    ['tecnologia']: "https://g1.globo.com/tecnologia/"

}

fields = ["Título", "Texto", "Assunto", "Data", "Classificação"]

filename = "fake_and_real_news_data.csv"


with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    for assunto in fake_news:
