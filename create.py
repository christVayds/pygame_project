from object import Object

class Create:

    def __init__(self, screen, player, list_obj):
        self.screen = screen
        self.player = player
        self.list_obj = list_obj

        # retun this list
        self.listofObjects = [player]

    def create(self):
        for obj in self.list_obj:
            object = Object(obj['rect'][0], obj['rect'][1], obj['rect'][2], obj['rect'][3], obj['type'], obj['name'])
            self.listofObjects.append(object)

    def draw(self):
        for obj in self.listofObjects:
            if obj != self.listofObjects[0]:
                obj.draw(self.screen)