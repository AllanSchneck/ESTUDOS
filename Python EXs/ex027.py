n = str(input('Digite seu nome completo: '))
t = (n.lower())
s = (t.split())
p = (s[0])
u = (s[-1])
print('Seu nome \033[1;30;107{}\033[m'.format(t))
print('primeiro nome é \033[32m{}\033[m'.format(p))
print('último nome é \033[31m{}'.format(u))