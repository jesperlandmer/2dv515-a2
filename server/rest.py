from flask import Flask, request, send_file
from flask_api import status
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from filereader import readFile
from kclusters import kcluster, jsonConverter
from hclusters import hcluster
from dendogram import drawDendrogram

app = Flask(__name__)
api = Api(app)

class KCluster(Resource):
    def get(self, num_clusters):
        blognames,words,data=readFile('blogdata.txt')
        clust=kcluster(data, K=int(num_clusters))
        result = jsonConverter(clust, labels=blognames)
        return jsonify(result)

class HCluster(Resource):
    def post(self):
        blognames,words,data=readFile('blogdata.txt')
        clust=hcluster(data)
        drawDendrogram(clust, blognames, jpeg='blogclust.jpg')
        return {'success': True }, status.HTTP_201_CREATED

class ClustTree(Resource):
    def get(self):
        filename = 'blogclust.jpg'
        return send_file(filename, mimetype='image/gif')
        

api.add_resource(KCluster, '/api/kcluster/<num_clusters>') # Route_1
api.add_resource(HCluster, '/api/hcluster/generate') # Route_2
api.add_resource(ClustTree, '/api/hcluster/tree.jpg') # Route_3


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5002)