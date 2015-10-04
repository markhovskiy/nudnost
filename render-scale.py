import argparse

from utils.scale import Scale


parser = argparse.ArgumentParser()

parser.add_argument('--fretboard', default=None,
                    help="None|'bass'|'guitar'")

args = parser.parse_args()

scale = Scale(fretboard=args.fretboard)
scale.render()
