import time
from functools import wraps

# The Timer Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  {func.__name__} took {end - start:.4f} seconds.")
        return result
    return wrapper

class Model:
    """Base class for all models."""
    def predict(self, data):
        raise NotImplementedError("Subclasses must implement predict()")

class LinearModel(Model):
    def __init__(self, weights):
        self.weights = weights

    def predict(self, data):
        # Simple weighted sum: y = Σ(w * x)
        return sum(w * x for w, x in zip(self.weights, data))

    # The __call__ dunder allows us to use model(data)
    def __call__(self, data):
        return self.predict(data)

    # The __repr__ dunder for clean debugging
    def __repr__(self):
        return f"LinearModel(weights={self.weights})"

    @timer
    def train(self, data):
        time.sleep(0.5)  # Simulating a heavy computation
        print("Model trained successfully.")

# Usage
model = LinearModel(weights=[0.5, -0.2, 0.1])
print(model) # Calls __repr__
model.train([1, 2, 3]) # Calls @timer
print(f"Prediction: {model([10, 5, 2])}") # Calls __call__ -> predict