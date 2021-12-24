import dash
from tdash import Nav


def test_nav(dash_duo):
    app = dash.Dash(__name__)
    app.layout = dash.html.Div(Nav('/assets/logo.png'))

    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)
    pass
