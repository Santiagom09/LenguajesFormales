from Project.app.functions.subset_construction import convertir_nfa_a_dfa, simular_cadena
from Project.app.models.schemas import DFAResponse, NFARequest, SimulateRequest, SimulateResponse


def procesar_conversion(nfa: NFARequest) -> DFAResponse:
    if nfa.initial not in nfa.states:
        raise ValueError("El estado inicial no está en la lista de estados")

    if not all(x in nfa.states for x in nfa.accepting):
        raise ValueError("Hay estados de aceptación que no están en la lista de estados")

    try:
        dfa_estados, transiciones, aceptacion, inicial = convertir_nfa_a_dfa(nfa)
    except Exception as error:
        raise ValueError(f"Error al convertir el NFA: {error}")

    return DFAResponse(
        dfaStates=dfa_estados,
        transitions=transiciones,
        acceptingStates=aceptacion,
        initial=inicial,
    )


def procesar_simulacion(request: SimulateRequest) -> SimulateResponse:
    try:
        path, accepted = simular_cadena(request.dfa, request.input)
    except Exception as error:
        raise ValueError(f"Error al simular la cadena: {error}")

    return SimulateResponse(path=path, accepted=accepted)