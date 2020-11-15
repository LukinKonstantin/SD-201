import pandas as pd

from decision_functions import (
    BuildDecisionTree,
    printDecisionTree,
)

def main():
    d  = 0
    alpha = .5
    min_num = 5
    df = pd.read_csv('data/data.csv')
    BuildDecisionTree(df, 3, min_num)
    with open('output_tree.txt', 'w') as f:
        f.write(printDecisionTree(root, df.columns))


if __name__ == '__main__':
    main()