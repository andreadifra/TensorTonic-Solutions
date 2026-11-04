import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    """
    Returns null_counts as a dictionary of integers and cleaned_data as a dictionary of lists.
    """
    df = pd.DataFrame(data)
    cleaned_data = df.fillna(fill_value).to_dict('list')
    null_counts = df.isnull().sum().to_dict()
    return {"null_counts": null_counts,"cleaned_data": cleaned_data}
