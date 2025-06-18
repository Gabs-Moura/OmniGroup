import os

# Caminho da pasta onde estão os arquivos .txt (labels)
pasta = '/Users/moura/Projects/OmniGroup/dataset_omni/toddynho/valid/labels' # Altere para o caminho correto

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        novas_linhas = []
        for linha in linhas:
            if linha and linha[0] in '0123456789':
                nova_linha = '6' + linha[1:] # Troca o primeiro caractere para '0', ou seja, trocar o número que precisa
            else:
                nova_linha = linha
            novas_linhas.append(nova_linha)
        
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.writelines(novas_linhas)

print("Todos os arquivos foram processados.")
