def calculo_IMC():
 nome='Priscila'
 altura=1.66
 peso=60
 imc=peso/altura**2
 print(f'{nome} tem { altura:.2f} m')
 print(f'Seu IMC é {imc:.2f}')

if __name__ == '__main__':
 calculo_IMC()
