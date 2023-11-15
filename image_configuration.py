from PIL import Image

img = Image.open("numbers.png")

def picar_imagem(img, quantidade, gap_horizontal, gap_vertical):
    nomes = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    qtd = 0
    numero = 0
    sum = 0
    ini_x = 0
    ini_y = 0
    fim_x = 28
    fim_y = 28
    while sum < quantidade:
        if ini_x > 529:
            ini_x = 0
            fim_x = 28

        if qtd > 15:
            qtd = 0
        nova_imagem = img.crop((ini_x, ini_y, fim_x, fim_y))
        nova_imagem.save(f"number_img/{nomes[numero]}_{str(qtd)}.png")
        qtd += 1
        sum += 1

        ini_x += 28 + gap_horizontal
        fim_x += 28 + gap_horizontal

        if ini_x in [105, 246, 387, 528]:
            ini_x += 1
            fim_x += 1
        
        if sum%16 == 0 and sum != 0:
            numero += 1
            ini_y += 28 + gap_vertical
            fim_y += 28 + gap_vertical

            if ini_y in [66, 265]:
                ini_y += 1
                fim_y += 1
#picar_imagem(img, 160, 7, 5)