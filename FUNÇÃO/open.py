# Ao utilizar ‘w’ em um arquivo já existente, ele reescreverá todo o conteúdo do
# arquivo, fazendo com que todos os dados que estavam nele sejam apagados.



arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('# Na função, adicionamos o nome do arquivo e, logo após o símbolo do ponto final, fazemos a chamada da função write. Em seguida, adicionamos o texto que deverá ser gravado entre aspas simples.')
arquivo.write('Ao utilizar ‘w’ em um arquivo já existente, ele reescreverá todo o conteúdo do arquivo, fazendo com que todos os dados que estavam nele sejam apagados.')
arquivo.close()