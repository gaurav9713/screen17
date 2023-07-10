# screen17

## Python Version

This project was developed using Python version 3.11.3. Make sure you have Python 3.11.3 or a compatible version installed.

## Dependencies

All the required dependencies for this project can be installed using the `requirements.txt` file. Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## Docker Compose

To set up the MySQL database and Adminer (workbench), make sure you have Docker installed on your machine. Create a .env file with your preferred credentials in the following format:

```
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_DATABASE=your_database_name
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
```
Then, use the following command to start the containers:

```
docker-compose up
```

## Usage
Scrape URLs
The scrape.py file contains the code for scraping URLs to download the Parquet files from the target URL. To run the scraper, execute the following command:

```
python scrape.py
```

## Download Files
The download.py file contains the code for downloading all the URLs. Run the following command to initiate the download process:
```
python download.py
```

## Calculate Average Trip Length
The query.py file contains the code for calculating the average trip length. Execute the following command to run the query:
```
python query.py
```

## Ingest Data
The ingest.py file contains the code for ingesting the data from the downloaded files into the MySQL database. Run the following command to start the ingestion process:
```
python ingest.py
```

## Rolling Averages SQL Query
The SQL query for calculating rolling averages can be found in the `rolling_averages_sql.sql` file. You can execute this query using a SQL workbench or equivalent tool to calculate the rolling averages based on your data.
