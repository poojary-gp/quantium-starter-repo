import pytest
from dash.testing.application_runners import import_app

# Load your app from app.py
@pytest.fixture
def dash_app(dash_duo):
    app = import_app("app")  # "app" means app.py file
    dash_duo.start_server(app)
    return dash_duo


def test_header_present(dash_app):
    header = dash_app.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales Visualiser" in header.text


def test_visualisation_present(dash_app):
    graph = dash_app.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_app):
    radio = dash_app.find_element("#region-picker")
    assert radio is not None
