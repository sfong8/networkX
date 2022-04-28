import geopandas


gdf = geopandas.read_file('./data/taxi_zones/taxi_zones.shp')

gdf.plot('zone',legend=True)