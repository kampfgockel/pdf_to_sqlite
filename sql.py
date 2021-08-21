
# %%
from sqlalchemy import create_engine
import pandas as pd
# %%
engine = create_engine('sqlite:///db.sqlite3') # create_engine('sqlite://', echo=False)

# %%
df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})
# %%
df.to_sql('users', con=engine)
# %%
dfOne = pd.DataFrame(engine.execute("SELECT * FROM users").fetchall())
# %%
print(dfOne.head())
# %%
# pd.read_sql("SELECT * FROM my_table;", engine)
dfTwo = pd.read_sql_table('users', engine)
print(dfTwo.head())
# pd.read_sql_query("SELECT * FROM my_table;", engine)
# %%
