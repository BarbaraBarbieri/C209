from PIL import Image

def msaa(input_image, kernel_size = 3):

    width, height = input_image.size                    # Altura e largura da imagem original
    output_image = Image.new("RGB", (width, height))    # Nova imagem, toda preta, com mesma altura e largura da original

    half_kernel = kernel_size // 2                      # Área onde a suavização será aplicada

    # Percorre os pixels da imagem original
    for x in range(half_kernel, width - half_kernel):
        for y in range(half_kernel, height - half_kernel):

            r_total, g_total, b_total = 0, 0, 0

            # Calcula a soma das cores dos pixels no Kernel
            for i in range(-half_kernel, half_kernel + 1):
                for j in range(-half_kernel, half_kernel + 1):
                    pixel = input_image.getpixel((x + i, y + j))
                    r, g, b = pixel
                    r_total += r
                    g_total += g
                    b_total += b

            # Calcula a média ponderada das cores dos pixels no Kernel
            num_pixels = kernel_size * kernel_size
            r_avg = r_total // num_pixels
            g_avg = g_total // num_pixels
            b_avg = b_total // num_pixels

            # Aplica a média ponderada das cores no pixel da imagem suavizada
            output_image.putpixel((x, y), (r_avg, g_avg, b_avg))

    return output_image

input_image = Image.open("input.jpeg")              # Carrega a imagem de entrada
output_image = msaa(input_image, kernel_size=5)     # Aplica a suavização
output_image.save("output.jpeg")                    # Salva a imagem resultante
