import os 
import json

CLEANED_DIR= "data/cleaned"
LABELED_DIR= "data/labeled"


# lets see the label options 



LABELS =[
"O",
"B-COMPONENT",
"I-COMPONENT",
"B-MEASUREMENT",
"I-MEASUREMENT",
"B-WARNING",
"I-WARNING",
"B-PROCEDURE",
"I-PROCEDURE",
"B-TOOL",
"I-TOOL"



]


os.makedirs("LABELED_DIR",exist_ok=True)



def label_text_file(file_path): # this function will take one file like wiki_abs.txt and  will label its all wors
    with open(file_path,"r",encoding="utf-8") as f:
        text= f.read()

    tokens= text.strip().split() # will break the text into individual words 
    labeled_tokens=[]
    print(f"\n Labeling file: {file_path}")
    print("Type the label number (e.g., 1 for B-COMPONENT), or press ENTER for 'O'\n")

    for i, token in enumerate(tokens):
        print(f"\n Token [{i+1}/{len(tokens)}]: {token}")
        for j, label in enumerate(LABELS):
            print(f"{j}: {label}")
        inp = input("Label number (default=0): ").strip()
        label_idx = int(inp) if inp.isdigit() else 0
        labeled_tokens.append({"token": token, "ner_tag": label_idx})

    out_path = os.path.join(LABELED_DIR, os.path.basename(file_path).replace(".txt", ".json"))
    with open(out_path, "w", encoding="utf-8") as out_file:
        json.dump(labeled_tokens, out_file, indent=2)

    print(f"\n Labeled file saved to: {out_path}\n")


# --- MAIN ---
if __name__ == "__main__":
    for file in os.listdir(CLEANED_DIR):
        if file.endswith(".txt"):
            path = os.path.join(CLEANED_DIR, file)
            label_text_file(path)
