import os 
import json 
from sklearn.model_selection import train_test_split # to split data into two sets 


# lets define the paths 
LABELED_DIR= "data/labeled"
OUTPUT_PATH= "data/dataset.json"


all_data=[]


# lets read data from labeled files ,(each is the list of token Dict)
for filename in os.listdir(LABELED_DIR): # it goes through every  file name inside the data/labeled 
    if filename.endswith(".json"):# check si the current fil is json 
        file_path= os.path.join(LABELED_DIR,filename)
        with open(file_path,"r", encoding="utf-8") as f :
            tokens= json.load(f) # it will read teh content of files  and laod it into python as a list of dictionaries 



        #as we have gotten files and can read data from files , lets creat teh token and tag list from file
        words= [entry["token"] for entry in tokens]
        labels=[entry["ner_tag"] for entry in tokens] 


        all_data.append({
            "tokens":words,
            "ner_tags":labels
                            })
        

# lets split into train and validation
train_data,val_data=train_test_split(all_data, test_size=0.2, random_state=42)


# lets save final dataset to disk 
final_dataset= {
    "train":train_data,
    "validation":val_data,
}

with open(OUTPUT_PATH,"w",encoding="utf8") as f :
    json.dump(final_dataset,f,indent=2)



print("dataset is prepared and saved to outputpath")