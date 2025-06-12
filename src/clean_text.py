import os 
import re 


# lets see the pths 
RAW_DIR = "data/raw"
CLEANED_DIR="data/cleaned"

# lets see or make sure cleaned directory exist 
os.makedirs(CLEANED_DIR, exist_ok=True)


# now its time to write the function 



def clean_text(text):
    text = text.replace('\n', ' ')           # replace newlines with spaces
    text = text.replace('\t', ' ')           # replace tabs with spaces
    text = re.sub(r' +', ' ', text)          # replace multiple spaces with one space
    text = re.sub(r'\[\d+\]', '', text)      # remove citation-style [1], [2], etc.
    text = text.strip()                      # remove extra leading/trailing spaces
    return text


# lets move to the enxt step and taht is loop throght all files I mean raw and apply that function and store resultant data or cleaned data in cleaned folder 
# Loop through all .txt files in raw folder
for filename in os.listdir(RAW_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(RAW_DIR, filename), 'r', encoding='utf-8') as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        with open(os.path.join(CLEANED_DIR, filename), 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

print(" All files cleaned and saved to data/cleaned/")
