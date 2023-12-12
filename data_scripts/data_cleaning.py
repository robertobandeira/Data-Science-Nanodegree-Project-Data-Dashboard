import pandas as pd
import plotly.graph_objs as go

def return_figures():
    """Creates plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the plotly visualizations

    """
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = [0, 1, 2, 3, 4, 5],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Chart One',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )

    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures