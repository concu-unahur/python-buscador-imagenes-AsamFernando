import logging
from api import PixabayAPI
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cantImgs=5

carpeta_imagenes = './imagenes'
query = 'perro'
api = PixabayAPI('15310722-6cbef7cd9b9a485bd996b4ad8', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cantImgs)

listaT=[]

for u in urls:
  listaT.append(threading.Thread(target=api.descargar_imagen, args=[u]))

for t in listaT:
  logging.info(f'Descargando {u}')
  t.start()

'''for u in urls:
  logging.info(f'Descargando {u}')
  api.descargar_imagen(u)'''
