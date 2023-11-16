import click
import numpy as np
import pandas as pd
from numpy import pi


# Define the main Click group
@click.group()
def main():
    pass


# Command for Sin
@main.command()
@click.option("-n", "--number", default=1, help="Choose a number", show_default=True)
def sin(number):
    """List input values (x) and the output values (sin(x)) with a chosen sampling amount of values of x between 0 and 2pi

    Args:
        number (int): number of samples
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


# Command for Tan
@main.command()
@click.option("-n", "--number", default=1, help="Choose a number", show_default=True)
def tan(number):
    """List input values (x) and the output values (tan(x)) with a chosen sampling amount of values of x between 0 and 2pi

    Args:
        number (int): number of samples
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    main()
