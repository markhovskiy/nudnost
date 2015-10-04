class Scale:
    def __init__(self, fretboard=None):
        self.fretboard = fretboard

    def render(self):
        print("\n".join(["|--o-o-o--",
                         "|--o-o-o--",
                         "|--o-oo---",
                         "|--o-oo---"]))
