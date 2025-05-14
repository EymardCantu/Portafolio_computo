import os
import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch
from collections import Counter

# Conectar a Elasticsearch
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "password"),
    headers={"Accept": "application/vnd.elasticsearch+json; compatible-with=7"}
)

# Realizar una consulta para obtener los datos
result = es.search(index="spotify_tracks", query={"match_all": {}}, size=1000)

# Extraer los valores para graficar
streams = [hit["_source"]["doc"]["popularity"] for hit in result["hits"]["hits"]]

# Asegurar que el directorio 'docs' exista
if not os.path.exists("docs"):
    os.makedirs("docs")


plt.figure(figsize=(10, 6))
plt.hist(streams, bins=50, color="skyblue", edgecolor="black")
plt.title("Distribución de Popularidad de Canciones en Spotify")
plt.xlabel("Popularidad")
plt.ylabel("Frecuencia")
plt.savefig("docs/graph.png")
plt.close()


plt.figure(figsize=(8, 5))
plt.plot(range(len(streams)), streams, marker='o', linestyle='-', color='blue')
plt.xlabel("Índice de la Canción")
plt.ylabel("Popularidad")
plt.title("Evolución de la Popularidad de Canciones")
plt.grid(True)
plt.savefig("docs/line_chart.png")
plt.close()


popularity_counts = Counter(streams)  # Contar la frecuencia de cada nivel de popularidad
plt.figure(figsize=(8, 5))
plt.bar(popularity_counts.keys(), popularity_counts.values(), color='purple', alpha=0.7)
plt.xlabel("Popularidad")
plt.ylabel("Número de Canciones")
plt.title("Frecuencia de Popularidad de Canciones en Spotify")
plt.grid(axis="y")
plt.savefig("docs/bar_chart.png")
plt.close()

print("Gráficos generados exitosamente: graph.png, line_chart.png y histogram.png")
