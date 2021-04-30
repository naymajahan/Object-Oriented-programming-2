
class Dancer:
    def __init__(self, style):
        self.style = style

    def dance(self):
        print(f'Dancing is , {self.style}')



class Singer:
    def __init__(self, genra):
        self.genra = genra

    def sing(self):
        print(f'singing {self.genra} music')


class Artist:
    def __init__(self, painting_material):
        self.painting_material = painting_material


    def paint(self):
        print(f'Painting with {self.painting_material} ')



class SuperHuman(Dancer, Singer, Artist):
    def __init__(self, style, genra, painting_material, sport):
        Dancer.__init__(self, style)
        Singer.__init__(self, genra)
        Artist.__init__(self, painting_material)
        self.sport = sport


    def play_sport(self):
        print(f'PLAYING {self.sport}')


    #### Over writing the dance method of dancer class
    def dance(self, competition = "PPP"):
        print(f'Dancing with my own {self.style} in the competition {competition}')






"""
s = SuperHuman('Hip-Hop', 'Classical', 'Acrylic', 'Football')

print(s.style)
print(s.genra)
print(s.painting_material)
print(s.sport)
s.dance()
s.sing()
s.paint()
s.play_sport()

"""

print(help(SuperHuman))




