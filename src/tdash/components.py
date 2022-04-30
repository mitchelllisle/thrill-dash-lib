from typing import Dict, Optional
from dash import html, dcc
from tdash.core import TComponent


class Label(html.P, TComponent):
    def __init__(self, style: Optional[Dict] = None, **kwargs):
        _style = {
            'size': '30px',
            'margin-bottom': '0px',
            'margin-top': '10px',
            'color': '#47474'
        }
        if not style:
            self.style = _style
        else:
            self.style = {**style, **_style}
        super().__init__(**kwargs)


class SquareDropdown(dcc.Dropdown, TComponent):
    def __init__(self, style: Optional[Dict] = None, **kwargs):
        _style = {
            'border-radius': '0px',
            'padding-left': '0px',
            'min-width': '250px',
            'max-width': '800px',
            'margin-right': '10px',
        }
        if not style:
            self.style = _style
        else:
            self.style = {**style, **_style}
        super().__init__(**kwargs)
