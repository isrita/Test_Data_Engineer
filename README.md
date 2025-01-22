# Test Data Engineer

This repository demonstrates my skills in data engineering by showcasing solutions for common data challenges, with a focus on data transformation, incremental ingestion, and generating insights. While I specialize in building scalable pipelines and performing incremental data ingestion in **Azure** and **Databricks**, this exercise is implemented locally using **Python** and **SQL** to keep foundational data transformation concepts fresh and show adaptability to open-source tools.

## Repository Structure

```
Test_Data_Engineer/
├── convert_csv_sql.py                 # Script to convert CSV files into SQL insert statements
├── data_calculate_kpis.py             # Python script to calculate KPIs from transformed data
├── data_script_sql.sql                # SQL script for creating and querying a PostgreSQL database
├── data_transformation.py             # Python script to transform and clean CSV data
├── data_transformation_with_API.py    # Script to enrich data with a currency conversion API
├── fixed_order_full_information.csv   # CSV file with transformed data including currency conversion
├── kpi_product_orders.csv             # CSV file with KPIs such as top products and categories
├── order_full_information.csv         # Consolidated CSV file combining product and order data
├── order_full_information.sql         # SQL script to create and populate the PostgreSQL table
├── orders.csv                         # Raw dataset with order details
├── products.csv                       # Raw dataset with product details
└── README.md                          # Documentation for the repository
```

## Challenges Addressed

### **Challenge 1: CSV File Manipulation**
- Combined `products.csv` and `orders.csv` into a single consolidated file (`order_full_information.csv`).
- Added columns: `order_created_date`, `order_id`, `product_name`, `quantity`, and `total_price`.
- Demonstrates foundational data transformation skills using Python.

### **Challenge 2.1: Currency Conversion**
- Enriched the data by converting prices from BRL to USD using the **Free Currency API**.
- Generated `fixed_order_full_information.csv` with additional columns: `total_price_br` and `total_price_us`.
- Showcases API integration and dynamic data enrichment.

### **Challenge 2.2: Data Exploration**
- Used Python to analyze the dataset and extract:
  - The date with the highest number of orders.
  - The most sold product and its total sales value.
  - The top 3 most demanded categories.
- Results saved in `kpi_product_orders.csv`.

### **Challenge 3: PostgreSQL Database and Querying**
- Programmatically created a PostgreSQL database and tables using the provided CSV files as data sources.
- Executed SQL queries to find:
  - The date with the maximum number of orders.
  - The most demanded product.
  - The top 3 most demanded categories.
- Script available in `data_script_sql.sql`.
- Emphasis on query efficiency for scalable environments.

## Why Databricks and Azure?
While this exercise is done locally, I specialize in building pipelines and performing incremental data ingestion in **Azure** and **Databricks**. These platforms enable:
- **Scalability:** Seamlessly handle large datasets using **Apache Spark**.
- **Flexibility:** Implement complex transformations with **PySpark** and **Scala**.
- **Automation:** Schedule and monitor pipelines with **Azure Data Factory** or Databricks Jobs.
- **Integration:** Connect with various cloud and on-premise data sources.

This local implementation demonstrates adaptability to different tools while maintaining a structured approach to data engineering tasks.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Test_Data_Engineer.git
   ```

2. Navigate to the repository:
   ```bash
   cd Test_Data_Engineer
   ```

3. Set up the environment:
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. Run scripts as needed:
   - Example: Execute the data transformation script:
     ```bash
     python data_transformation.py
     ```
   - Example: Run the SQL queries:
     ```bash
     psql -d your_database -f data_script_sql.sql
     ```

## Future Improvements
- **Databricks Integration:** Migrate these workflows to Databricks for showcasing scalable, cloud-based pipelines.
- **Visualization:** Build dashboards in Power BI to present insights effectively.
- **Automation:** Schedule workflows using Azure Data Factory or Airflow.

## Contact
For questions or collaboration opportunities, feel free to reach out!
