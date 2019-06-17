from src.app import *


#=====================================================================================================================
# Layout
#=====================================================================================================================
# Main layout, this is where your app goes
indexLayout = html.Div(id='indexContent', children=[
    html.H1(id='title', children='Welcome to Clarity'),
    html.Div(id='user'),
    html.Div(id='content',className='content')
])


#=====================================================================================================================
# Callbacks
#=====================================================================================================================
# Main callback, return the rigth layout based on the selected page
@app.callback(
    Output('authorizedContent', 'children'),
    [Input('url', 'pathname')]
)
def on_load(pageName):
    # if pageName == '/page1':
    #     return page1.layout
    # elif pageName == '/page2':
    #     return page2.layout
    # else:
        return indexLayout


# Load the user element and logout link
# This is here as an example. You will want to replace it with your own
@app.callback(
    Output('user', 'children'),
    [Input('user', 'value')]
)
def on_load(value):
    picture = ''
    name = ''

    if session.currentUser is not None:
        email = session.currentUser.email
        id = session.currentUser.id
        name = session.currentUser.name
        picture = session.currentUser.picture

    layout = html.Table([
        html.Tr([
            html.Td([html.Img(src=picture,width=64,height=64)]),
            html.Td([html.P(name),dcc.Link('Logout', href='revoke')])
            ])
        ])

    return layout


#runMyApp()
hostName = env['SERVER']['host']
if __name__ == '__main__':
    app.run_server(debug=True,host=hostName)