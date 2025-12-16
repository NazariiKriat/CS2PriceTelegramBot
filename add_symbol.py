import pandas as pd

                                                      #WE need this code because parser sometimes makes invisiable errors and it solves by adding 1 more symbol 
df = pd.read_csv('databases\LMG.csv')


print(f"Original shape: {df.shape}")


df_cleaned = df.drop_duplicates()

print(f"Shape after removing duplicates: {df_cleaned.shape}")


if len(df_cleaned.columns) > 1:
    column_name = df_cleaned.columns[1]  
    print(f"Adding symbol to column: '{column_name}'")
    
    
    df_cleaned.iloc[:, 1] = df_cleaned.iloc[:, 1].astype(str) + "1"
    
    
    print(f"\nFirst 5 rows of column '{column_name}':")
    print(df_cleaned.iloc[:5, 1].to_string(index=False))
else:
    print("Error: DataFrame has less than 2 columns!")


df_cleaned.to_csv('Snipers_cleaned.csv', index=False)


if 'Gun' in df_cleaned.columns and 'Skin' in df_cleaned.columns:
    duplicate_gun_skin = df.duplicated(subset=['Gun', 'Skin'], keep=False)
    print(f"\nRows with duplicate Gun+Skin combinations: {duplicate_gun_skin.sum()}")
    

    duplicate_examples = df[duplicate_gun_skin][['Gun', 'Skin']].drop_duplicates()
    print(f"\nExamples of duplicate Gun+Skin combinations:")
    print(duplicate_examples.head(10).to_string(index=False))
else:
    print("\nColumns 'Gun' and 'Skin' not found for duplicate check")