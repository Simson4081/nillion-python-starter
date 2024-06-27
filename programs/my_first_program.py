from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computation (e.g., addition)
    result = my_int1 + my_int2

    # Define the output based on the computation result
    return [Output(result, "my_output", party1)]