def readFile(filename):
    lines = open(filename).readlines()

    # First line is the column titles
    col_names = lines[0].strip().split('\t')[1:]
    row_names = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')

        # First column in each row is the row name
        row_names.append(p[0])

        # The data for this row is the remainder of the row
        data.append([float(x) for x in p[1:]])
    return row_names, col_names, data

class bicluster:
    def __init__(self, vec, id=None, distance=0.0):
        self.vec = vec
        self.id = id
        self.distance = distance

class centroid:
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


blognames,words,data=readFile('blogdata.txt')
clust=kcluster(data, K=3)
printClust(clust, blognames)