import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")
pic = px.bar(data, x = "Country", y = "InternetUsers")
pic.show()