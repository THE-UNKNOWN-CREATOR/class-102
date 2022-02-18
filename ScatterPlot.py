import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")
pic = px.scatter(data, x = "Population", y = "Per capita", size = "Percentage", color = "Country", size_max = 50)
pic.show()
