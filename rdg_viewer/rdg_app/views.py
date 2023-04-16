from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import plotly.graph_objs as go
import plotly.offline as opy

def plotly_view(request):
    nodes = [
        {"id": "A", "x": 0, "y": 0},
        {"id": "B", "x": 1, "y": 1},
        {"id": "C", "x": 2, "y": 0},
    ]

    edges = [
        {"source": "A", "target": "B"},
        {"source": "B", "target": "C"},
    ]

    node_trace = go.Scatter(
        x=[node["x"] for node in nodes],
        y=[node["y"] for node in nodes],
        text=[node["id"] for node in nodes],
        mode="markers+text",
        textposition="top center",
        name="Nodes",
        marker=dict(size=10, color="rgba(0, 0, 255, 0.8)"),
        textfont=dict(color="black"),
    )

    edge_trace = go.Scatter(
        x=[],
        y=[],
        mode="lines",
        line=dict(color="rgba(0, 0, 0, 0.8)", width=1),
        hoverinfo="none",
    )

    for edge in edges:
        source = next(node for node in nodes if node["id"] == edge["source"])
        target = next(node for node in nodes if node["id"] == edge["target"])

        edge_trace["x"] += (source["x"], target["x"], None)
        edge_trace["y"] += (source["y"], target["y"], None)

    layout = go.Layout(
        title="RDG Viewer - Plotly.py",
        showlegend=False,
        hovermode="closest",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )

    data = [edge_trace, node_trace]
    fig = go.Figure(data=data, layout=layout)
    plot = opy.plot(fig, auto_open=False, output_type="div")

    return render(request, "rdg_app/plotly.html", {"plot": plot})

def index(request):
    return render(request, 'rdg_app/index.html')


def networkx_view(request):
    return render(request, 'rdg_app/networkx.html')


def graphviz_view(request):
    return render(request, 'rdg_app/graphviz.html')