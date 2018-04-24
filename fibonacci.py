print("""Fibonacci serisi, bir sayıyı önceki iki sayının toplamı olarak oluşturur.""")
fibonacci = 1
liste = [0, 1]
for i in range(21):
    liste.append(liste[-1] + liste[-2])
print(liste)
