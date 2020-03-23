elementler = {"D": 2.014102, "T": 3.016049,
                     "H": 1.00794, "He": 4.002602,"Li": 6.941,
                     "Be": 9.012182, "B": 10.811, "C": 12.0107,
                     "N": 14.0067, "O": 15.9994, "F": 18.9984032,
                     "Ne": 20.1797, "Na": 22.989769, "Mg": 24.305,
                     "Al": 26.9815386, "Si": 28.0855, "P": 30.973762,
                     "S": 32.065, "Cl": 35.453, "Ar": 39.948,
                     "K": 39.0983, "Ca": 40.078, "Sc": 44.955912,
                     "Ti": 47.867, "V": 50.9415, "Cr": 51.9961,
                     "Mn": 54.938045, "Fe": 55.845, "Co": 58.933195,
                     "Ni": 58.6934, "Cu": 63.546, "Zn": 65.409,
                     "Ga": 69.723, "Ge": 72.64, "As": 74.9216,
                     "Se": 78.96, "Br": 79.904, "Kr": 83.798,
                     "Rb": 85.4678, "Sr": 87.62, "Y": 88.90585,
                     "Zr": 91.224, "Nb": 92.90638, "Mo": 95.94,
                     "Tc": 97.907215, "Ru": 101.07, "Rh": 102.9055,
                     "Pd": 106.42, "Ag": 107.8682, "Cd": 112.411,
                     "In": 114.818, "Sn": 118.71, "Sb": 121.76,
                     "Te": 127.6, "I": 126.90447, "Xe": 131.293,
                     "Cs": 132.9054519, "Ba": 132.327, "La": 138.90547,
                     "Ce": 140.116, "Pr": 140.90765, "Nd": 144.242,
                     "Pm": 144.912745, "Sm": 150.36, "Eu": 151.964,
                     "Gd": 157.25, "Tb": 158.92535, "Dy": 172.5,
                     "Ho": 164.93032, "Er": 167.259, "Tm": 168.93421,
                     "Yb": 173.04, "Lu": 174.967, "Hf": 178.49,
                     "Ta": 180.94788, "W": 183.84, "Re": 186.07,
                     "Os": 190.23, "Ir": 192.217, "Pt": 195.084,
                     "Au": 196.966569, "Hg": 200.59, "Tl": 204.3833,
                     "Pb": 207.2, "Bi": 208.98040, "Po": 208.982415,
                     "At": 209.987131, "Rn": 222.01757, "Fr": 223.019731,
                     "Ra": 226.025402, "Ac": 227.027747, "Th": 232.03806,
                     "Pa": 231.03588, "U": 238.02891, "Np": 237.048167,
                     "Pu": 244.064198, "Am": 243.061373, "Cm": 247.070347,
                     "Bk": 247.070299, "Cf": 251.07958, "Es": 252.08297,
                     "Fm": 257.095099, "Md": 258.098425, "No": 259.10102,
                     "Lr": 266, "Rf": 267, "Db": 268, "Sg": 269, "Bh": 270,
                     "Hs": 270, "Mt": 278, "Ds": 281, "Rg": 282, "Cn": 285,
                     "Nh": 286, "Fl": 289, "Mc": 290, "Lv": 293, "Ts": 294,
                     "Og": 294}

while True:
    başlık = "A N A  M E N Ü".center(50, '_')
    alt_başlık = "".center(50, "_")
    print("\n"+başlık,"\n 1) Molekül formülü girerek yüzde hesaplama,\n\
 2) Yüzde girerek molekül formülü hesaplama,\n 3) Çıkış\n"+alt_başlık)

    seçenek = int(input("\nSeçiminizi yapınız (1-3): "))

    if seçenek == 1:
            while True:
                molekül_formülü = str(input("Molekül formülünü elementler arasında boşluk bırakarak giriniz \
(örnek: C6 H12 O6): "))
                elm = molekül_formülü.split(" ")
                hesaplama = {}
                atom_sayısı = {}
                for i in elm:
                    if i[:2] in elementler.keys():
                        hesaplama[i[:2]] = elementler[i[:2]]
                        if i[2:] == '':
                            atom_sayısı[i[:2]] = 1
                        else:
                            atom_sayısı[i[:2]] = i[2:]
                    elif i[:1] in elementler.keys():
                        hesaplama[i[:1]] = elementler[i[:1]]
                        if i[1:] == '':
                            atom_sayısı[i[:1]] = 1
                        else:
                            atom_sayısı[i[:1]] = i[1:]
                        
                molekül_ağırlığı = 0
                for i in hesaplama.keys():
                    molekül_ağırlığı += float(hesaplama[i]) * int(atom_sayısı[i])
                print("Molekül ağırlığı (g/mol): ",molekül_ağırlığı)

                yüzdeler = {}

                for j in hesaplama.keys():
                    yüzdeler[j] = float(hesaplama[j]) * int(atom_sayısı[j]) * 100 / molekül_ağırlığı

                for k in yüzdeler.keys():
                    print("Element: %s, "%k + "yüzdesi: %",round(yüzdeler[k],2))

                devam = input("Devam etmek için E, ana menüye gitmek için H tuşuna basınız: ")
                if devam == "E" or devam == "e":
                    continue
                elif devam == "H" or devam == "h":
                    break
                else:
                    pass
                break
    elif seçenek == 2:
        sorgu = {}
        while True:
            element_sembolü = input("Element sembolü: ")
            element_yüzdesi = input("Element yüzdesi: ")
            sorgu[element_sembolü] = element_yüzdesi
            devam = input("Devam etmek için 'E', tamamlamak için 'H' yazınız: ")
            if devam == 'e' or devam == 'E':
                continue
            else:
                break

        for i in sorgu.keys():
           sorgu[i] = float(sorgu[i]) / float(elementler[i])

        en_küçük = round(min(sorgu.values()))

        for j in sorgu.keys():
            sorgu[j] = round(sorgu[j]) / en_küçük

        print(sorgu)
        devam = input("Başka bir hesaplama yapmak ister misiniz? (E/H)")

        if devam == "E" or devam == "e":
            continue

    elif seçenek == 3:
       break
