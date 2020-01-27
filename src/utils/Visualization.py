import plotly.graph_objects as go


def visualize(weight_grid):
    fig = go.Figure(
        data=go.Contour(
            z=weight_grid,
            contours_coloring='heatmap'
        ))
    fig.show()
