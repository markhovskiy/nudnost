# gnb-scales

[![Build Status](https://travis-ci.org/oleksmarkh/gnb-scales.svg)](https://travis-ci.org/oleksmarkh/gnb-scales)

CLI utility to draw guitar/bass scales


## usage

```bash
render-scale.py [-h] {major,minor} {bass,guitar}
```

```
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

1. `mkvirtualenv --python=/usr/bin/python3 gnb-scales`
2. `pip install -r requirements.txt`
