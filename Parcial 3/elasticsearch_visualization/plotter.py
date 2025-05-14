import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch

# Conectar a Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Realizar una consulta para obtener los datos
result = es.search(index="spotify_tracks", body={
    "query": {
        "match_all": {}
    },
    "size": 1000  # Limitar el número de resultados (puedes ajustar esto)
})

# Extraer los valores de la columna que deseas graficar
streams = [hit['_source']['streams'] for hit in result['hits']['hits']]  # Reemplaza 'streams' con el nombre de la columna que deseas graficar

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.hist(streams, bins=50, color='skyblue', edgecolor='black')
plt.title('Distribución de Streams de Canciones en Spotify')
plt.xlabel('Streams')
plt.ylabel('Frecuencia')
plt.show()
plt.savefig('docs/graph.png')
