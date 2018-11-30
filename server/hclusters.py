import json

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()
        
class bicluster(JsonSerializable):
    def __init__(self, vec, left=None, right=None, id=None, distance=0.0):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance

from pearson import pearson

def hcluster(rows, distance=pearson):
    closestClusters = []
    clusters = {}
    storedDistances = {}
    combinedClustersId = -1

    for i in range(len(rows)):
        clusters[i] = bicluster(rows[i], id=i)

    # Iterate until there are only one cluster left
    while len(clusters) > 1:
        closest = 10.0
        for i in clusters:
            for j in clusters:
                if (j != i):
                    # Store all the distances in a list
                    # so that we later on can just do a simple look-up
                    # and don't have to iterate through the entire list and find
                    # distances again
                    A = clusters[i]
                    B = clusters[j]
                    if (A.id, B.id) not in storedDistances:
                        dist = distance(A.vec, B.vec)
                        storedDistances[(A.id, B.id)] = dist

                    # Find the closest distance from the stored distances
                    if (storedDistances[(A.id, B.id)] < closest):
                        closest = dist
                        closestClusters = [A, B]

        # ... and merge the clusters
        combinedClustersId -= 1
        merged_clusters = merge(closestClusters, closest, combinedClustersId)

        # Remove the old clusters since these are merged
        del clusters[closestClusters[1].id]
        del clusters[closestClusters[0].id]
        clusters[combinedClustersId] = merged_clusters

    # Return the last merged cluster of clusters
    return list(clusters.values())[0]

def merge(clusters, distance, id):
    A = clusters[0]
    B = clusters[1]
    newCluster = []

    # Assuming vec-length of A is same as length of words
    for i in range(len(A.vec)):
        countWordA = A.vec[i]
        countWordB = B.vec[i]

        merge_count = countWordA + countWordB / 2.0
        newCluster.append(merge_count)
    
    merged_clusters = bicluster(newCluster, left=A, right=B, id=id, distance=distance)
    return merged_clusters

def HJsonConverter(clust, labels=None):
    if labels != None:
        parent = { 'id': 'root', 'children': [], 'name': '' }
        tree = recursiveJson(clust, parent, labels)

        return tree
    else: return []

def recursiveJson(node, parent, labels=None):
    newNode = { 'id': node.id, 'children': [], 'name': '' }
    # If id is less than 0 => it's a merged cluster
    if (node.id > -1):
        newNode['name'] = labels[node.id]

    parent['children'].append(newNode)
    # Now store the right and left clusters
    if node.left is not None: recursiveJson(node.left, newNode, labels=labels)
    if node.right is not None: recursiveJson(node.right, newNode, labels=labels)

    return parent

from filereader import readFile

# blognames,words,data=readFile('blogdata.txt')
# clust=hcluster(data)
# jsonConverter(clust, labels=blognames)
# printClust(clust,labels=blognames)