import PIL.Image
import io


print("1 - Esconder PNG em JPG \n2 - Achar imagem escondida")
op = int(input("Escolha a opcao:\n "))

if op == 1:
    oculta = input("nome da imagem que quer esconder:")
    img = PIL.Image.open(oculta)#Colocar aqui a imagem q quer codificar.png
    byte_arr = io.BytesIO()
    img.save(byte_arr, format ='PNG')

    alvo = input("Nome da imagem EM que se quer esconder:")
    with open(alvo, 'ab') as f:
        f.write(byte_arr.getvalue())



if op == 2:
    retirar = input("Nome da imagem da qual se quer tirar outra imagem escondida: ")
    with open(retirar, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)

        new_img = PIL.Image.open(io.BytesIO(f.read()))
        new_img.save("decodificada.png")





