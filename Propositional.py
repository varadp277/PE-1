# Propositional variables
p = True   # Example: 'It is raining.'
q = False  # Example: 'It is sunny.'

# Logical operations
negation = not p                # ¬p
conjunction = p and q           # p ∧ q
disjunction = p or q            # p ∨ q
implication = (not p) or q      # p → q, equivalent to ¬p ∨ q
biconditional = (p and q) or (not p and not q)  # p ↔ q

print("¬p:", negation)
print("p ∧ q:", conjunction)
print("p ∨ q:", disjunction)
print("p → q:", implication)
print("p ↔ q:", biconditional)
