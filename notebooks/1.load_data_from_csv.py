def load_ecommerce_data(month):
    """
    Load eCommerce event data for a given month.

    Parameters:
    month (str): "Oct", "Nov", or "All"

    Returns:
    Spark DataFrame
    """

    base_path = "/Volumes/workspace/ecommerce/ecommerce_data"

    if month == "Oct":
        path = f"{base_path}/2019-Oct.csv"
    elif month == "Nov":
        path = f"{base_path}/2019-Nov.csv"
    elif month == "All":
        path = f"{base_path}/*.csv"
    else:
        raise ValueError("Month must be 'Oct', 'Nov', or 'All'")

    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(path)
    )

    return df


# Load your data
events = load_ecommerce_data("Oct")

# Verify it's working
print(f"✅ Ready to go! Loaded {events.count():,} events")
events.show(5)
events.filter(events.price>1000).show(10)
