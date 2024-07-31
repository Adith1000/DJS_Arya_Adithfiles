import plotly.express as px
import pandas as pd

population_df=pd.read_csv('/Users/adithshetty/Desktop/Programming Folder/Python Programming/Machine Learning Tutorials/Plotly tutorial/Population_ds.csv')


asia_df=population_df(['India', 'China'])

dif=asia_df.diff()

fig = px.line(dif,
              title='Population', 
            )

fig.update_layout(yaxis_title='Population', 
                  legend_title='Countries', 
                  plot_bgcolor='black',
                  font_size=14)

fig.update_yaxes(rangemode='tozero')

fig.show()