def construir_mapa_transiciones(transitions: list) -> dict:
    mapa = {}
    for transicion in transitions:
        origen = transicion.from_state
        simbolo = transicion.symbol
        destinos = transicion.to
        if origen not in mapa:
            mapa[origen] = {}
        mapa[origen][simbolo] = destinos
    return mapa


def mover(conjunto_estados: set, simbolo: str, mapa_transiciones: dict) -> set:
    resultado = set()
    for estado in conjunto_estados:
        if estado in mapa_transiciones and simbolo in mapa_transiciones[estado]:
            resultado.update(mapa_transiciones[estado][simbolo])
    return resultado


def formatear_estado(conjunto_estados: frozenset) -> str:
    if not conjunto_estados:
        return "∅"
    return "".join(str(estado) for estado in sorted(conjunto_estados))


def construir_dfa_por_subconjuntos(
    q0: int,
    alfabeto: list[str],
    mapa_transiciones: dict,
    estados_aceptacion: list[int],
) -> tuple[list[str], list[dict], list[str], str]:
    inicial_dfa = frozenset({q0})
    cola = [inicial_dfa]
    visitados = {inicial_dfa}
    transiciones_dfa = {}

    while cola:
        actual = cola.pop(0)
        for simbolo in alfabeto:
            destino = frozenset(mover(actual, simbolo, mapa_transiciones))
            transiciones_dfa[(actual, simbolo)] = destino
            if destino not in visitados:
                visitados.add(destino)
                cola.append(destino)

    dfa_estados = [formatear_estado(estado) for estado in visitados]
    aceptacion = [
        formatear_estado(estado)
        for estado in visitados
        if any(estado_aceptacion in estado for estado_aceptacion in estados_aceptacion)
    ]
    transiciones = [
        {
            "from": formatear_estado(origen),
            "symbol": simbolo,
            "to": formatear_estado(destino),
        }
        for (origen, simbolo), destino in transiciones_dfa.items()
    ]

    return dfa_estados, transiciones, aceptacion, formatear_estado(inicial_dfa)


def convertir_nfa_a_dfa(nfa) -> tuple[list[str], list[dict], list[str], str]:
    mapa_transiciones = construir_mapa_transiciones(nfa.transitions)
    return construir_dfa_por_subconjuntos(
        nfa.initial,
        nfa.alphabet,
        mapa_transiciones,
        nfa.accepting,
    )


def simular_cadena(dfa, cadena: str) -> tuple[list[str], bool]:
    mapa = {}
    for t in dfa.transitions:
        mapa[(t.from_state, t.symbol)] = t.to

    estado_actual = dfa.initial
    path = [estado_actual]

    for simbolo in cadena:
        siguiente_estado = mapa.get((estado_actual, simbolo))
        if siguiente_estado is None:
            return path, False
        estado_actual = siguiente_estado
        path.append(estado_actual)

    accepted = estado_actual in dfa.acceptingStates
    return path, accepted



