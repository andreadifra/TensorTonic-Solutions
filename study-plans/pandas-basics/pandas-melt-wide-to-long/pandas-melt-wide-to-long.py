import pandas as pd

def melt_dataframe(data: dict, id_vars: list, value_vars: list) -> dict:
    """
    Returns identifier column lists together with variable and value lists.
    """
    df = pd.DataFrame(data)
    return pd.melt(df, id_vars=id_vars, value_vars=value_vars).to_dict('list')
