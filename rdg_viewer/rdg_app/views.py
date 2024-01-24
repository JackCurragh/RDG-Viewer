from django.shortcuts import render

import graphviz
# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import plotly.graph_objs as go
import plotly.offline as opy
from plotly.offline import plot

from io import BytesIO
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

import mpld3

import networkx as nx

from ete3 import Tree



def plotly_view(request):
    x_vals = [0, 100, 200, 400, 400]
    y_vals = [0, 0, 1, -1, 1]
    labels = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5']
    node_sizes = [30, 30, 30, 30, 30]
    node_colors = ['#1f77b4', '#2ca02c', '#d62728', '#808080', '#808080']


    edges = [(0, 1), (1, 2), (1, 3), (2, 4)]

    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in edges:
        x0, y0 = x_vals[edge[0]], y_vals[edge[0]]
        x1, y1 = x_vals[edge[1]], y_vals[edge[1]]
        edge_trace['x'] = list(edge_trace['x']) + [x0, x1, None]
        edge_trace['y'] = list(edge_trace['y']) + [y0, y1, None]

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=node_sizes,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))

    for node in range(len(x_vals)):
        x, y = x_vals[node], y_vals[node]
        node_trace['x'] += (x, )
        node_trace['y'] += (y, )
        node_trace['text'] += (labels[node], )
        node_trace['marker']['color'] += (node_colors[node], )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>RDG Graph',
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    plot_div = plot(fig, output_type='div')
    return render(request, 'rdg_app/plotly.html', {'plot_div': plot_div, 'page_title': 'Plotly Graph'})

def index(request):
    return render(request, 'rdg_app/index.html')





def networkx_view(request):
    G = nx.DiGraph()
    G.add_node(1, pos=(0, 0))
    G.add_node(2, pos=(100, 0))
    G.add_node(3, pos=(200, 10))
    G.add_node(4, pos=(400, -10))
    G.add_node(5, pos=(400, 10))
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 5)

    # Get node positions
    pos = nx.get_node_attributes(G, 'pos')

    # Draw graph
    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=500, edge_color='black', width=2)

    # Set layout
    ax.set_title('NetworkX Graph')
    ax.set_xlim([min(pos.values())[0]-100, max(pos.values())[0]+100])
    ax.set_ylim([min(pos.values())[1]-100, max(pos.values())[1]+100])
    ax.axis('off')

    chart = mpld3.fig_to_html(fig)
    return render(request, 'rdg_app/networkx.html', {'chart': chart, 'page_title': 'NetworkX'})

def graphviz_view(request):
    dot = graphviz.Digraph(comment='RDG')
    # add nodes
    dot.node('1', pos="0,0!")
    dot.node('2', pos="100,0!")
    dot.node('3', pos="200,-100!")
    dot.node('4', pos="400,0!")
    dot.node('5', pos="400,-100!")

    # add edges
    dot.edge('1', '2')
    dot.edge('2', '3')
    dot.edge('2', '4')
    dot.edge('3', '5')
    # set node and edge styles
    dot.attr('node', shape='oval', style='filled', fillcolor='lightblue')
    dot.attr('node', shape='diamond', style='filled', fillcolor='mediumpurple')
    dot.attr('node', shape='circle', style='filled', fillcolor='green')
    dot.node('2', style='filled', fillcolor='green')
    dot.attr('node', shape='circle', style='filled', fillcolor='red')
    dot.node('3', style='filled', fillcolor='red')
    dot.node('4', style='filled', fillcolor='red')
    dot.node('5', style='filled', fillcolor='red')
    dot.attr('edge', arrowhead='open')
    dot.graph_attr['rankdir'] = 'LR'   # Horizontal from left to right
    
    graph = dot.pipe(format='svg').decode('utf-8')
    
    return render(request, 'rdg_app/graphviz.html', {'graph': graph, 'page_title': 'Graphviz'})

def d3_view(request):
    # Define the tree data structure as a Python dictionary
    tree_data = {
        "text": {"name": "Parent node"},
        "children": [
            {
                "text": {"name": "Child node 1"},
                "children": [
                    {
                        "text": {"name": "Grandchild node 1"}
                    },
                    {
                        "text": {"name": "Grandchild node 2"}
                    }
                ]
            },
            {
                "text": {"name": "Child node 2"},
                "children": [
                    {
                        "text": {"name": "Grandchild node 3"}
                    },
                    {
                        "text": {"name": "Grandchild node 4"}
                    }
                ]
            }
        ]
    }

    # Pass the tree data to the template as a context variable
    context = {
        "tree_data": tree_data
    }

    # Render the template and pass the context
    return render(request, "rdg_app/d3.html", context)


from ete3 import Tree
from io import BytesIO
from django.http import HttpResponse

def ete3_view(request):
    # Create your newick string with branch lengths
    newick = "(((5:850)4:100,((8:460)7:400,2:859)6:90)3:50)1;"

    # Parse the newick string
    t = Tree(newick)
    
    # Render the tree to a PNG file
    t.render("/home/jack/Downloads/mytree.png")

    with open("mytree.png", "rb") as f:
        img_data = f.read()


    # Return the PNG file as a response
    with open("mytree.png", "rb") as f:
        response = HttpResponse(img_data, content_type="image/png")
    return response