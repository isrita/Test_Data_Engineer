import pandas as pd
import os
import requests

class DataTransformer:
    def __init__(self, data_dir, api_key):
        self.data_dir = data_dir
        self.api_key = api_key

    def get_conversion_rate(self, from_currency="BRL", to_currency="USD"):
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={self.api_key}&base_currency={from_currency}"
        response = requests.get(url)
        response.raise_for_status()
        rates = response.json().get("data", {})
        return rates.get(to_currency, 1.0)

    def process(self, products_file, orders_file, output_file):
        products = pd.read_csv(os.path.join(self.data_dir, products_file))
        orders = pd.read_csv(os.path.join(self.data_dir, orders_file))
        
        conversion_rate = self.get_conversion_rate()

        result = orders.merge(products, left_on="product_id", right_on="id")[
            ["created_date", "id_x", "name", "quantity", "price"]
        ]
        result.columns = ["order_created_date", "order_id", "product_name", "quantity", "total_price_br"]
        result["total_price_br"] = (result["quantity"] * result["total_price_br"]).round(4)
        result["total_price_us"] = (result["total_price_br"] * conversion_rate).round(4)

        result.to_csv(os.path.join(self.data_dir, output_file), index=False)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    api_key = "fca_live_MOLYoNAzF2GHpNcZ4pljAHgQyAkWzEj8cVDSi6l5" 
    transformer = DataTransformer(data_dir=os.path.join(base_dir, "data"), api_key=api_key)
    transformer.process("products.csv", "orders.csv", "fixed_order_full_information.csv")
