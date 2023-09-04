import pandas as pd
import pymongo

pd.set_option('display.max_columns', None)

client = pymongo.MongoClient('localhost', 27017)
db = client['Slack_Apps']
collection = db['slack_apps']
data = collection.find()


# Convert the cursor to a list of dictionaries and create a DataFrame
df = pd.DataFrame(list(data), columns=['date', 'category', 'ranking', 'app_name', 'supported_languages', 'pricing', 'app_description'])


df['date'] = pd.to_datetime(df['date'])
df['ranking'] = pd.to_numeric(df['ranking'], errors='coerce')



df_sorted = df.sort_values(by=['category', 'ranking'])


category_test = df_sorted[df_sorted['category'] == 'Design']
print(category_test)


