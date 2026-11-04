import pandas as pd

def concat_dataframes(dfs: list) -> list:
    """
    Returns [shape, data], with shape [rows, columns] and data a dictionary of lists.
    """
    data = pd.concat([pd.DataFrame(df) for df in dfs])
    return [
        list(data.shape),
        data.to_dict("list")
    ]