import requests

url = 'https://www.cuspide.com/cienmasvendido'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

pos = html.find("ctl02_img_tapa")
segmento = html[pos+58: pos+150]
pos_final = segmento.find('"')
nombre_libro = segmento[: pos_final]
print(nombre_libro)
