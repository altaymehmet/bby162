print("Adam Asmaca ")

import random

hayvanlar = random.choice(['ayı', 'penguen', 'kedi', 'köpek', 'fare', 'zürafa'])

harfhavuzu = []

kalanhak = 4

karakterçizgisi = '_'

karakteryazısı = list(karakterçizgisi * len(hayvanlar))

dongu = 1





while dongu:

    print(' '.join(karakteryazısı), end='\n\n')

    alinanharf = input('Bir harf giriniz: ')

    try:

        int(alinanharf)

        print('Lütfen harf girin.')

    except:

        if len(alinanharf) > 1:

            print('Sadece bir harf giriniz.')

        else:

            if alinanharf in harfhavuzu:

                print('Bu harfi zaten girdiniz.')





            else:

                bulduk = None

                for i in range(len(hayvanlar)):

                    if alinanharf == hayvanlar[i]:

                        bulduk = True

                        karakteryazısı[i] = alinanharf

                        harfhavuzu.append(alinanharf)

                        if karakterçizgisi not in karakteryazısı:

                            print(' '.join(karakteryazısı))

                            print('Tebrikler...')

                            dongu = 0





                else:

                    if bulduk != True:

                        kalanhak -= 1

                        print('Yanlış harf girdiniz. Kalan hakkınız: {}'.format(kalanhak))

                        harfhavuzu.append(alinanharf)

                if kalanhak == 0:

                    print('Kaybettiniz. Doğru kelime "{}"'.format(hayvanlar))

                    break