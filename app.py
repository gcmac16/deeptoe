import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import (
    Input,
    Output
)

from boards.config import ALL_CELL_INPUTS
from boards.game import Game


cell_size = '50px'
padding_size = '10px'
BOARD_DIV_STYLE = {
    'padding-bottom': padding_size,
}


def generate_board(board_id, values=['']*9):
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
    i = 0
    for row_num in range(3):
        table_row = []
        for col_num in range(3):
            cell_id = f'{board_id}_c{row_num}{col_num}'
            table_row.append(html.Td(values[i], id=cell_id, style=td_style))
        table.append(html.Tr(table_row))

    return html.Table(html.Tbody(table), style=table_style)


def serve_layout():
    global game
    game = Game()
    return html.Div(children=[
        html.H1(children='Are You Read To Lose?'),
        html.Div(id='full-board', children=[
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
    ])


game = Game()
    
app = dash.Dash(__name__)
app.layout = serve_layout

        
def build_board_with_values():
    cell_values = game.get_cell_values()

    return html.Div(id='full-board', children=[
        html.Div(children=[
            generate_board('b00', cell_values[:9]),
            generate_board('b01', cell_values[9:18]),
            generate_board('b02', cell_values[18:27])
        ], style=BOARD_DIV_STYLE),
        html.Div(children=[
            generate_board('b10', cell_values[27:36]),
            generate_board('b11', cell_values[36:45]),
            generate_board('b12', cell_values[45:54])
        ], style=BOARD_DIV_STYLE),
        html.Div(children=[
            generate_board('b20', cell_values[54:63]),
            generate_board('b21', cell_values[63:72]),
            generate_board('b22', cell_values[72:])
        ], style=BOARD_DIV_STYLE)
    ])


@app.callback(
     Output(component_id='full-board', component_property='children'),
     ALL_CELL_INPUTS
)
def cell_clicks(*args):
#     sum_args = sum([int(arg) if arg else 0 for arg in args])
#     if sum_args == 0:
#         return build_board_with_values()
    
#     board_id, cell_id = 'b00_c00'.split('_')
#     game.player_move(board_id[1:], cell_id[1:])
    
    print(len(args))
    return build_board_with_values()
        


if __name__ == '__main__':
    app.run_server(debug=True)
