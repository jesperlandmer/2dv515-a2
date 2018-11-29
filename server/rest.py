from flask import Flask, request, send_file
from flask_api import status
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from filereader import readFile
from kclusters import kcluster, KJsonConverter
from hclusters import hcluster, HJsonConverter
from dendogram import drawDendrogram

app = Flask(__name__)
api = Api(app)

class KCluster(Resource):
    def get(self, num_clusters):
        blognames,words,data=readFile('blogdata.txt')
        clust=kcluster(data, K=int(num_clusters))
        result = KJsonConverter(clust, labels=blognames)
        return jsonify(result)

class HCluster(Resource):
    def get(self):
        blognames,words,data=readFile('blogdata.txt')
        clust=hcluster(data)
        result=HJsonConverter(clust, labels=blognames)
        return jsonify(result)
        

api.add_resource(KCluster, '/api/kcluster/<num_clusters>') # Route_1
api.add_resource(HCluster, '/api/hcluster') # Route_2


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5002)