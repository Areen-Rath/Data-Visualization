import pandas as pd
import plotly_express as px

data = pd.read_csv("Data.csv")

fig = px.scatter(data, x="date", y="cases", color="country")
fig.show()