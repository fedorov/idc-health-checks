import unittest
from google.cloud import bigquery
import os

bq_queries = {
"check_if_table_exists": "SELECT 1 FROM `biquery-public-data.idc_current.dicom_all` LIMIT 1",

}


class MyTest(unittest.TestCase):
    def test_bq_queries(self):
        # iterate over all queries in bq_queries dictionary and execute each query
        for query_name,query in bq_queries.items():
            print("Executing query: " + query_name + " with query: " + query + " ...")
            client = bigquery.Client(os.environ["PROJECT_ID"])
            client.query(bq_queries[query_name]).result()

if __name__ == '__main__':
    unittest.main()
