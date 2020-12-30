## FOR LOADER
HUE_DICT = {
    "red": [-30, 30],
    "yellow": [30, 90],
    "green": [90, 150],
    "cyan": [150, 210],
    "blue": [210, 270],
    "purple": [270, 330],
}
ALPHABET_NUM = 26
DICT_FOR_NAME_CONVERT = {
    ("C", "c", "ド", ("ﾄ", "ﾞ")): ("C", True),
    ("D", "d", "レ", "ﾚ"): ("D", True),
    ("E", "e", "ミ", "ﾐ"): ("E", True),
    ("F", "f", ("フ", "ァ"), ("ﾌ", "ｧ")): ("F", True),
    ("G", "g", "ソ", "ｿ"): ("G", True),
    ("A", "a", "ラ", "ﾗ"): ("A", True),
    ("H", "h", "シ", "ｼ"): ("H", True),
    ("♯", "＃", "#", ("i", "s")): ("is", False),
    ("♭", "ｂ", "b", ("e", "s")): ("es", False),
    ("・", "･", "."): ("r", True),
}
DICT_FOR_CONVERT_GERMAN2JAPAN = {
    "C": "ド",
    "Cis": "ド♯",
    "Des": "レ♭",
    "D": "レ",
    "Dis": "レ♯",
    "Es": "ミ♭",
    "E": "ミ",
    "Eis": "ミ♯",
    "Fes": "ﾌｧ♭",
    "F": "ﾌｧ",
    "Fis": "ﾌｧ♯",
    "Ges": "ソ♭",
    "G": "ソ",
    "Gis": "ソ♯",
    "As": "ラ♭",
    "A": "ラ",
    "Ais": "ラ♯",
    "B": "シ♭",
    "H": "シ",
    "His": "シ♯",
}
DICT_FOR_CONVERT_GERMAN2JAPAN_SHORTEN = {
    "C": "C",
    "Cis": "C#",
    "Des": "ﾚb",
    "D": "ﾚ",
    "Dis": "ﾚ#",
    "Es": "ﾐb",
    "E": "ﾐ",
    "Eis": "ﾐ#",
    "Fes": "Fb",
    "F": "F",
    "Fis": "F#",
    "Ges": "ｿb",
    "G": "ｿ",
    "Gis": "ｿ#",
    "As": "ﾗb",
    "A": "ﾗ",
    "Ais": "ﾗ#",
    "B": "ｼb",
    "H": "ｼ",
    "His": "ｼ#",
}
DICT_FOR_OCTAVE = {
    "minus1": 0,
    "plus1": 2,
    "plus2": 3,
}
