from finite_automaton import FiniteAutomaton

# States S0, S1, S2 represent remainder 0, 1, 2 respectively
states = {'S0', 'S1', 'S2'}
alphabet = {'0', '1'}
initial_state = 'S0'
final_states = {'S0', 'S1', 'S2'}  # All states are final, mapping to their respective remainders

# Transitions as shown in the example:
# S0 --1--> S1
# S1 --1--> S0
# S0 --0--> S0
transitions = {
    ('S0', '1'): 'S1',  # When in S0 and see 1, go to S1
    ('S1', '1'): 'S0',  # When in S1 and see 1, go to S0
    ('S0', '0'): 'S0',  # When in S0 and see 0, stay in S0
    ('S1', '0'): 'S2',  # Complete the transition table
    ('S2', '0'): 'S1',  # Complete the transition table
    ('S2', '1'): 'S2',  # Complete the transition table
}

mod_three = FiniteAutomaton[str, str](
    states=states,
    alphabet=alphabet,
    initial_state=initial_state,
    final_states=final_states,
    transitions=transitions
) 