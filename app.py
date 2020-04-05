import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import (
    Input,
    Output
)


cell_size = '50px'
padding_size = '10px'
BOARD_DIV_STYLE = {
    'padding-bottom': padding_size,
}
TURN = 'X'


def switch_turn():
    global TURN
    if TURN == 'X':
        TURN = 'O'
    else:
        TURN = 'X'


def generate_board(board_id):
    table_style = {
        'display': 'inline-block',
        'border-spacing': 0,
        'padding-right': padding_size
    }
    td_style = {
        'height': cell_size,
        'width': cell_size,
        'text-align': 'center',
        'vertical-align': 'center',
        'border': '3px solid black'
    }

    table = []
    for row_num in range(3):
        table_row = []
        for col_num in range(3):
            cell_id = f'{board_id}_c{row_num}{col_num}'
            table_row.append(html.Td(id=cell_id, style=td_style))
        table.append(html.Tr(table_row))

    return html.Table(html.Tbody(table), style=table_style)


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Are You Read To Lose?'),
    html.Div(children=[
        generate_board('b00'),
        generate_board('b01'),
        generate_board('b02')
    ], style=BOARD_DIV_STYLE),
    html.Div(children=[
        generate_board('b10'),
        generate_board('b11'),
        generate_board('b12')
    ], style=BOARD_DIV_STYLE),
    html.Div(children=[
        generate_board('b20'),
        generate_board('b21'),
        generate_board('b22')
    ], style=BOARD_DIV_STYLE)
])


@app.callback(
     Output(component_id='b00_c00', component_property='children'),
     [Input('b00_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c01', component_property='children'),
     [Input('b00_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c02', component_property='children'),
     [Input('b00_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c10', component_property='children'),
     [Input('b00_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c11', component_property='children'),
     [Input('b00_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c12', component_property='children'),
     [Input('b00_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c20', component_property='children'),
     [Input('b00_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c21', component_property='children'),
     [Input('b00_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b00_c22', component_property='children'),
     [Input('b00_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c00', component_property='children'),
     [Input('b01_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c01', component_property='children'),
     [Input('b01_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c02', component_property='children'),
     [Input('b01_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c10', component_property='children'),
     [Input('b01_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c11', component_property='children'),
     [Input('b01_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c12', component_property='children'),
     [Input('b01_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c20', component_property='children'),
     [Input('b01_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c21', component_property='children'),
     [Input('b01_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b01_c22', component_property='children'),
     [Input('b01_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c00', component_property='children'),
     [Input('b02_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c01', component_property='children'),
     [Input('b02_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c02', component_property='children'),
     [Input('b02_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c10', component_property='children'),
     [Input('b02_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c11', component_property='children'),
     [Input('b02_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c12', component_property='children'),
     [Input('b02_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c20', component_property='children'),
     [Input('b02_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c21', component_property='children'),
     [Input('b02_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b02_c22', component_property='children'),
     [Input('b02_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c00', component_property='children'),
     [Input('b10_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c01', component_property='children'),
     [Input('b10_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c02', component_property='children'),
     [Input('b10_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c10', component_property='children'),
     [Input('b10_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c11', component_property='children'),
     [Input('b10_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c12', component_property='children'),
     [Input('b10_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c20', component_property='children'),
     [Input('b10_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c21', component_property='children'),
     [Input('b10_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b10_c22', component_property='children'),
     [Input('b10_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c00', component_property='children'),
     [Input('b11_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c01', component_property='children'),
     [Input('b11_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c02', component_property='children'),
     [Input('b11_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c10', component_property='children'),
     [Input('b11_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c11', component_property='children'),
     [Input('b11_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c12', component_property='children'),
     [Input('b11_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c20', component_property='children'),
     [Input('b11_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c21', component_property='children'),
     [Input('b11_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b11_c22', component_property='children'),
     [Input('b11_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c00', component_property='children'),
     [Input('b12_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c01', component_property='children'),
     [Input('b12_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c02', component_property='children'),
     [Input('b12_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c10', component_property='children'),
     [Input('b12_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c11', component_property='children'),
     [Input('b12_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c12', component_property='children'),
     [Input('b12_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c20', component_property='children'),
     [Input('b12_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c21', component_property='children'),
     [Input('b12_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b12_c22', component_property='children'),
     [Input('b12_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c00', component_property='children'),
     [Input('b20_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c01', component_property='children'),
     [Input('b20_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c02', component_property='children'),
     [Input('b20_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c10', component_property='children'),
     [Input('b20_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c11', component_property='children'),
     [Input('b20_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c12', component_property='children'),
     [Input('b20_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c20', component_property='children'),
     [Input('b20_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c21', component_property='children'),
     [Input('b20_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b20_c22', component_property='children'),
     [Input('b20_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c00', component_property='children'),
     [Input('b21_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c01', component_property='children'),
     [Input('b21_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c02', component_property='children'),
     [Input('b21_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c10', component_property='children'),
     [Input('b21_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c11', component_property='children'),
     [Input('b21_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c12', component_property='children'),
     [Input('b21_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c20', component_property='children'),
     [Input('b21_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c21', component_property='children'),
     [Input('b21_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b21_c22', component_property='children'),
     [Input('b21_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c00', component_property='children'),
     [Input('b22_c00', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c01', component_property='children'),
     [Input('b22_c01', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c02', component_property='children'),
     [Input('b22_c02', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c10', component_property='children'),
     [Input('b22_c10', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c11', component_property='children'),
     [Input('b22_c11', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c12', component_property='children'),
     [Input('b22_c12', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c20', component_property='children'),
     [Input('b22_c20', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c21', component_property='children'),
     [Input('b22_c21', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn

@app.callback(
     Output(component_id='b22_c22', component_property='children'),
     [Input('b22_c22', 'n_clicks')]
)
def cell_clicks(n_clicks):
    if n_clicks and n_clicks > 0:
        current_turn = TURN
        switch_turn()
        return current_turn


if __name__ == '__main__':
    app.run_server(debug=True)
