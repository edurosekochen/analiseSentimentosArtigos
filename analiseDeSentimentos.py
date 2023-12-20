import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Função para realizar a análise de sentimento de um artigo
def analisar_sentimento(url):
    # Realiza uma solicitação HTTP para obter o conteúdo do artigo
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parseia o conteúdo HTML da página usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra o conteúdo do artigo com base na classe CSS
        conteudo_artigo = soup.find('div', class_='td-post-content tagdiv-type')

        if conteudo_artigo:
            # Obtém o texto do artigo
            texto_artigo = conteudo_artigo.get_text()

            # Realiza a análise de sentimento
            sentimento_artigo = TextBlob(texto_artigo)

            # Classifica o sentimento com base na polaridade
            if sentimento_artigo.sentiment.polarity > 0:
                sentimento = "positivo"
            elif sentimento_artigo.sentiment.polarity < 0:
                sentimento = "negativo"
            else:
                sentimento = "neutro"

            # Exibe o resultado da análise de sentimento
            print("Análise de Sentimento do Artigo:")
            print("Sentimento:", sentimento)
            print("Polaridade:", sentimento_artigo.sentiment.polarity)
        else:
            print("Conteúdo do artigo não encontrado.")
    else:
        print("Falha ao fazer a solicitação HTTP.")

# URLs dos artigos
urls = [
    'https://ricaperrone.com.br/um-inter-campeao-desmonta-teses/',
    'https://ricaperrone.com.br/10-anos-no-rio/',
    'https://ricaperrone.com.br/o-cone-sem-clone/',
    'https://ricaperrone.com.br/memoravel-jogo-ruim/',
    'https://ricaperrone.com.br/o-que-o-tempo-nao-pode-apagar/',
    'https://ricaperrone.com.br/ouvi-falar-muito-de-voce-roberto/',
    'https://ricaperrone.com.br/o-gremio-do-renato-nao-ganha-de-ninguem/'
]

# Itera por cada URL e realiza a análise de sentimento
for url in urls:
    print("\nAnalisando artigo:", url)
    analisar_sentimento(url)
