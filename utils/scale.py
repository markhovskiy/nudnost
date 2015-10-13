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

    matrix = [('D', 'E♭', 'E', 'F', 'G♭'),
              ('A', 'B♭', 'B', 'C', 'D♭'),
              ('E', 'F', 'G♭', 'G', 'A♭'),
              ('B', 'C', 'D♭', 'D', 'E♭')]

    scales = {'major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
              'minor': ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭']}

    def __init__(self, scale, fretboard, strings=None):
        self.scale = scale
        self.fretboard = fretboard
        self.strings = strings or {'bass': 4, 'guitar': 6}.get(fretboard)

    def render(self):
        scale_notes = self.scales[self.scale]
        print(" ".join(scale_notes))

        for line in self.matrix:
            print("|··", end='')

            [print(self._get_note_symbol(note, scale_notes), end='')
             for note in line]

            print("·")

    def _get_note_symbol(self, note, scale_notes):
        if note not in scale_notes:
            return "·"

        return "●" if note == 'C' else '○'
