import unittest
from google.cloud import bigquery
import os
import requests
import json

bq_queries = {
"check_if_table_exists": """
    SELECT PatientID 
    FROM `bigquery-public-data.idc_current.dicom_all` 
    LIMIT 1
""",

}

idc_api_preamble = "https://api.imaging.datacommons.cancer.gov/v1"
idc_dev_api_preamble = "https://dev-api.canceridc.dev/v2"

def pretty(response):
    print(json.dumps(response.json(), sort_keys=True, indent=4))

class MyTest(unittest.TestCase):
    def test_bq_queries(self):
        # iterate over all queries in bq_queries dictionary and execute each query
        for query_name,query in bq_queries.items():
            print("Executing query: " + query_name + " with query: " + query + " ...")
            client = bigquery.Client(os.environ["PROJECT_ID"])
            client.query(bq_queries[query_name]).result()

    def test_prod_api(self):
        response = requests.get('{}/collections'.format(idc_api_preamble))
        # Check that there wasn't an error with the request
        if response.status_code != 200:
            # Print the error code and message if something went wrong
            print('Request failed: {}'.format(response.reason))

        # Print the collections JSON text
        pretty(response)

    def test_dev_api(self):
        response = requests.get('{}/collections'.format(idc_dev_api_preamble))
        # Check that there wasn't an error with the request
        if response.status_code != 200:
            # Print the error code and message if something went wrong
            print('Request failed: {}'.format(response.reason))
        
        # Print the collections JSON text
        pretty(response)

# Print the collections JSON text
pretty(response)
if __name__ == '__main__':
    unittest.main()
