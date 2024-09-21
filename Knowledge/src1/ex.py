from logic import *

rain = Symbol("rain")
football = Symbol("football") 
table_tennis = Symbol("table tennis")  

knowledge = And(

    Implication(Not(rain), football),  # ¬(It is raining) → (rauf played cricket)

    Or(football, table_tennis),  # (Rauf played football) ∨ (Rauf played table tennis).

    Not(And(football, table_tennis)),  # ¬(Rauf played football ∧ Rauf played table tennis)

    football
    )

def check_all(knowledge, query, symbols, model):
    if not symbols:

        # If knowledge base is true in model, then query must also be true
        if knowledge.evaluate(model):
            return query.evaluate(model)
        return True
    else:

        # Choose one of the remaining unused symbols
        remaining = symbols.copy()
        p = remaining.pop()

        # Create a model where the symbol is true
        model_true = model.copy()
        model_true[p] = True

        # Create a model where the symbol is false
        model_false = model.copy()
        model_false[p] = False

        # Ensure entailment holds in both models
        return(check_all(knowledge, query, remaining, model_true) and check_all(knowledge, query, remaining, model_false))
    