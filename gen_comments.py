import pandas as pd

# Import df
df = pd.read_pickle('scrapedb_comments.pkl')
#df.reset_index(inplace=True)

# Output total files
done = 0
print("Total ids: ", set(df['id_val']))

# Go through each id_val
for id_val_unique in set(df['id_val']):
	dftemp = df.loc[df['id_val']==id_val_unique]

	# Json file name
	file_name = id_val_unique+'.json'

	# Save
	dftemp.to_json(file_name, orient="records")
	done+=1

	if(done%100==0):
		print(f"Completed {done}.")
	
