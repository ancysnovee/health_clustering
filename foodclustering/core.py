import pandas as pd
import os

# Load CSV from inside the package
def load_data():
    dir_path = os.path.dirname(__file__)
    csv_path = os.path.join(dir_path, "FOOD-DATA-GROUP1.csv")
    df = pd.read_csv(csv_path)
    return df

# List all foods
def list_foods():
    df = load_data()
    return df['food'].tolist()

# Get nutrition info of a specific food
def get_nutrition(food_name):
    df = load_data()
    row = df[df['food'].str.lower() == food_name.lower()]
    if row.empty:
        return f"{food_name} not found!"
    return row.to_dict(orient='records')[0]

# Simple classification based on calories, fat, and sugar
def classify_food(food_name):
    df = load_data()
    row = df[df['food'].str.lower() == food_name.lower()]
    if row.empty:
        return f"{food_name} not found!"

    row = row.iloc[0]

    # Thresholds (you can tweak these)
    calories_limit = 200          # Calories per serving
    fat_limit = 10                # grams
    sugar_limit = 15              # grams

    # Check if any of these exceed limits
    if row['Caloric Value'] > calories_limit or row['Fat'] > fat_limit or row['Sugars'] > sugar_limit:
        return "Unhealthy"
    else:
        return "Healthy"
if __name__ == "__main__":
    # List foods
    foods = list_foods()
    print("First 10 foods:", foods[:10])

    # Nutrition info for banana
    banana_info = get_nutrition("banana")
    print("Banana nutrition info:", banana_info)

    # Classification examples
    print("Banana classification:", classify_food("banana"))
    print("Cream cheese classification:", classify_food("cream cheese"))


