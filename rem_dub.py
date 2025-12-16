import pandas as pd

                                                       #Sometimes Webscrapper script is making dublicates of items and this script delates them
df = pd.read_csv('LMG.csv')


print(f"Original shape: {df.shape}")

df_cleaned = df.drop_duplicates()

print(f"Shape after removing duplicates: {df_cleaned.shape}")


duplicates_removed = df.shape[0] - df_cleaned.shape[0]
print(f"Duplicates removed: {duplicates_removed}")


df_cleaned.to_csv('Snipers_cleaned.csv', index=False)


duplicate_gun_skin = df.duplicated(subset=['Gun', 'Skin'], keep=False)
print(f"\nRows with duplicate Gun+Skin combinations: {duplicate_gun_skin.sum()}")


duplicate_examples = df[duplicate_gun_skin][['Gun', 'Skin']].drop_duplicates()
print(f"\nExamples of duplicate Gun+Skin combinations:")
print(duplicate_examples.head(10).to_string(index=False))