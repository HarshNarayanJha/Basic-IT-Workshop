def print_res(img_name: str):
    with open(img_name, 'rb') as fp:
        data = fp.read()
        if data.startswith(b'\xff\xd8'):
            w, h = None, None
            index = 2
            while index < len(data):
                m = data[index]
                if m == 0xFF:
                    m = data[index + 1]
                    if m == 0xC0 or m == 0xC2:
                        h = (data[index + 5] << 8) + data[index + 6]
                        w = (data[index + 7] << 8) + data[index + 8]
                        break
                index += 1

            return w, h

img = input("Enter Image Name: ")
print_res(img)
