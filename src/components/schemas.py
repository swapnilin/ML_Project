# src/flight_analytics/ingestion/schemas.py

"""
Schemas for Flight Analytics Project using Pandera.

This defines expected data structure, types, categorical constraints,
and numeric checks. It acts as a contract for incoming datasets.
"""

# -----------------------------
# Allowed categories
# -----------------------------
FLIGHT_CATEGORIES = {
    "origin": ["JFK", "LAX", "SFO", "ORD", "ATL"],
    "destination": ["JFK", "LAX", "SFO", "ORD", "ATL"],
    "status": ["on_time", "delayed", "cancelled"],
    "airline": ["Delta", "United", "American", "Southwest"],
}

# -----------------------------
# Pandera Schema
# -----------------------------
try:
    import pandera as pa
    from pandera import Column, DataFrameSchema, Check

    FLIGHT_SCHEMA = DataFrameSchema(
        {
            "flight_id": Column(int, checks=Check.ge(0)),  # ID >= 0
            "departure_time": Column(pa.DateTime),
            "arrival_time": Column(pa.DateTime),
            "origin": Column(str, checks=Check.isin(FLIGHT_CATEGORIES["origin"])),
            "destination": Column(str, checks=Check.isin(FLIGHT_CATEGORIES["destination"])),
            "duration": Column(float, checks=Check.ge(0)),  # duration >=0
            "airline": Column(str, checks=Check.isin(FLIGHT_CATEGORIES["airline"])),
            "status": Column(str, checks=Check.isin(FLIGHT_CATEGORIES["status"])),
        },
        strict=True,  # no extra columns allowed
        coerce=True,  # cast types automatically
    )

except ImportError:
    FLIGHT_SCHEMA = None
    print("Pandera not installed: advanced validation disabled.")


# -----------------------------
# Optional: Pandas-based validation
# -----------------------------
import pandas as pd

def validate_categories(df: pd.DataFrame, categories: dict = FLIGHT_CATEGORIES):
    """
    Checks that categorical columns only contain allowed values.
    Raises ValueError if invalid values exist.
    """
    for col, allowed in categories.items():
        if col in df.columns:
            invalid_values = set(df[col].unique()) - set(allowed)
            if invalid_values:
                raise ValueError(
                    f"Column '{col}' has invalid values: {invalid_values}"
                )
    return True


def validate_schema(df: pd.DataFrame):
    """
    Validate dataframe using Pandera if available, else fallback to basic checks.
    """
    if FLIGHT_SCHEMA is not None:
        # Pandera validation
        FLIGHT_SCHEMA.validate(df, lazy=True)  # lazy=True reports all errors at once
    else:
        # Basic Pandas validation
        required_cols = [
            "flight_id", "departure_time", "arrival_time",
            "origin", "destination", "duration",
            "airline", "status"
        ]
        missing_cols = [c for c in required_cols if c not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")

        # Type checks
        dtype_map = {
            "flight_id": "int64",
            "departure_time": "datetime64[ns]",
            "arrival_time": "datetime64[ns]",
            "origin": "object",
            "destination": "object",
            "duration": "float64",
            "airline": "object",
            "status": "object",
        }
        for col, expected_dtype in dtype_map.items():
            if str(df[col].dtype) != expected_dtype:
                raise TypeError(f"Column '{col}' has dtype {df[col].dtype}, expected {expected_dtype}")

        # Category check
        validate_categories(df)
        # Numeric checks
        if (df["flight_id"] < 0).any():
            raise ValueError("flight_id contains negative values")
        if (df["duration"] < 0).any():
            raise ValueError("duration contains negative values")
