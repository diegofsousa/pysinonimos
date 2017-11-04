# pysinonimos

> Buscador de sinônimos para palavras em português brasileiro escrito em Python.

[![PyPI version](https://badge.fury.io/py/pysinonimos.svg)](https://badge.fury.io/py/pysinonimos)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Instalação:

```pip install pysinonimos```

## Exemplos:

```
>>> from pysinonimos.sinonimos import Search, historic

>>> apresentacao = Search("apresentação")
>>> sinonimos_de_apresentacao = apresentacao.synonyms()
>>> print(sinonimos_de_apresentacao)
['ida', 'vinda', 'aparição', 'aparecimento', 'surgimento', 'presença', 'comparecimento', 'forma',
'conformação', 'imagem', 'porte', 'formato', 'configuração', 'feitio', 'talhe', 'fisionomia',
'figura', 'aspecto', 'aparência', 'adução', 'manifestação', 'exposição', 'alegação', 'declaração',
'relato', 'comunicação', 'propaganda', 'difusão', 'divulgação', 'veiculação', 'abonação', 'indicação',
'proposição', 'proposta', 'sugestão', 'recomendação', 'sessão', 'atuação', 'show', 'exibição',
'espetáculo', 'mostra', 'demonstração', 'função', 'produção', 'introdução', 'anteâmbulo', 'prolusão',
'prólogo', 'prefácio', 'preâmbulo']

>>> historico = historic()
>>> print(historico)

4 resultados encontrados para 'avião':
['aeronave', 'aeronave', 'aeroplano', 'aparelho']

51 resultados encontrados para 'apresentação':
['ida', 'vinda', 'aparição', 'aparecimento', 'surgimento', 'presença', 'comparecimento', 'forma',
'conformação', 'imagem', 'porte', 'formato', 'configuração', 'feitio', 'talhe', 'fisionomia',
'figura', 'aspecto', 'aparência', 'adução', 'manifestação', 'exposição', 'alegação', 'declaração',
'relato', 'comunicação', 'propaganda', 'difusão', 'divulgação', 'veiculação', 'abonação', 'indicação',
'proposição', 'proposta', 'sugestão', 'recomendação', 'sessão', 'atuação', 'show', 'exibição',
'espetáculo', 'mostra', 'demonstração', 'função', 'produção', 'introdução', 'anteâmbulo', 'prolusão',
'prólogo', 'prefácio', 'preâmbulo']
```

## Créditos:

> Diego Fernando
