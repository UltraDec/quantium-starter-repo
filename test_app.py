from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

from app import dash_app

def test_header(dash_duo):
    dash_duo.start_server(dash_app)
    assert dash_duo.find_element("#header").text == "Pink Morsel Sales"

def test_visualization(dash_duo):
    dash_duo.start_server(dash_app)
    assert dash_duo.find_element("#visualization")

def test_radioitems(dash_duo):
    dash_duo.start_server(dash_app)
    assert dash_duo.find_element("#options")