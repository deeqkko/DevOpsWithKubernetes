import requests

def load_image():
    pic_url = "https://picsum.photos/1200"
    pic_object = requests.get(pic_url)
    with open("backend/potd/potd.jpg","wb") as file:
        file.write(pic_object.content)
        file.close()