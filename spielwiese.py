import pandas as pd
df=pd.read_csv("dummy.csv")
df.set_index("country",inplace=True)
df.to_json("dummy.json")

# Group DataFrame by 'City' column and convert to nested JSON
#grouped_data = df.groupby('cat').apply(lambda x: x[['val1', 'val2']].to_json("dummy2.json"))
 
# Print the grouped data
#print(grouped_data)