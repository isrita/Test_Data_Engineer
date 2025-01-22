import pandas as pd
import os

class DataTransformer:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def process(self, products_file, orders_file, output_file):
        products = pd.read_csv(os.path.join(self.data_dir, products_file))
        orders = pd.read_csv(os.path.join(self.data_dir, orders_file))

        result = orders.merge(products, left_on="product_id", right_on="id")[
            ["created_date", "id_x", "name", "category", "quantity", "price"]
        ]
        result.columns = ["order_created_date", "order_id", "product_name", "category", "quantity", "total_price"]
        result["total_price"] = (result["quantity"] * result["total_price"]).round(4)

        result.to_csv(os.path.join(self.data_dir, output_file), index=False)
        return result

    def calculate_kpis(self, processed_data, output_file):
        # Fecha con el mayor número de órdenes
        highest_orders_date = processed_data["order_created_date"].value_counts().idxmax()
        highest_orders_count = processed_data["order_created_date"].value_counts().max()

        # Producto más vendido y su valor total
        most_sold_product = processed_data.groupby("product_name")["quantity"].sum().idxmax()
        most_sold_value = processed_data[processed_data["product_name"] == most_sold_product]["total_price"].sum()

        # Top 3 categorías más demandadas
        top_categories = processed_data.groupby("category")["quantity"].sum().nlargest(3)

        # Crear un DataFrame con las métricas calculadas
        kpi_data = pd.DataFrame({
            "Metric": [
                "Date with Highest Orders",
                "Most Sold Product",
                "Most Sold Product Value",
                "Top 3 Categories"
            ],
            "Value": [
                f"{highest_orders_date} ({highest_orders_count} orders)",
                most_sold_product,
                round(most_sold_value, 2),
                ", ".join(top_categories.index)
            ]
        })

        kpi_data.to_csv(os.path.join(self.data_dir, output_file), index=False)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    transformer = DataTransformer(data_dir=os.path.join(base_dir, "data"))

    # Procesar los datos
    processed_data = transformer.process("products.csv", "orders.csv", "order_full_information.csv")

    # Calcular y guardar las métricas
    transformer.calculate_kpis(processed_data, "kpi_product_orders.csv")
