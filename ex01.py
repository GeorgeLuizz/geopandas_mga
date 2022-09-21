import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

data = gpd.read_file('dados/PR_Municipios_2021.shp')

data.plot()

data.plot(figsize=(16, 14), facecolor='white', edgecolor='black')

gdf_mga = data[data['NM_MUN'] == 'Maringá']
gdf_mga

gdf_mga.plot(figsize=(8, 8), facecolor='white', edgecolor='black')
plt.show()

filename = "dados/maringa.json"
gdf_mga.to_file(filename, driver="GeoJSON")

gdf_mga = gpd.read_file(filename, driver="GeoJSON")
gdf_mga



ponto_1 = Point(2,3)
ponto_2 = Point(5,7)

distancia = ponto_1.distance(ponto_2)

print(distancia)

ponto_1 = Point(2,3)
ponto_2 = Point(5,7)
ponto_3 = Point(2,10)

linha = LineString([ponto_1, ponto_2, ponto_3])

cordenadas_x = list(linha.xy[0])
cordenadas_y = list(linha.xy[1])
print('cordenadas_x:', cordenadas_x)
print('cordenadas_y:', cordenadas_y)

poly = Polygon([(2,3),(5,7),(2,10)])

poly_area = poly.area

print(poly_area)