# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Customers = dataiku.Dataset("Customers")
Customers_df = Customers.get_dataframe()

# TESTING DTIKU ROBERTO WITH DSS
# TESTING 2 branched


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

TEST_df = Customers_df # For this sample code, simply copy input to output


# Write recipe outputs
TEST = dataiku.Dataset("TEST")
TEST.write_with_schema(TEST_df)
