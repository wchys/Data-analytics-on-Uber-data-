# -*- coding: utf-8 -*-
"""(Transformation) uber_transformation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1epH4n9O5Zl9tlhJZMQs4kqGfhc15mD0y
"""

import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    
    #Converting the 'tpep_pickup_datetime' and 'tpep_dropoff_datetime' columns to datetime format:
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    #Removing duplicate rows from the DataFrame and resetting the index:
    df = df.drop_duplicates().reset_index(drop=True)

    #Adding a new column 'trip_id' to the DataFrame using the index values:
    df['trip_id'] = df.index

    #Creating a new DataFrame 'datetime_dim' containing selected columns from the original DataFrame:
    datetime_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].reset_index(drop=True)

    #Extracting various date and time components from the 'tpep_pickup_datetime' column:
    datetime_dim['tpep_pickup_datetime'] = datetime_dim['tpep_pickup_datetime']
    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday

    #Extracting various date and time components from the 'tpep_dropoff_datetime' column:
    datetime_dim['tpep_dropoff_datetime'] = datetime_dim['tpep_dropoff_datetime']
    datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday

    #Adding a new column 'datetime_id' to the 'datetime_dim' DataFrame using the index values:
    datetime_dim['datetime_id'] = datetime_dim.index

    #Selecting and renaming columns in the 'datetime_dim' DataFrame:
    datetime_dim = datetime_dim[['datetime_id', 'tpep_pickup_datetime', 'pick_hour', 'pick_day', 'pick_month', 'pick_year', 'pick_weekday',
                                'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month', 'drop_year', 'drop_weekday']]

    #Creating a new DataFrame 'passenger_count_dim' containing the 'passenger_count' column:
    passenger_count_dim = df[['passenger_count']].reset_index(drop=True)

    #Adding a new column 'passenger_count_id' to the 'passenger_count_dim' DataFrame using the index values:
    passenger_count_dim['passenger_count_id'] = passenger_count_dim.index

    #Selecting and rearranging columns in the 'passenger_count_dim' DataFrame:
    passenger_count_dim = passenger_count_dim[['passenger_count_id','passenger_count']]

    #Creating a new DataFrame 'trip_distance_dim' containing the 'trip_distance' column:
    trip_distance_dim = df[['trip_distance']].reset_index(drop=True)

    #Adding a new column 'trip_distance_id' to the 'trip_distance_dim' DataFrame using the index values:
    trip_distance_dim['trip_distance_id'] = trip_distance_dim.index

    #Selecting and rearranging columns in the 'trip_distance_dim' DataFrame:
    trip_distance_dim = trip_distance_dim[['trip_distance_id','trip_distance']]

    #Defining a dictionary mapping rate code values to rate code names:
    rate_code_type = {
        1:"Standard rate",
        2:"JFK",
        3:"Newark",
        4:"Nassau or Westchester",
        5:"Negotiated fare",
        6:"Group ride"
    }

    #Creating a new DataFrame 'rate_code_dim' containing the 'RatecodeID' column:
    rate_code_dim = df[['RatecodeID']].reset_index(drop=True)

    #Adding new columns 'rate_code_id' and 'rate_code_name' to the 'rate_code_dim' DataFrame based on the rate code dictionary: 
    rate_code_dim['rate_code_id'] = rate_code_dim.index
    rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(rate_code_type)
    rate_code_dim = rate_code_dim[['rate_code_id','RatecodeID','rate_code_name']]

    #Creating a new DataFrame 'pickup_location_dim' containing the pickup latitude and longitude columns:
    pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].reset_index(drop=True)

    #Adding a new column 'pickup_location_id' to the 'pickup_location_dim' DataFrame using the index values:
    pickup_location_dim['pickup_location_id'] = pickup_location_dim.index

    #Selecting and rearranging columns in the 'pickup_location_dim' DataFrame:
    pickup_location_dim = pickup_location_dim[['pickup_location_id','pickup_latitude','pickup_longitude']] 

    #Creating a new DataFrame 'dropoff_location_dim' containing the dropoff latitude and longitude columns:
    dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].reset_index(drop=True)

    #Adding a new column 'dropoff_location_id' to the 'dropoff_location_dim' DataFrame using the index values:
    dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index

    #Selecting and rearranging columns in the 'dropoff_location_dim' DataFrame:
    dropoff_location_dim = dropoff_location_dim[['dropoff_location_id','dropoff_latitude','dropoff_longitude']]

    #Defining a dictionary mapping payment type values to payment type names:
    payment_type_name = {
        1:"Credit card",
        2:"Cash",
        3:"No charge",
        4:"Dispute",
        5:"Unknown",
        6:"Voided trip"
    }

    #Creating a new DataFrame 'payment_type_dim' containing the 'payment_type' column:
    payment_type_dim = df[['payment_type']].reset_index(drop=True)

    #Adding new columns 'payment_type_id' and 'payment_type_name' to the 'payment_type_dim' DataFrame based on the payment type dictionary:
    payment_type_dim['payment_type_id'] = payment_type_dim.index
    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)

    #Selecting and rearranging columns in the 'payment_type_dim' DataFrame:
    payment_type_dim = payment_type_dim[['payment_type_id','payment_type','payment_type_name']]

    #Creating the fact table by merging the various dimension tables with the original DataFrame:
    fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
             .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id') \
             .merge(rate_code_dim, left_on='trip_id', right_on='rate_code_id') \
             .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id') \
             .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')\
             .merge(datetime_dim, left_on='trip_id', right_on='datetime_id') \
             .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id') \
             [['trip_id','VendorID', 'datetime_id', 'passenger_count_id',
               'trip_distance_id', 'rate_code_id', 'store_and_fwd_flag', 'pickup_location_id', 'dropoff_location_id',
               'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
               'improvement_surcharge', 'total_amount']]

    return {"datetime_dim":datetime_dim.to_dict(orient="dict"),
    "passenger_count_dim":passenger_count_dim.to_dict(orient="dict"),
    "trip_distance_dim":trip_distance_dim.to_dict(orient="dict"),
    "rate_code_dim":rate_code_dim.to_dict(orient="dict"),
    "pickup_location_dim":pickup_location_dim.to_dict(orient="dict"),
    "dropoff_location_dim":dropoff_location_dim.to_dict(orient="dict"),
    "payment_type_dim":payment_type_dim.to_dict(orient="dict"),
    "fact_table":fact_table.to_dict(orient="dict")}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'