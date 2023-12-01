# User inputs
file_name = "Day 1.txt"

# Libraries
import pandas as pd
import regex as re

pd.options.mode.chained_assignment = None  # default='warn'

dat = pd.read_csv("C:/Users/marla/OneDrive/Desktop/Advent of Code 2023/" + file_name, sep = " ", header = None)
df = pd.DataFrame(dat)
df.columns = ["input_value"]

# Puzzle 1
df["total"] = 0

for idx, row in df.iterrows():
    df["total"].loc[idx] = pd.to_numeric(re.findall(r'[0-9]', row["input_value"])[0] + re.findall(r'[0-9]', row["input_value"])[-1])

sum(df["total"])

# Puzzle 2
number_list = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'

number_df = pd.DataFrame()
number_df["text"] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine","1","2","3","4","5","6","7","8","9"]
number_df["num_text"] = ["1","2","3","4","5","6","7","8","9","1","2","3","4","5","6","7","8","9"]

df["first_val"] = "0"
df["last_val"] = "0"

for idx, row in df.iterrows():
    df["first_val"].loc[idx] = re.findall(number_list, row["input_value"], overlapped=True)[0]
    df["last_val"].loc[idx] = re.findall(number_list, row["input_value"], overlapped=True)[-1]

df = df.merge(number_df
         , left_on = 'first_val'
         , right_on = 'text'
         , how = 'left')

df.rename(columns={'num_text': 'first_val_num'}, inplace=True)

df = df.merge(number_df
         , left_on = 'last_val'
         , right_on = 'text'
         , how = 'left')

df.rename(columns={'num_text': 'last_val_num'}, inplace=True)

df["total"] = pd.to_numeric(df["first_val_num"] + df["last_val_num"])
sum(df["total"])