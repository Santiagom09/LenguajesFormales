from Project.app.functions.subset_construction import convertir_nfa_a_dfa
from Project.app.models.schemas import NFARequest

# Ejemplo simplificado — ajusta las transiciones según lo que definas
# (aquí uso datos de prueba, no necesariamente el ejemplo exacto del PDF,
# porque el enunciado no mostró la lista completa de transitions)

nfa_prueba = NFARequest(
    states=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    alphabet=["a", "b"],
    initial=0,
    accepting=[8],
    transitions=[
        {"from": 0, "symbol": "a", "to": [1, 3, 7]},
        {"from": 0, "symbol": "b", "to": [1, 2]},
        {"from": 7, "symbol": "a", "to": [7]},
        {"from": 7, "symbol": "b", "to": [8]},
        {"from": 8, "symbol": "b", "to": [8]},
        # completa aquí el resto según lo que quieras probar
    ],
)

dfa_estados, transiciones, aceptacion = convertir_nfa_a_dfa(nfa_prueba)

print("Estados DFA:", dfa_estados)
print("Transiciones:", transiciones)
print("Estados de aceptación:", aceptacion)
