# encoding: utf-8

import unittest
import requests
import json

headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}
# pass transaction Id
 
class TestAPIEndpoints(unittest.TestCase):
 
 # Test code To PUT transaction API
    def test_transactions_success(self):
        res = requests.put("http://localhost:5000/api/v1/transactionservice/transactions", data = json.dumps({"amount": 5000, "type": "cars"}), headers=headers)
        self.assertDictEqual({"status": "ok"}, res.json())

 # Test code To  GET Trasaction Detail BY transaction_id API    
    def test_gettrascations_success(self):
        res = requests.get("http://localhost:5000/api/v1/transactionservice/types/cars")
        t_id = res.json()[0]
        res = requests.get("http://localhost:5000/api/v1/transactionservice/transactions/" + t_id)    
        print(res.json()) 
         

# Test code To GET All Transaction_ids by transaction type  
    def test_types_success(self):
        res = requests.get("http://localhost:5000/api/v1/transactionservice/types/car")           
        self.assertEqual(1, len(res.json()))

# Test Code To Get  Sum of all transactions that are /
# transitively linked by their parent_id to transaction_id
    def test_getSum_success(self):
        res = requests.get("http://localhost:5000/api/v1/transactionservice/types/car")
        t_id = res.json()[0]
        res = requests.get("http://localhost:5000/api/v1/transactionservice/sum/" + t_id)    
        print(res.json())

if __name__ == '__main__':
    unittest.main()