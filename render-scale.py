import argparse

from utils.scale import Scale


parser = argparse.ArgumentParser(description="Draws bass/guitar scales\n\n"
                                             "|··○●·○···\n"
                                             "|···○·○···\n"
                                             "|··○·○○···\n"
                                             "|··○·○●···\n"
                                             "|··○○·○···\n"
                                             "|··○●·○···\n",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="\../")

parser.add_argument("scale", choices=Scale.scales,
                    help="Scale")
parser.add_argument("fretboard", choices=["bass", "guitar"],
                    help="Fretboard")
parser.add_argument("--strings", type=int, choices=range(4, 9),
                    help="Number of strings. "
                         "Defaults to 4 for bass and 6 for guitar'")

args = parser.parse_args()

scale = Scale(fretboard=args.fretboard,
              scale=args.scale,
              strings=args.strings)
scale.render()
