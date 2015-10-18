from utils.scale import Scale


def test_render_major_guitar(capsys):
    Scale.render(scale='major',
                 fretboard='guitar')

    out, _ = capsys.readouterr()

    assert out == ("C D E F G A B\n"
                   "1E|~··○●·○··\n"
                   "2B|~···○·○··\n"
                   "3G|~··○·○○··\n"
                   "4D|~··○·○●··\n"
                   "5A|~··○○·○··\n"
                   "6E|~··○●·○··\n"
                   "7B|~···○·○··\n")


def test_render_minor_guitar(capsys):
    Scale.render(scale='minor',
                 fretboard='guitar')

    out, _ = capsys.readouterr()

    assert out == ("C D E♭ F G A♭ B♭\n"
                   "1E|~···●·○○·\n"
                   "2B|~···○○·○·\n"
                   "3G|~··○○·○··\n"
                   "4D|~···○·●··\n"
                   "5A|~···○·○○·\n"
                   "6E|~···●·○○·\n"
                   "7B|~···○○·○·\n")


def test_render_major_bass(capsys):
    Scale.render(scale='major',
                 fretboard='bass')

    out, _ = capsys.readouterr()

    assert out == ("C D E F G A B\n"
                   "0C|~···○○·○·\n"
                   "1G|~··○·○○··\n"
                   "2D|~··○·○●··\n"
                   "3A|~··○○·○··\n"
                   "4E|~··○●·○··\n"
                   "5B|~···○·○··\n")


def test_render_minor_bass(capsys):
    Scale.render(scale='minor',
                 fretboard='bass')

    out, _ = capsys.readouterr()

    assert out == ("C D E♭ F G A♭ B♭\n"
                   "0C|~···○·○··\n"
                   "1G|~··○○·○··\n"
                   "2D|~···○·●··\n"
                   "3A|~···○·○○·\n"
                   "4E|~···●·○○·\n"
                   "5B|~···○○·○·\n")
