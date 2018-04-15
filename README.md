# dash-html-template
[Dash HTML components](https://github.com/plotly/dash-html-components) tree generator from HTML template with optional ID-based injection of other Dash components.

## Installation
```
pip install git+https://github.com/masdeseiscaracteres/dash-html-template.git
```

## Usage
Just write `<template id='your_component_id'></template>` in your HTML code and have this replaced by the component specified as the
`"your_component_id"` key of a Python dictionary.

Complete example:
```python
import dash
import dash_core_components as dcc
from datetime import datetime as dt
from dash_html_template import Template

date_picker = dcc.DatePickerSingle(
    id='date-picker-single',
    date=dt(1997, 5, 10)
)

html_layout = """
    <div style='height: 20em; display: flex;
                align-items: center; justify-content: center;
                border: dashed;'>
    <template id='date_picker'></template>
    </div>
    """

injection_dict = {'date_picker': date_picker}

app = dash.Dash()
app.layout = Template.from_string(html_layout, injection_dict)

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Use cases
- Insert Dash components in complex HTML layouts.
- Facilitate the use of CSS frameworks (e.g. Bootstrap, Bulma) in Dash applications. No need to write your HTML using Dash HTML components.
