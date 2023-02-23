import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import json

f = open('./test/city.json')
data = json.load(f)

##      DATA LOAD

df = pd.read_csv("./test/test.csv", 
                 usecols=["latitude", "longitude", "aqius"])


##      GEOPANDAS

# initialize an axis
fig, ax = plt.subplots(figsize=(8,6))
ax.set_axis_off()

# plot map on axis
countries = gpd.read_file(  
     gpd.datasets.get_path("naturalearth_lowres"))
countries[countries["name"] == data['data']['country']].plot(color="lightgrey", ax=ax, figsize=(8,1))

# # plot points
df.plot(x="longitude", y="latitude", kind="scatter", 
     c="aqius", colormap="YlOrRd",  
           ax=ax, figsize=(8,3))

# add grid
# ax.grid(alpha=0.5)
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()