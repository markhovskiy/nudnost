# gnb-scales

  [![license][license-image]][license-url]
  ![code size][code-size-image]

CLI utility to draw guitar/bass scales.

## Status

*Experimental* - only 2 scales are supported.

## How does it look like?

```
(major, guitar)     (minor, bass)

C D E F G A B       C D E♭ F G A♭ B♭

1E|~··○●·○··        0C|~···○·○··
2B|~···○·○··        1G|~··○○·○··
3G|~··○·○○··        2D|~···○·●··
4D|~··○·○●··        3A|~···○·○○·
5A|~··○○·○··        4E|~···●·○○·
6E|~··○●·○··        5B|~···○○·○·
7B|~···○·○··
```

## How to run it?

```bash
$ python render-scale.py [-h] {major,minor} {bass,guitar}
```

## Development setup

```bash
$ mkvirtualenv --python=/usr/local/bin/python3 gnb-scales
$ pip install -r requirements.txt
$ pep8 --show-source .
$ py.test utils/tests/
```

## Resources

* https://www.guitarcommand.com/guitar-scales and https://www.guitarcommand.com/guitar-scales/bass-scales
* http://www.angelfire.com/id/bass (so 1998 but lots of examples)

[license-image]: https://img.shields.io/github/license/oleksmarkh/gnb-scales.svg?style=flat-square
[license-url]: https://github.com/oleksmarkh/gnb-scales/blob/master/LICENSE
[code-size-image]: https://img.shields.io/github/languages/code-size/oleksmarkh/gnb-scales.svg?style=flat-square
