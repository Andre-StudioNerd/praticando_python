import os as o

def somatorio():
  soma_impares=0
  for i in range(1,11,2):
    soma_impares+=i
  print(soma_impares)

if __name__=='__main__':
  o.system('cls' if o.name == 'nt' else 'clear')
  somatorio()
