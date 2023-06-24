import ui


mystyle={"margin": "120px"}
button = {"background-color":"red", "color":"white", "width":"50px", "height":"50px"}



layout = ui.Div(content=[
    ui.A(content='Home', style=mystyle),
    ui.A(content='Dashboard', style=mystyle),
    ui.A(content='Users', style=mystyle),
    ui.Button(content='Users', style=button)
], style={
      "color": "red",
      "font-size": "16px",
      "padding":"10px",
      "margin": "120px"
    },)





if __name__ == '__main__':
    app = ui.UI(layout=layout)
    app.run()
