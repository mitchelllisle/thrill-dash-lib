from typing import ClassVar

from dash import dcc, html
import dash_bootstrap_components as dbc
from tdash.core import TComponent


class NoDataText(dbc.FormText, TComponent):
    def __init__(self, children: str = 'No data found for current applied filters.', **kwargs):
        self.style = {'fontSize': '20px', 'textAlign': 'center'}
        super().__init__(children=children, **kwargs)


class TGraphTitle(html.H5, TComponent):
    def __init__(self, size: int = 20, **kwargs):
        self.style = {'font-size': f'{size}px', 'font-weight': 'bold', 'float': 'left'}
        super().__init__(**kwargs)


class TGraphSubtitle(html.H6, TComponent):
    def __init__(self, **kwargs):
        self.style = {'max-width': '100%'}
        super().__init__(**kwargs)


class TGraph(dcc.Graph, TComponent):
    def __init__(self, id: str, **kwargs):
        self.id = id
        self.config = {'displayModeBar': False}
        super().__init__(id=id, **kwargs)


class TChart(dbc.Card, TComponent):

    name: ClassVar[str] = 'chart'

    def __init__(self, id: str, title: str, subtitle: str = None, footer: str = None, **kwargs):
        self.id = id
        self.style = {'width': '100%'}

        self.title = TGraphTitle(
            id=self.build_children_id('title', self.id), size=23, children=title
        )
        self.subtitle = TGraphSubtitle(
            id=self.build_children_id('subtitle', self.id), children=subtitle
        )
        self.graph = TGraph(id=self.build_children_id('graph', self.id))
        self.footer = TGraphSubtitle(id=self.build_children_id('footer', self.id), children=footer)

        super().__init__(id=self.id, children=self.build_children(), **kwargs)

    def _body(self) -> dbc.CardBody:
        return dbc.CardBody(
            children=[
                self.title,
                html.Br(),
                html.Br(),
                self.subtitle,
                dcc.Loading(self.graph),
            ]
        )

    def build_children(self):
        return [self._body(), html.Br(), self.footer]


class Stat(html.Div, TComponent):

    name: ClassVar[str] = 'stat'

    def __init__(
        self,
        id: str,
        title: str = None,
        subtitle: str = None,
        value: str = '-',
        color: str = '#445DED',
        with_filter: bool = False,
        **kwargs,
    ):
        self.id = id
        self.title = title
        self.color = color
        self.with_filter = with_filter
        self.subtitle = html.P(
            id=self.build_children_id(self.id, 'subtitle'),
            children=subtitle,
            style={'fontSize': '12px', 'position': 'absolute'},
        )

        self.value = html.H1(
            id=self.build_children_id(self.id, 'value'),
            children=value,
            style={'fontWeight': 'bold', 'fontSize': '50px', 'color': self.color},
        )

        self.body = self._body()
        self.children = self.build_children()

        super().__init__(
            id=self.id,
            children=self.children,
            **kwargs,
        )

    def _body(self) -> dbc.CardBody:
        return dbc.CardBody(
            id=self.build_children_id(self.id, 'body'),
            children=[
                html.Div(
                    children=[
                        TGraphTitle(
                            id=self.build_children_id(self.id, 'title'),
                            children=self.title
                        )
                    ],
                    style={'marginBottom': '10px'},
                ),
                html.Br(),
                dcc.Loading(
                    children=self.value,
                    type='dot',
                ),
                self.subtitle
            ],
        )

    def _card(self) -> dbc.Card:
        _style = {
            'max-height': '250px',
            'min-height': '250px' if self.with_filter else '200px',
            'min-width': '250px',
        }
        return dbc.Card(
            id=self.build_children_id(self.id, 'card'),
            children=[self.body],
            style=_style,
        )

    def build_children(self) -> dbc.Card:
        return self._card()


class Divider(dbc.Row, TComponent):
    def __init__(self, **kwargs):
        self.style = {
            'border-bottom': '1px solid lightgray',
            'margin-top': '20px',
            'margin-bottom': '20px'
        }
        super().__init__(**kwargs)
