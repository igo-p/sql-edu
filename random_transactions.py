import random
import pandas as pd
from faker import Faker
from datetime import datetime

# List of customer names
customers = [
    "Kelly Slater",
    "John Florence",
    "Mike T",
    "Olga Tokarczuk",
    "Iga Świątek",
    "Sam Altman",
    "Taylor Swift",
    "Wisława Szymborska",
    "Adam Małysz",
    "Napoleon Bonaparte",
    "Mihaly Csikszentmihalyi",
    "Paul Graham"
]

# List of cycling equipment in Polish
# Modify the products list to include prices
products = {
    "rower szosowy": 3500.00,
    "kask rowerowy": 250.00,
    "pedały SPD": 180.00,
    "pompa ręczna": 50.00,
    "bidon": 30.00,
    "licznik rowerowy": 150.00,
    "światła rowerowe": 120.00,
    "dętka": 25.00,
    "łańcuch rowerowy": 80.00,
    "sakwa rowerowa": 200.00,
    "blat korbowy": 150.00,
    "zestaw naprawczy": 45.00
}

# Initialize Faker for random dates
fake = Faker()
Faker.seed(42)

# Add a list of European countries
european_countries = [
    "Polska",
    "Niemcy",
    "Francja",
    "Włochy",
    "Hiszpania",
    "Holandia",
    "Belgia",
    "Czechy",
    "Szwajcaria",
    "Austria",
    "Dania",
    "Szwecja",
    "Norwegia",
    "Finlandia",
    "Portugalia"
]

# Add product colors
product_colors = [
    "czerwony",
    "czarny",
    "niebieski",
    "biały",
    "zielony"
]

# Create a dictionary to store product IDs
product_ids = {}

def generate_product_id(product, color, origin):
    # Create a unique key
    key = f"{product}_{color}_{origin}"
    # If this combination doesn't have an ID yet, create one
    if key not in product_ids:
        # Generate a new ID - let's use a simple incremental system
        new_id = len(product_ids) + 1
        product_ids[key] = f"PROD_{new_id:04d}"  # Format: PROD_0001, PROD_0002, etc.
    return product_ids[key]

def generate_random_transactions(num_transactions):
    data = []
    for _ in range(num_transactions):
        transaction_day = fake.date_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31)
        )
        product = random.choice(list(products.keys()))
        product_price = products[product]
        item_count = random.randint(1, 10)
        # Ensure discount is smaller than product price and between 0-30%
        max_discount = min(0.3, product_price / product_price)  # This ensures max 30% discount
        discount = round(random.uniform(0, max_discount), 2)
        transaction_amount = round(product_price * item_count * (1 - discount), 2)
        customer = random.choice(customers)
        product_origin = random.choice(european_countries)
        product_color = random.choice(product_colors)
        product_id = generate_product_id(product, product_color, product_origin)

        data.append([
            transaction_day,
            transaction_amount,
            customer,
            "",  # Company is blank
            product,
            product_price,
            discount,
            item_count,
            product_origin,
            product_color,
            product_id
        ])
    return data

# Update the columns list
columns = [
    "transaction_day", "transaction_amount", "customer", "company",
    "product", "product_price", "discount", "item_count", "product_origin",
    "product_color", "product_id"
]

# Number of random transactions to generate
num_transactions = 7770
transactions = generate_random_transactions(num_transactions)

# Create a DataFrame for better visualization and export
columns = [
    "transaction_day", "transaction_amount", "customer", "company",
    "product", "product_price", "discount", "item_count", "product_origin",
    "product_color", "product_id"
]
df = pd.DataFrame(transactions, columns=columns)

# Save to a CSV file
df.to_csv("output_files/random_transactions.csv", index=False, encoding="utf-8")

print("Random transaction data generated and saved to 'output_files/random_transactions.csv'.")
