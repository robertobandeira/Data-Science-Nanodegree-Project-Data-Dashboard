import pandas as pd
import plotly.graph_objs as go
import wbgapi as wb

def return_figures():
    """Creates plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the plotly visualizations

    """
    data = wb.data.DataFrame(['NY.GDP.PCAP.CD',
                              'SP.POP.TOTL',
                              'NY.GDP.MKTP.CD', 
                              'SE.XPD.TOTL.GD.ZS'], 
                              ['USA', 'BRA', 'CHN', 'IND'], 
                              columns='series').reset_index()
    data.rename(columns={'NY.GDP.PCAP.CD':'GDP Per Capita', 
                 'SP.POP.TOTL':'Population', 
                 'NY.GDP.MKTP.CD':'GDP', 
                 'SE.XPD.TOTL.GD.ZS':'Education Expenditure'}, inplace=True)
    data['time'] = data.time.str.extract('(\d+)')
    print(data.head())

    graph_one = []
    graph_two = []
    graph_three = []
    graph_four = []

    for country in data.economy.unique():
        data_country = data[data.economy == country]
        graph_one.append(
            go.Scatter(
                x = data_country.time,
                y = data_country['Population'],
                mode = 'lines',
                name = country
            )
        )

        graph_two.append(
            go.Scatter(
                x = data_country.time,
                y = data_country['GDP'],
                mode = 'lines',
                name = country
            )
        )

        graph_three.append(
            go.Scatter(
                x = data_country.time,
                y = data_country['GDP Per Capita'],
                mode = 'lines',
                name = country
            )
        )

        graph_four.append(
            go.Scatter(
                x = data_country.time,
                y = data_country['Education Expenditure'],
                mode = 'lines',
                name = country
            )
        )

    layout_one = dict(title = 'Population',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Population'),
                )
    
    layout_two = dict(title = 'GDP',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'GDP'),
                )
    
    layout_three = dict(title = 'GDP Per Capita',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'GDP Per Capita'),
                )
    
    layout_four = dict(title = 'Education Expenditure',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Education Expenditure'),
                )

    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    return figures