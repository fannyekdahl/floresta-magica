def le_arquivo(nome):
  fh = open(nome, 'r')
  texto = fh.read()
  fh.close()
  return texto

print(le_arquivo('tela_inicial.txt'))
