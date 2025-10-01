# FoodClustering

A simple clustering package that classifies food plates (carbs, protein, fiber, fats) as **Healthy** or **Unhealthy**.

## Usage
```python
from foodclustering import FoodClustering

fc = FoodClustering()
print(fc.predict(60, 25, 10, 15))  # Example input
