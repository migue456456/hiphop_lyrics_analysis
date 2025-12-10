import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_top_k(sorted_items, k, title):
    top_k = dict(sorted_items[:k])
    fig = px.bar(
        x=list(top_k.keys()),
        y=list(top_k.values()),
        title=f"Top {k} Words in {title}"
    )
    fig.show()

def compare_top_k(sorted1, sorted2, k, name1, name2):
    top1 = dict(sorted1[:k])
    top2 = dict(sorted2[:k])

    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=(name1, name2))

    fig.add_trace(go.Bar(x=list(top1.keys()), y=list(top1.values())), row=1, col=1)
    fig.add_trace(go.Bar(x=list(top2.keys()), y=list(top2.values())), row=1, col=2)

    fig.update_layout(
        title=f"Top {k} Words Comparison",
        height=500, width=1000,
        showlegend=False
    )
    fig.show()

def plot_categories(cat1, cat2, name1, name2):
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=(name1, name2))

    fig.add_trace(go.Bar(
        x=list(cat1.keys()),
        y=list(cat1.values()),
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        x=list(cat2.keys()),
        y=list(cat2.values()),
    ), row=1, col=2)

    fig.update_layout(
        title="Category Word Frequency Comparison",
        height=500, width=1000,
        showlegend=False
    )
    fig.show()
