import pandas as pd

def csv_to_sql(csv_file_path, table_name, output_sql_file):

    try:
        data = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"Error: The file at {csv_file_path} was not found.")
        return

    sql_statements = []
    for _, row in data.iterrows():
        values = ", ".join(
            ["'" + str(value).replace("'", "''") + "'" if isinstance(value, str) else str(value) for value in row]
        )
        sql_statements.append(f"INSERT INTO {table_name} VALUES ({values});")

    try:
        with open(output_sql_file, 'w') as f:
            f.write("\n".join(sql_statements))
        print(f"SQL script saved to {output_sql_file}")
    except Exception as e:
        print(f"Error writing to output file: {e}")

csv_file_path = r'C:\PROYECTOS\Python_projects\Data\order_full_information.csv' 
table_name = 'order_full_information'
output_sql_file = r'C:\PROYECTOS\Python_projects\Data\order_full_information.sql' 

csv_to_sql(csv_file_path, table_name, output_sql_file)

