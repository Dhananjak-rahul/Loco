# encoding: utf-8
from flask import Flask, jsonify, request
# import uuid1 to generate a unique id 
from uuid import uuid1
# import configuration values from config.py
from config import API_BASE, HOST, PORT, DEBUG

app = Flask(__name__)
# Definition of Dictionary
txn_lst = dict()


# API call to PUT Transactions in Dictionary
# METHOD : PUT
# trasaction_id automatically generated using UUID1

@app.route(API_BASE + "/transactions", methods=["PUT"])
def transactions_insert():
    try:
        if request.method == 'PUT':
            data = request.json
            data["id"] = uuid1().hex
            txn_lst[data["id"]] = data
            return jsonify({"status": "ok"})
    except:
        return jsonify({"Error": "Please check the request!"})


# API for  GET Transactions Details by it transaction_id 
# METHOD : GET
# Parameter: transaction_id

@app.route(API_BASE + "/transactions/<id>", methods=["GET"])
def transactions_get(id):
    try:
        if request.method == "GET":
            return jsonify(txn_lst[id])
        else:
            return jsonify({"Error": "Invalid Request"})
    except Exception as e:
        print(e)
        return jsonify({"Error": "Please check the request!"})


# API to GET All Transactions_ids of given Type
# METHOD : GET
# Parameter: type

@app.route(API_BASE + "/types/<ttype>", methods = ["GET"])
def types(ttype):
    if request.method == "GET":
        tlist = [txn_lst[t]["id"] for t in txn_lst.keys() if txn_lst[t]["type"] == ttype]
        return jsonify(tlist)
    else:
        return jsonify({"Error": "Invalid Request"})



# Sum of all transactions that are transitively linked by their parent_id to transaction_id
# Method: GET
# Parameter: transaction_id
 
@app.route(API_BASE + "/sum/<tid>", methods = ["GET"])
def sum(tid):
    famt = 0
    if request.method == "GET":
        # if parent_id is found in data
        if( "parent_id" in txn_lst[tid].keys()): 
            parent_id = txn_lst[tid]["parent_id"]
            txnsum = [float(txn_lst[t]["amount"]) for t in txn_lst.keys() if txn_lst[t]["parent_id"] == parent_id]
            for amt in txnsum:
                famt += float(amt)
        # else parent_id is not found in data        
        else:
            famt = txn_lst[tid]["amount"]
        # sum of amount
        return jsonify({"sum": famt})
    else:
        return jsonify({"Error": "Invalid Request"})


# Code to Run API Using HOST ,PORT in Debug Mode


if __name__ == "__main__":
    app.run(host = HOST, port = PORT, debug = DEBUG)
    
