class Scale:
    notes = ['C',  # Do
             'D♭',
             'D',  # Re
             'E♭',
             'E',  # Mi
             'F',  # Fa
             'G♭',
             'G',  # Sol
             'A♭',
             'A',  # La
             'B♭',
             'B']  # Si

    scales = {'major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
              'minor': ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭']}

    def __init__(self, scale, fretboard, strings=None):
        self.scale = scale
        self.fretboard = fretboard
        self.strings = strings or {'bass': 4, 'guitar': 6}.get(fretboard)

    def render(self):
        print(" ".join(Scale.scales[self.scale]))

        # print("\n".join(["|··{}{}{}{}{}··".format('·', '·', '·', '·', '·')
        #                  for _ in range(0, self.strings)]))
