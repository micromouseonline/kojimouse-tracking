
from pyqtgraph.Qt import QtCore, QtWidgets, QtGui

color_map_10a = [
    QtGui.QColor(166, 206, 227),
    QtGui.QColor(31, 120, 180),
    QtGui.QColor(178, 223, 138),
    QtGui.QColor(51, 160, 44),
    QtGui.QColor(251, 154, 153),
    QtGui.QColor(227, 26, 28),
    QtGui.QColor(253, 191, 111),
    QtGui.QColor(255, 127, 0),
    QtGui.QColor(202, 178, 214),
    QtGui.QColor(106, 61, 154)
]
color_map_10b = [
    QtGui.QColor(141, 211, 199),
    QtGui.QColor(255, 255, 179),
    QtGui.QColor(190, 186, 218),
    QtGui.QColor(251, 128, 114),
    QtGui.QColor(128, 177, 211),
    QtGui.QColor(253, 180, 98),
    QtGui.QColor(179, 222, 105),
    QtGui.QColor(252, 205, 229),
    QtGui.QColor(217, 217, 217),
    QtGui.QColor(188, 128, 189),
]

color_map_tol_qualitative_10 = [
    QtGui.QColor('#332288'),
    QtGui.QColor('#88ccee'),
    QtGui.QColor('#44aa99'),
    QtGui.QColor('#117733'),
    QtGui.QColor('#999933'),
    QtGui.QColor('#ddcc77'),
    QtGui.QColor('#661100'),
    QtGui.QColor('#cc6677'),
    QtGui.QColor('#882255'),
    QtGui.QColor('#aa4499'),
    QtGui.QColor('#ffffff'),
]

color_map_tol_divergent_10 = [
    QtGui.QColor('#3c53a1'),
    QtGui.QColor('#408ccb'),
    QtGui.QColor('#83c1ec'),
    QtGui.QColor('#c7e8fc'),
    QtGui.QColor('#f1f9ed'),
    QtGui.QColor('#fef0bf'),
    QtGui.QColor('#f8cc89'),
    QtGui.QColor('#ea9461'),
    QtGui.QColor('#d75448'),
    QtGui.QColor('#aa1c3b'),
    QtGui.QColor('#ffffff'),
]
color_map_tol_sequential_10 = [
    QtGui.QColor('#ffffe4'),
    QtGui.QColor('#fff7c5'),
    QtGui.QColor('#ffe798'),
    QtGui.QColor('#ffce65'),
    QtGui.QColor('#fdac3a'),
    QtGui.QColor('#f7861c'),
    QtGui.QColor('#e5610c'),
    QtGui.QColor('#c24406'),
    QtGui.QColor('#923004'),
    QtGui.QColor('#662404'),
    QtGui.QColor('#ffffff'),

]
color_map_tol_rainbow_10 = [
    QtGui.QColor('#781c81'),
    QtGui.QColor('#43328d'),
    QtGui.QColor('#416fb8'),
    QtGui.QColor('#519cb8'),
    QtGui.QColor('#70b484'),
    QtGui.QColor('#99bd5c'),
    QtGui.QColor('#c3ba45'),
    QtGui.QColor('#e0a239'),
    QtGui.QColor('#e66b2d'),
    QtGui.QColor('#d92120'),
    QtGui.QColor('#ffffff'),
]

# qualitative colors from https://carto.com/carto-colors/
antique = [
    QtGui.QColor('#855C75'),
    QtGui.QColor('#D9AF6B'),
    QtGui.QColor('#AF6458'),
    QtGui.QColor('#736F4C'),
    QtGui.QColor('#526A83'),
    QtGui.QColor('#625377'),
    QtGui.QColor('#68855C'),
    QtGui.QColor('#9C9C5E'),
    QtGui.QColor('#A06177'),
    QtGui.QColor('#8C785D'),
    QtGui.QColor('#467378'),
    QtGui.QColor('#7C7C7c')
]
bold = [
    QtGui.QColor('#7F3C8D'),
    QtGui.QColor('#11A579'),
    QtGui.QColor('#3969AC'),
    QtGui.QColor('#F2B701'),
    QtGui.QColor('#E73F74'),
    QtGui.QColor('#80BA5A'),
    QtGui.QColor('#E68310'),
    QtGui.QColor('#008695'),
    QtGui.QColor('#CF1C90'),
    QtGui.QColor('#f97b72'),
    QtGui.QColor('#4b4b8f'),
    QtGui.QColor('#A5AA99')
]
pastel = [
    QtGui.QColor('#66C5CC'),
    QtGui.QColor('#F6CF71'),
    QtGui.QColor('#F89C74'),
    QtGui.QColor('#DCB0F2'),
    QtGui.QColor('#87C55F'),
    QtGui.QColor('#9EB9F3'),
    QtGui.QColor('#FE88B1'),
    QtGui.QColor('#C9DB74'),
    QtGui.QColor('#8BE0A4'),
    QtGui.QColor('#B497E7'),
    QtGui.QColor('#D3B484'),
    QtGui.QColor('#B3B3B3')
]

