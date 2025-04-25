from threading import Lock

leituras_por_ambiente = {}
lock = Lock()

def atualizar_leitura(ambiente, tipo, valor):
    with lock:
        if ambiente not in leituras_por_ambiente:
            leituras_por_ambiente[ambiente] = {}
        leituras_por_ambiente[ambiente][tipo] = valor

def get_leituras():
    with lock:
        return dict(leituras_por_ambiente)
