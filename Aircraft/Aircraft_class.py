class Aircraft:
    def __init__(self, corrdonates:list, drawing:list):
        self.__corrdonates = corrdonates
        self.__drawing = drawing

    def get_corrdonates(self):
        return self.__corrdonates

    def get_drawing(self):
        return self.__drawing


