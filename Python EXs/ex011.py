A = float(input('Digite a altura em metros das paredes de sua casa: '))
L = float(input('Digite a largura das paredes da casa: '))
a = (A*L)
t = (a/2)
print('Com a área de \033[1;30;43m{}m²\033[m você tera que gastar \033[1;30;107m{}L\033[m de tinta'.format(a, t))