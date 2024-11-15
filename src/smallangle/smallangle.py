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
@click.argument("name")
@click.option(
    "-n", 
    "--number",
    default=10,
    help="Number of steps taken between 0 and 2*pi.",
    show_default=True)
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
    default=10,
    help="Number of steps taken between 0 and 2*pi.",
    show_default=True)
def tan(number):
    """Calculate tangent for values.
    
    Calculate tangent for values between 0 and 2pi 
    in a certain amount of steps.
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    function_group(10)
