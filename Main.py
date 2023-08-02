from App import App
from Object import Object

App = App("Shotformer", 640, 480)

Object1 = Object(25, 25, 150, 200, "blue_square.png")
App.app_add_obj(Object1)
App.app_running()

