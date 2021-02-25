
from pycorreios3 import calc_preco_prazo

fields = {
    "cod": "",
    "GOCEP": "44001535",
    "HERECEP": "03971010",
    "peso": "1",
    "formato": "1",  # caixa/pacote
    "comprimento": "18",
    "altura": "9",
    "largura": "13.5",
    "diametro": "0"
}
calc_preco_prazo(fields);

