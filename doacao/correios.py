
from pycorreios.correios import Correios

fields = {
    "cod": Correios.SEDEX,
    "GOCEP": "44001535",
    "HERECEP": "03971010",
    "peso": "1",
    "formato": "1",  # caixa/pacote
    "comprimento": "18",
    "altura": "9",
    "largura": "13.5",
    "diametro": "0"
}

test = Correios().frete(**fields)  # remember to call with **

# or with positional parameters - same result as above
test = Correios().frete(Correios.SEDEX, '44001535', '03971010', 1, 1, 18, 9, 13.5, 0)

if test['Erro'] != '0':
    print
    'Deu erro! :('
    print
    test['Erro']
    print
    test['MsgErro']
else:
    print
    "Valor: R$%s\nPrazo de Entrega: %s" % (test['Valor'], test['PrazoEntrega'])

