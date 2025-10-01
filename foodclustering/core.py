import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

class FoodClustering:
    def __init__(self, n_clusters=2):
        # Generate synthetic training data
        self.df = pd.DataFrame({
            "carbs": np.random.randint(30, 80, 50),
            "protein": np.random.randint(5, 40, 50),
            "fiber": np.random.randint(2, 20, 50),
            "fats": np.random.randint(10, 40, 50)
        })

        # Normalize so percentages sum ≈ 100
        self.df["total"] = self.df.sum(axis=1)
        for col in ["carbs", "protein", "fiber", "fats"]:
            self.df[col] = (self.df[col] / self.df["total"] * 100).round(2)
        self.df = self.df.drop("total", axis=1)

        # Train KMeans clustering
        self.model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.df["cluster"] = self.model.fit_predict(self.df[["carbs","protein","fiber","fats"]])

        # Find which cluster is "healthy" (closest to balanced)
        self.cluster_summary = self.df.groupby("cluster").mean()
        self.healthy_cluster = self.cluster_summary.apply(
            lambda row: abs(row["carbs"]-50) + abs(row["protein"]-25) +
                        abs(row["fiber"]-15) + abs(row["fats"]-10),
            axis=1
        ).idxmin()

    def predict(self, carbs, protein, fiber, fats):
        total = carbs + protein + fiber + fats
        if total == 0:
            return "Invalid input!"
        
        # Normalize input
        x = np.array([[carbs/total*100, protein/total*100, fiber/total*100, fats/total*100]])
        cluster = self.model.predict(x)[0]

        if cluster == self.healthy_cluster:
            return "Healthy"
        else:
            return "Unhealthy"
