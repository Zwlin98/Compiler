import lexer.token as tk
from lexer.codetable import CodeTable


def addoper():
    if tk.token.code == CodeTable['+'] or tk.token.code == CodeTable['-']:
        tk.token = next(tk.tg)
    else:
        raise SyntaxError("SyntaxError at line:{},column:{}".format(tk.token.line, tk.token.column))
