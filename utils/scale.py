from collections import OrderedDict


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

    matrices = {'guitar': OrderedDict([('1E', ('B', 'C', 'D♭', 'D', 'E♭')),
                                       ('2B', ('G♭', 'G', 'A♭', 'A', 'B♭')),
                                       ('3G', ('D', 'E♭', 'E', 'F', 'G♭')),
                                       ('4D', ('A', 'B♭', 'B', 'C', 'D♭')),
                                       ('5A', ('E', 'F', 'G♭', 'G', 'A♭')),
                                       ('6E', ('B', 'C', 'D♭', 'D', 'E♭')),
                                       ('7B', ('G♭', 'G', 'A♭', 'A', 'B♭'))]),
                'bass': OrderedDict([('0C', ('G♭', 'G', 'A', 'B♭', 'B')),
                                     ('1G', ('D', 'E♭', 'E', 'F', 'G♭')),
                                     ('2D', ('A', 'B♭', 'B', 'C', 'D♭')),
                                     ('3A', ('E', 'F', 'G♭', 'G', 'A♭')),
                                     ('4E', ('B', 'C', 'D♭', 'D', 'E♭')),
                                     ('5B', ('G♭', 'G', 'A♭', 'A', 'B♭'))])}

    scales = {'major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
              'minor': ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭']}

    @classmethod
    def render(cls, scale, fretboard):
        scale_notes = cls.scales[scale]

        print(" ".join(scale_notes))

        [print("{0}|~··{1}·".format(open_note,
                                    "".join([cls._get_note_symbol(note, scale_notes)
                                             for note in line])))
         for open_note, line in cls.matrices[fretboard].items()]

    @classmethod
    def _get_note_symbol(cls, note, scale_notes):
        if note not in scale_notes:
            return "·"

        return "●" if note == 'C' else '○'
