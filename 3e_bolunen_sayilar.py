print("""1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
Bu işlemi continue ile yapmaya çalışın.""")

i = 1
while i <= 100:
    if i % 3 == 0:
        print(i)
        i += 1
    else:
        i += 1
        continue
