import json
import csv
import time
from functools import wraps
from typing import List, Dict, Any, Generator

# 1. OOP & Decorators: The Timer Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time for {func.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper

# 1. OOP: Base Model Class
class Model:
    def predict(self, data: Any) -> Any:
        raise NotImplementedError("Subclasses must implement predict()")

# 1. OOP: LinearModel with Inheritance, __call__, and __repr__
class LinearModel(Model):
    def __init__(self, weights: List[float]):
        self.weights = weights

    def predict(self, data: List[float]) -> float:
        # Simple dot product simulation
        if len(data) != len(self.weights):
            raise ValueError("Data dimension mismatch")
        return sum(d * w for d, w in zip(data, self.weights))

    def __call__(self, data: List[float]) -> float:
        # Allows calling model(data) instead of model.predict(data)
        return self.predict(data)

    def __repr__(self):
        return f"LinearModel(weights={self.weights})"

# 2. Pythonic Iterations: Generator for Batching
def batch_generator(data: List[Any], batch_size: int) -> Generator[List[Any], None, None]:
    """
    Yields chunks of data.
    Why Generators? For a 10GB dataset, a list would load everything into RAM, likely crashing the system.
    A generator yields one batch at a time, keeping memory usage constant regardless of dataset size.
    """
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# 2. Pythonic Iterations: Lambda Sorting
def sort_models_by_accuracy(models: List[tuple]) -> List[tuple]:
    # Sort by the second element (accuracy) in descending order
    return sorted(models, key=lambda x: x, reverse=True)

# 2. Pythonic Iterations: List Comprehension Filtering
def filter_low_loss(results: List[Dict[str, Any]], threshold: float) -> List[float]:
    # Extract 'loss' where loss < threshold
    return [r['loss'] for r in results if r.get('loss', 1.0) < threshold]

# 3. Environment & Dependencies: Conceptual Commands
# Note: These are commands you would run in a terminal, not executable Python code.
"""
# Create environment
python -m venv ml_env

# Activate (Windows)
ml_env\Scripts\activate
# Activate (Mac/Linux)
source ml_env/bin/activate

# Install packages
pip install numpy pandas

# Generate requirements.txt
pip freeze > requirements.txt

# Recreate environment (for teammate)
pip install -r requirements.txt
"""

# 4. CSV & JSON Handling: Robust File Operations
def load_config(config_path: str) -> Dict[str, Any]:
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.")
        return {}

def process_data(csv_path: str, json_output_path: str, label_map: Dict[str, int]) -> None:
    try:
        with open(csv_path, 'r', newline='') as infile, open(json_output_path, 'w') as outfile:
            reader = csv.DictReader(infile)
            processed_rows = []
            
            for row in reader:
                # Convert labels using the map
                row['label'] = label_map.get(row['label'], -1) 
                processed_rows.append(row)
            
            json.dump(processed_rows, outfile, indent=2)
            print(f"Processed {len(processed_rows)} rows into {json_output_path}")
            
    except FileNotFoundError:
        print(f"Error: Data file '{csv_path}' not found.")

# Challenge Task: The Mini-Pipeline
@timer
def run_pipeline():
    # 1. Load Config
    config = load_config("config.json")
    if not config:
        print("Using default config due to missing file.")
        config = {"learning_rate": 0.01, "batch_size": 32, "optimizer": "adam"}
    
    print(f"Loaded config: {config}")

    # 2. Create Model
    model = LinearModel(weights=[0.5, -0.2, 0.8])
    print(f"Model initialized: {model}")

    # 3. Generate Synthetic Data (Simulating CSV loading via generator)
    # In a real scenario, you would read from CSV: with open('raw_data.csv') as f...
    raw_data = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
        [1.1, 2.2, 3.3],
        [4.4, 5.5, 6.6]
    ]
    
    # Use generator to process in batches
    batches = list(batch_generator(raw_data, 2))
    
    # 4. Process Features with List Comprehension
    # Example: Normalize first feature of each batch
    processed_batches = [
        [[x * 0.5] + x[1:] for x in batch] 
        for batch in batches
    ]
    
    # 5. "Train" (Predict) with the Decorator timing
    print("Starting training loop (predictions)...")
    total_loss = 0.0
    for batch in processed_batches:
        for sample in batch:
            pred = model(sample) # Uses __call__
            # Mock loss calculation
            loss = (pred - 1.0) ** 2 
            total_loss += loss
            
    print(f"Total mock loss: {total_loss:.4f}")

    # 6. Filter Results (List Comprehension)
    mock_results = [{'loss': 0.5, 'epoch': 1}, {'loss': 0.2, 'epoch': 2}, {'loss': 0.1, 'epoch': 3}]
    low_loss_epochs = filter_low_loss(mock_results, 0.3)
    print(f"Epochs with loss < 0.3: {low_loss_epochs}")

    # 7. Sort Models (Lambda)
    model_performance = [('model_A', 0.92), ('model_B', 0.95), ('model_C', 0.88)]
    sorted_models = sort_models_by_accuracy(model_performance)
    print(f"Sorted Models: {sorted_models}")

if __name__ == "__main__":
    # To fully test file handling, you would create 'config.json' and 'raw_data.csv' first
    # For this demo, we run the in-memory simulation
    run_pipeline()