import os
import requests

def baixa_arquivo(url, endereco):
    # Faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Salvo em {}".format(endereco))
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    BASE_URL = 'https://www.ime.usp.br/~slago/lp-{}.pdf' # URL do arquivo com um parametro {} que é o número da apostila
    
    OUTPUT_DIR = 'Silvio_LP' # Nome da pasta onde os arquivos serão baixados

    if os.path.exists(OUTPUT_DIR) == False: # cria diretório com o nome da variável para baixar os arquivos caso não exista 
        os.mkdir(OUTPUT_DIR)

    for i in range(1, 14):
        # transforma i em string e adiciona zero a esqueda caso i < 10
        if i < 10:
            a = str(i)
            num = ('0' + a)
        else: 
            num = str(i)

        nome_arquivo = os.path.join(OUTPUT_DIR, 'Aula_Silvio_LP_{}.pdf'.format(num)) 
        baixa_arquivo(BASE_URL.format(num), nome_arquivo)