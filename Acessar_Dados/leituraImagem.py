imagem = "/path/to/file.jpg"
with open(imagem, "rb") as imagem_file:
    content= imagem_file.read()
print(len(content))