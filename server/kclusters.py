import json

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()

class bicluster(JsonSerializable):
    def __init__(self, vec, id=None, distance=0.0):
        self.vec = vec
        self.id = id
        self.distance = distance

class centroid(JsonSerializable):
    def __init__(self, row):
        self.row = row
        self.blogs = []
    
    def assign(self, blog):
        self.blogs.append(blog)

    def clearAssignments(self):
        self.prevCluster = self.blogs
        self.blogs = []
    
    def noNewAssignments(self):
        return len(self.blogs) == len(self.prevCluster)
                
        

from pearson import pearson
from random import randint

def kcluster(rows, distance = pearson, K = 0):
    # Generate K random centroids
    centroids = []
    for i in range(K):
        centroids.append(centroid([randint(0, 20) * 1.0 for i in range(len(rows[0]))]))
    
    done = False
    while done != True:
        for c in centroids:
            c.clearAssignments()
        
        # Each row is a blog
        for i in range(len(rows)):
            dist = 1.0
            best = centroids[0]

            for c in centroids:
                cDist = distance(c.row, rows[i])
                if cDist < dist:
                    best = c
                    dist = cDist

            best.assign(bicluster(rows[i], id=i, distance=dist))

        # Recenter the centroids
        for c in centroids:
            for i in range(len(c.row)):
                avg = 0.0
                
                for blog in c.blogs:
                    avg += blog.vec[i]
                avg /= len(c.blogs)

                c.row[i] = avg
            
            if c.noNewAssignments(): done = True
            else: done = False


    return centroids

def printClust(centroids, labels=None, n=0):
    for c in centroids:
        print('-')
        print('-')
        closest = None

        newlist = sorted(c.blogs, key=lambda x: x.distance, reverse=False)
        for i in range(len(newlist)):
            print(labels[newlist[i].id])
            print('-')

def jsonConverter(clust, labels=None):
    if labels != None:
        result = []
        for i in range(len(clust)):
            labelsInOrder = []
            newlist = sorted(clust[i].blogs, key=lambda x: x.distance, reverse=False)

            for i in range(len(newlist)):
                labelsInOrder.append({ 'name': labels[newlist[i].id], 'dist': newlist[i].distance })

            result.append({ 'id': i, 'cluster': labelsInOrder})
        
        return result
    else: return []


# from filereader import readFile

# blognames,words,data=readFile('blogdata.txt')
# clust=kcluster(data, K=3)

# printClust(clust, blognames)