import pandas as pd
import matplotlib.pyplot as plt

bonds = pd.read_csv("data/bond_portfolio_data.csv")
print(bonds.head())
print(bonds.columns)

print(bonds.columns.tolist())
