import pyfiglet
alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message,num):

    password = list(message)

    for i in range(0,len(password)):

        if password[i] != " ":
            newNum = alfabe.index(password[i]) + num

            if newNum >= len(alfabe):

                newNum = newNum - len(alfabe)

                password[i] = alfabe[newNum]

            else:
                password[i] = alfabe[newNum]

    return "".join(password)

def decode(password,num):

    password = list(password)

    for i in range(0, len(password)):

        if password[i] != " ":
            newNum = alfabe.index(password[i]) - num

            if newNum < 0:

                newNum = newNum + len(alfabe)

                password[i] = alfabe[newNum]

            else:
                password[i] = alfabe[newNum]

    return "".join(password)

selamlama = pyfiglet.figlet_format("Sezar Sifresi")
bilgi = ("Hosgeldiniz.Bu programda mesajinizi sezar sifresi yontemiyle belirli bir miktar oteleyerek sifreleyebilirsiniz\n"
         "1-) Encode: Mesajinizi sifreler.\n"
         "2-) Decode: Sifreyi cozer.\n"
         "3-) Cikis.  ")
print(selamlama)
print(bilgi)



while(True):

    islem = int(input("Yapacaginiz Islemi Seciniz: "))
    if islem == 1:

        mesaj = input("Mesajinizi Giriniz: ")
        otelemeMiktari = int(input("Oteleme Miktarini Giriniz: "))

        print(encode(mesaj.lower(), otelemeMiktari))

    elif islem == 2:

        sifre = mesaj = input("Sifre Giriniz: ")
        otelemeMiktari = int(input("Oteleme Miktarini Giriniz: "))
        print(decode(sifre.lower(),otelemeMiktari))

    elif islem == 3:

        print("Program Sonlandirildi")
        break

    else:
        print("Lutfen Gecerli Bir Islem Seciniz")


