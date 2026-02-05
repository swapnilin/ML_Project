
"""
from flight_analytics.ingestion.schemas import validate_schema
import pandas as pd

df = pd.read_csv("raw_flights.csv")
validate_schema(df)  # raises descriptive errors if invalid
"""