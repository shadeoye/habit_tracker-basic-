
#track my habits throughout the week

PGHOST=localhost
PGDATABASE=habit_tracker

import psycopg2
import sys, os
import numpy as np
import pandas as pd
import example_psql as creds
import pandas.io.sql as psq


habits = {}

while True:
    habits['bedtime'] = input("What time did you go to bed\n")
    habits['wake_up'] = input("What time did you wake up\n")
    habits['coding'] = input("how long did you spend coding\n")
    habits['reading'] = input("how long did you spend reading \n")

    cont = input("Are you tracking any other habits\n\n")
    if not cont.lower() in ("y", "yes"):
        break

print(habits)