prism = [
    QtGui.QColor('#5F4690'),
    QtGui.QColor('#1D6996'),
    QtGui.QColor('#38A6A5'),
    QtGui.QColor('#0F8554'),
    QtGui.QColor('#73AF48'),
    QtGui.QColor('#EDAD08'),
    QtGui.QColor('#E17C05'),
    QtGui.QColor('#CC503E'),
    QtGui.QColor('#94346E'),
    QtGui.QColor('#6F4070'),
    QtGui.QColor('#994E95'),
    QtGui.QColor('#666666'),
]

safe = [
    QtGui.QColor('#88CCEE'),
    QtGui.QColor('#CC6677'),
    QtGui.QColor('#DDCC77'),
    QtGui.QColor('#117733'),
    QtGui.QColor('#332288'),
    QtGui.QColor('#AA4499'),
    QtGui.QColor('#44AA99'),
    QtGui.QColor('#999933'),
    QtGui.QColor('#882255'),
    QtGui.QColor('#661100'),
    QtGui.QColor('#6699CC'),
    QtGui.QColor('#888888'),
]

vivid = [
    QtGui.QColor('#E58606'),
    QtGui.QColor('#5D69B1'),
    QtGui.QColor('#52BCA3'),
    QtGui.QColor('#99C945'),
    QtGui.QColor('#CC61B0'),
    QtGui.QColor('#24796C'),
    QtGui.QColor('#DAA51B'),
    QtGui.QColor('#2F8AC4'),
    QtGui.QColor('#764E9F'),
    QtGui.QColor('#ED645A'),
    QtGui.QColor('#CC3A8E'),
    QtGui.QColor('#A5AA99'),
]

hsl12 = [
    QtGui.QColor('#b80100'),
    QtGui.QColor('#b85d00'),
    QtGui.QColor('#b6b800'),
    QtGui.QColor('#5bb800'),
    QtGui.QColor('#00b801'),
    QtGui.QColor('#00b85d'),
    QtGui.QColor('#00b6b8'),
    QtGui.QColor('#005bb8'),
    QtGui.QColor('#0100b8'),
    QtGui.QColor('#5d00b8'),
    QtGui.QColor('#b800b6'),
    QtGui.QColor('#b8005b'),
]

category_dark_14 = [
    QtGui.QColor('#6929c4'),
    QtGui.QColor('#1192e8'),
    QtGui.QColor('#005d5d'),
    QtGui.QColor('#9f1853'),
    QtGui.QColor('#fa4d56'),
    QtGui.QColor('#570408'),
    QtGui.QColor('#198038'),
    QtGui.QColor('#002d9c'),
    QtGui.QColor('#ee538b'),
    QtGui.QColor('#b28600'),
    QtGui.QColor('#009d9a'),
    QtGui.QColor('#012749'),
    QtGui.QColor('#8a3800'),
    QtGui.QColor('#a56eff'),
]

category_light_14 = [
    QtGui.QColor('#8a3ffc'),
    QtGui.QColor('#33b1ff'),
    QtGui.QColor('#007d79'),
    QtGui.QColor('#ff7eb6'),
    QtGui.QColor('#fa4d56'),
    QtGui.QColor('#fff1f1'),
    QtGui.QColor('#6fdc8c'),
    QtGui.QColor('#4589ff'),
    QtGui.QColor('#d12771'),
    QtGui.QColor('#d2a106'),
    QtGui.QColor('#08bdba'),
    QtGui.QColor('#bae6ff'),
    QtGui.QColor('#ba4e00'),
    QtGui.QColor('#d4bbff'),
]
