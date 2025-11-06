# Predicate: "x is greater than 5"
def P(x):
    return x > 5

# Universal quantifier: "All numbers in the list are > 5"
def for_all(lst, predicate):
    return all(predicate(x) for x in lst)

# Existential quantifier: "There exists a number in the list > 5"
def exists(lst, predicate):
    return any(predicate(x) for x in lst)

nums = [2, 7, 4, 10]

print("∃x P(x):", exists(nums, P))     # True, as 7 and 10 are > 5
print("∀x P(x):", for_all(nums, P))    # False, as 2 and 4 are not > 5
