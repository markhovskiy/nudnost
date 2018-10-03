# gnb-scales

[![Build Status](https://travis-ci.org/oleksmarkh/gnb-scales.svg)](https://travis-ci.org/oleksmarkh/gnb-scales)

CLI utility to draw guitar/bass scales.

## usage

```bash
$ python render-scale.py [-h] {major,minor} {bass,guitar}
```

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

## setup

```bash
$ mkvirtualenv --python=/usr/local/bin/python3 gnb-scales
$ pip install -r requirements.txt
```

## see

* https://www.guitarcommand.com/guitar-scales and https://www.guitarcommand.com/guitar-scales/bass-scales
* http://www.angelfire.com/id/bass (so 1998 but lots of examples)
