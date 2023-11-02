# Importing libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Display all df w/o truncation
pd.set_option('display.max_columns', None)

df = pd.read_csv("lsda/data/csv/GlobalWeatherRepository.csv")

