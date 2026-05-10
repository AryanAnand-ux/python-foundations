import json
import csv

# 1. Loading Config
def load_config(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ Error: {path} not found. Using defaults.")
        return {"lr": 0.01, "batch_size": 32}

# 2. Transforming CSV to JSON
def process_data(input_csv, output_json):
    processed = []
    label_map = {"spam": 1, "ham": 0}
    
    try:
        with open(input_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Transform label and store
                row['label'] = label_map.get(row['label'], -1)
                processed.append(row)
        
        with open(output_json, 'w') as f:
            json.dump(processed, f, indent=4)
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example JSON config might look like:
# { "learning_rate": 0.001, "optimizer": "Adam" }