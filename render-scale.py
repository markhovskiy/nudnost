import argparse

from utils.scale import Scale


parser = argparse.ArgumentParser(description="Draws bass/guitar scales\n\n"
                                             "1E|~··○●·○···\n"
                                             "2B|~···○·○···\n"
                                             "3G|~··○·○○···\n"
                                             "4D|~··○·○●···\n"
                                             "5A|~··○○·○···\n"
                                             "6E|~··○●·○···\n"
                                             "7B|~···○·○···\n",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="\../")

parser.add_argument("scale", choices=Scale.scales,
                    help="Scale")
parser.add_argument("fretboard", choices=Scale.matrices,
                    help="Fretboard")

args = parser.parse_args()

Scale.render(scale=args.scale,
             fretboard=args.fretboard)
