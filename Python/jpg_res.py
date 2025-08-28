from PIL import Image


def find_res(img_name: str):
    return Image.open(img_name).size


img = input("Enter Image Name: ")
print(find_res(img))
