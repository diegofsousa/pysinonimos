import requests
from scrapy.selector import Selector as scp
import sys
from unicodedata import normalize

param = "-".join(sys.argv[1:])

def loadingSynonyms():
	try:
		r = requests.get('https://www.sinonimos.com.br/{}/'.format(param))
		if r.status_code == 200:
			conteudo = r.content.decode('iso8859-1')
			palavra = scp(text=conteudo).xpath('//h1[@class="h-palavra"]/text()').extract_first()[12:]
			sinonimos = scp(text=conteudo).xpath('//a[@class="sinonimo"]/text()').extract()
			tam_sinonimos = len(sinonimos)

			print("{} resultados encontrados:".format(tam_sinonimos))
			print(sinonimos)
			arq = open('.historico', 'a')
			arq.write("{} resultados encontrados para '{}':\n".format(tam_sinonimos, palavra))
			arq.write(str(sinonimos))
			arq.write("\n\n")
			arq.close()
		else:
			print("Nenhum resultado encontrado.")
	except Exception as e:
		print("Impossivel conectar a internet. :/. Tipo de erro: {}".format(e))
	

if param == "-h" or param == "-help":
	print("\nBem-vindo ao pysinonimos!")
	print("Para usar execute: python pysinonimos.py 'palavra'")

elif param == "-his" or param == "-history":
	try:
		arq = open('.historico', 'r')
		print("Histórico:")
		print(arq.read())
		arq.close()
	except Exception as e:
		print("Arquivo ainda não existe.")	

elif param == "-del" or param == "-d":
	arq = open('.historico', 'w')
	arq.write("")
	arq.close()
	print("Histórico apagado.")

else:
	param = normalize('NFKD', param).encode('ASCII','ignore').decode('ASCII')
	print("Carregando sinônimos para '{}'...".format(param))
	loadingSynonyms()
