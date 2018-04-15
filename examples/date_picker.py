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