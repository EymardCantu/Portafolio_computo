import os
import pandas as pd
import plotly.express as px
from elasticsearch import Elasticsearch
from collections import Counter

# Conectar a Elasticsearch
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "password")
)

# Obtener datos de Elasticsearch
result = es.search(index="spotify_tracks", query={"match_all": {}}, size=1000)
data = [hit["_source"] for hit in result["hits"]["hits"]]
df = pd.DataFrame(data)

# Limpiar datos
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')


# Asegurar la existencia de la carpeta docs
os.makedirs("docs", exist_ok=True)

# Convertir fechas y obtener el año de lanzamiento
df['release_date'] = pd.to_datetime(df['release_date'])
df['release_year'] = df['release_date'].dt.year


year_data = df.groupby('release_year').agg({
    'popularity': 'mean', 
    'duration_min': 'mean',
    'track_name': 'count'
}).reset_index()

fig1 = px.scatter(
    year_data, 
    x='release_year', 
    y='popularity', 
    size='track_name',  
    color='duration_min',  
    hover_name='release_year',
    color_continuous_scale='viridis',
    title='Evolución de la Popularidad y Duración por Año'
)
fig1.write_html("docs/bubble_chart_year_popularity.html")
fig1.write_image("docs/bubble_chart_year_popularity.png")


top_artists = df.groupby('artist').agg({
    'popularity': 'mean',
    'track_name': 'count'
}).sort_values('popularity', ascending=False).head(15).reset_index()

fig2 = px.bar(
    top_artists,
    y='artist',
    x='popularity',
    color='popularity',
    text='track_name', 
    orientation='h',
    color_continuous_scale='Plasma',
    title='Top 15 Artistas por Popularidad Promedio'
)
fig2.write_html("docs/top_artists_popularity.html")
fig2.write_image("docs/top_artists_popularity.png")


fig3 = px.scatter(
    df,
    x='duration_min',
    y='popularity',
    color='release_year',
    hover_name='track_name',
    hover_data=['artist'],
    color_continuous_scale='turbo',
    title='Relación entre Duración y Popularidad'
)
fig3.write_html("docs/scatter_duration_popularity.html")
fig3.write_image("docs/scatter_duration_popularity.png")


popularity_counts = Counter(df['popularity'])

fig4 = px.bar(
    x=list(popularity_counts.keys()),
    y=list(popularity_counts.values()),
    color=list(popularity_counts.keys()),
    color_continuous_scale='Bluered',
    title='Distribución de la Popularidad de Canciones'
)
fig4.write_html("docs/popularity_distribution.html")
fig4.write_image("docs/popularity_distribution.png")

print("Las cuatro gráficas han sido generadas en 'docs'")
