"""
Plot a mind map based on data in the dataframe df grouped by a defined criteria.

2023-03-11, Johannes Köppern
"""

from graphviz import Digraph
import pandas as pd
import numpy as np

G = Digraph(format='jpeg')

G.attr(rankdir='LR', size='8,5')
G.attr('node', shape='circle')

df = pd.read_csv('so.csv')

# add the vertices
[G.node(str(x)) for x in np.unique(df[['From', 'To']].values.flatten())]

# add the edges
[G.edge(str(x[1][0]), str(x[1][1]), label=str(x[1][2])) for x in df.iterrows()]

G.render('sg', view=True)

print("Done.")


