import PIL 
import numpy as np


def QIM():
    image_path = input("Введите путь до файла\n")

    img = PIL.Image.open(image_path)
    img_rgb = img.convert('RGB')
    img_matrix = np.array(img_rgb, dtype=np.int16)

    q = int(input("Введите шаг квантования, являющийся четным от 0 до 255"))

    if q%2!=0 or q<0 or q>255:
        print("Введите корректное q")
        return 0

    mes_vstr = input("Введите сообщение для встраивания\n")

    bytes_data = mes_vstr.encode('utf-8')
    binary_mes_vstr = ''.join(f'{byte:08b}' for byte in bytes_data)

    def qim(x, q, m):
        return q * (x // q) + (q // 2) * m

    height, width, channels = img_matrix.shape

    total_pixels = height * width * channels
    total_bits = len(binary_mes_vstr)

    if total_bits > total_pixels:
        print(f"({total_bits} бит) больше изображения ({total_pixels} пикселей)")
        return 0

    bit_counter = 0
    done = False  # Флаг завершения
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                if bit_counter >= total_bits:  # Сообщение встроено — выходим
                    done = True
                    break
                current_bit = int(binary_mes_vstr[bit_counter])
                img_matrix[y, x, c] = qim(img_matrix[y, x, c], q, m=current_bit)
                bit_counter += 1
            if done:
                break
        if done:
            break

    # FIX: Обрезаем значения в [0, 255] и конвертируем в uint8 перед сохранением
    img_matrix = np.clip(img_matrix, 0, 255).astype(np.uint8)
    
    result_img = PIL.Image.fromarray(img_matrix)
    result_img.save("stego_cyclic.png")

    return "Успех файл сохранен в stego_cyclic.png"