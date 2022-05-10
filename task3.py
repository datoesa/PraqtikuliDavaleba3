import requests

response = requests.get('https://httpbin.org/image/webp')

image = open("image.jpg", "wb")

image.write(response.content)
