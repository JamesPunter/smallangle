import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def function_group():
    """Calculate tan and sin of values.
    """    
    pass

@function_group.command()
@click.option(
    "-n", 
    "--number",
    default = 10,
    help= "Number of steps taken between 0 and 2pi.",
    show_default= True)
def sin(number):
    """Calculate sine for values.

    Calculate sine for values between 0 and 2pi 
    in a certain amount of steps.
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
   
@function_group.command()
@click.option(
    "-n", 
    "--number",
    default = 10,
    help= "Number of steps taken between 0 and 2pi.",
    show_default=True)
def tan(number):
    """Calculate tangent for values.

    Calculate tangent for values between 0 and 2pi 
    in a certain amount of steps.
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

@function_group.command()
@click.argument("epsilon", type=float)
@click.argument("number", type=int)
def approx(epsilon, number):
    """Check if small-angle approximation holds.

    Function calculates x - sin(x) and compares it to given
    value of epsilon. If (x-sin(x)) <= epsilon, the approximation holds.

    Args:
        epsilon (float): Certain small value.
        number (int): Number of steps taken between 0 and 2pi.
    """    
    list_smaller_than_epsilon = []
    x = np.linspace(0, 2 * pi, number)
    for calculation in x:
        if abs(calculation - np.sin(calculation)) <= epsilon:
            list_smaller_than_epsilon.append(calculation)
        else:
            pass
    print(f"For an accuracy of {epsilon}, the small-angle approximation holds up to x = {list_smaller_than_epsilon[-1]}")
    
if __name__ == "__main__":
    function_group(10)
