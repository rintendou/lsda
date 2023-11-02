# Importing libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Display all df w/o truncation
pd.set_option('display.max_columns', None)

df = pd.read_csv("lsda/data/csv/GlobalWeatherRepository.csv")

# Setting up US dataframe
us_df = df[(df['country'] == "United States of America")]
numeric = us_df.describe(include=np.number)
category = us_df.describe(include="object")

# Average temperature in the US in Celcius
temp_fig = px.line(us_df, x='last_updated', y='temperature_fahrenheit',
                     title="Recent Temperature Trends in the United States of America", markers=True)
temp_fig.update_xaxes(title="Last Updated (Date)")
temp_fig.update_yaxes(title="Temperature (°F)")

temp_fig.update_traces(
    line=dict(width=4, color='Red'),  # Adjust line width
    # Adjust marker size and outlineß
    marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')),
)

temp_fig.show()
