import requests
from scrapy.selector import Selector as scp
import sys
from unicodedata import normalize

class Search(object):
	"""docstring for Search"""
	def __init__(self, palavra):
		super(Search, self).__init__()
		self.word = palavra.split(" ")

	def synonyms(self, verbose=False):
		param = "-".join(self.word)
		param = normalize('NFKD', param).encode('ASCII','ignore').decode('ASCII')
		if verbose == True:
			print("Carregando sinônimos para '{}'...".format(param))
			try:
				r = requests.get('https://www.sinonimos.com.br/{}/'.format(param))
				print(r)
				if r.status_code == 200:
					conteudo = r.content.decode('iso8859-1')
					palavra = scp(text=conteudo).xpath('//h1[@class="h-palavra"]/text()').extract_first()[12:]
					sinonimos = scp(text=conteudo).xpath('//a[@class="sinonimo"]/text()').extract()
					tam_sinonimos = len(sinonimos)

					#print("{} resultados encontrados:".format(tam_sinonimos))
					
					arq = open('.historico', 'a')
					arq.write("{} resultados encontrados para '{}':\n".format(tam_sinonimos, palavra))
					arq.write(str(sinonimos))
					arq.write("\n\n")
					arq.close()
					print("Pronto!")
					return sinonimos
				else:
					return "Nenhum resultado encontrado."
			except Exception as e:
				return "Impossivel conectar a internet. :/. Tipo de erro: {}".format(e)
		else:
			try:
				r = requests.get('https://www.sinonimos.com.br/{}/'.format(param))
				if r.status_code == 200:
					conteudo = r.content.decode('iso8859-1')
					palavra = scp(text=conteudo).xpath('//h1[@class="h-palavra"]/text()').extract_first()[12:]
					sinonimos = scp(text=conteudo).xpath('//a[@class="sinonimo"]/text()').extract()
					tam_sinonimos = len(sinonimos)
					arq = open('.historico', 'a')
					arq.write("{} resultados encontrados para '{}':\n".format(tam_sinonimos, palavra))
					arq.write(str(sinonimos))
					arq.write("\n\n")
					arq.close()
					return sinonimos
				else:
					return r.status_code
			except Exception as e:
				return e

def about():
	return "Bem-vindo ao pysinonimos!\nPara usar execute: python pysinonimos.py 'palavra'"

def historic(delete=False):
	try:
		if delete == True:
			arq = open('.historico', 'w')
			arq.write("")
			arq.close()
			print("Histórico apagado.")
		else:
			arq = open('.historico', 'r')
			return arq.read()
			arq.close()
	except Exception as e:
		return "Arquivo ainda não existe."