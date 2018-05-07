valor=float(input())
n100=valor//100
valor%=100
n50=valor//50
valor%=50
n20=valor//20
valor%=20
n10=valor//10
valor%=10
n5=valor//5
valor%=5
n2=valor//2
valor%=2
n1=valor//1
valor%=1
n050=valor//0.50
valor=valor%0.50
n025=valor//0.25
valor=valor%0.25
n010=valor//0.10
valor=valor%0.10
n05=valor//0.05
valor=valor%0.05
n01=int(round(valor/0.01))
print("NOTAS:")
print(int(n100),"nota(s) de R$ 100.00")
print(int(n50),"nota(s) de R$ 50.00")
print(int(n20),"nota(s) de R$ 20.00")
print(int(n10),"nota(s) de R$ 10.00")
print(int(n5),"nota(s) de R$ 5.00")
print(int(n2),"nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(n1),"moeda(s) de R$ 1.00")
print(int(n050),"moeda(s) de R$ 0.50")
print(int(n025),"moeda(s) de R$ 0.25")
print(int(n010),"moeda(s) de R$ 0.10")
print(int(n05),"moeda(s) de R$ 0.05")
print(n01,"moeda(s) de R$ 0.01")
