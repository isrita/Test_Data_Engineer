import pandas as pd
import os

class DataTransformer:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def process(self, products_file, orders_file, output_file):
        products = pd.read_csv(os.path.join(self.data_dir, products_file))
        orders = pd.read_csv(os.path.join(self.data_dir, orders_file))
        
        result = orders.merge(products, left_on="product_id", right_on="id")[
            ["created_date", "id_x", "name", "quantity", "price"]
        ]
        result.columns = ["order_created_date", "order_id", "product_name", "quantity", "total_price"]
        result["total_price"] = (result["quantity"] * result["total_price"]).round(4)

        result.to_csv(os.path.join(self.data_dir, output_file), index=False)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    transformer = DataTransformer(data_dir=os.path.join(base_dir, "data"))
    transformer.process("products.csv", "orders.csv", "order_full_information.csv")