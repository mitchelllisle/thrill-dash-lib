from typing import List
from tdash.core import TComponent
from dash import html
import dash_bootstrap_components as dbc
from collections import namedtuple

NavLink = namedtuple('NavLink', ('text', 'path'))


class Nav(dbc.Nav, TComponent):

    name: str = 'nav'

    def __init__(self, links: List[NavLink], **kwargs):
        self.id = self.build_id()
        self.links = links
        # this centers the items in the middle of the nav
        self._item_style = {
            'margin-top': 'auto',
            'margin-bottom': 'auto',
            'color': 'black'
        }

        self.logo = html.Div(
            id=self.build_children_id('logo'),
            children='👋',
            style={
                'margin-left': '20px',
                'margin-right': '10px',
                **self._item_style
            }
        )

        self.style = {
            'border-bottom': '1px solid #ECECF1',
            'height': '60px'
        }

        super().__init__(id=self.id, children=self.build_children(), **kwargs)

    def build_children(self):
        _children = [self.logo]
        for link in self.links:
            _children.append(
                dbc.NavLink(
                    id=self.build_children_id(link.text.replace(' ', '-').lower(), 'link'),
                    children=link.text,
                    href=link.path,
                    style=self._item_style
                )
            )
        return _children
