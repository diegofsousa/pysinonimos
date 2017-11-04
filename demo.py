from pysinonimos import Search, about, historic

aviao = Search("avião")
sin_aviao = doce.synonyms(verbose=True)
print(sin_aviao)

apesar = Search("apesar que")
sin_apesar = apesar.synonyms()

print(sin_apesar)

about()
historic()

