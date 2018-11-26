from PIL import Image, ImageDraw

def getHeight(clust):
    # Is this an endpoint? Then the height is 1
    if clust.left == None and clust.right == None:
        return 1

    # otherwise the height is the same as the rest of the branches
    return getHeight(clust.left) + getHeight(clust.right)


def getDepth(clust):
    # the distance of two endpoints is 0
    if clust.left == None and clust.right == None:
        return 0

    # The distance is greater than two sides plus its own distance
    return max(getDepth(clust.left), getDepth(clust.right)) + clust.distance


def drawDendrogram(clust, labels, jpeg='clusters.jpg'):
    # Set height, width and depth
    h = getHeight(clust) * 20
    w = 1200
    d = getDepth(clust)

    # width is static so scale distances accordingly
    scaling = float(w - 150) / d

    # Create the image
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.line((0, h / 2, 10, h / 2), fill=(255, 0, 0))

  # Draw the first node
    drawNode(draw, clust, 10, h / 2, scaling, labels)
    img.save(jpeg, 'JPEG')

def drawNode(draw, clust, x, y, scaling, labels):
    if clust.id < 0:
        h1 = getHeight(clust.left) * 20
        h2 = getHeight(clust.right) * 20
        top = y - (h1 + h2) / 2
        bottom = y + (h1 + h2) / 2
        # Line length
        ll = clust.distance * scaling
        # Vertical line from this cluster to children
        draw.line((x, top + h1 / 2, x, bottom - h2 / 2), fill=(255, 0, 0))

        # Horizontal line to left item
        draw.line((x, top + h1 / 2, x + ll, top + h1 / 2), fill=(255, 0, 0))

        # Horizontal line to right item
        draw.line((x, bottom - h2 / 2, x + ll, bottom - h2 / 2), fill=(255, 0,
                  0))

        # Call this function if it's not an endpoint
        drawNode(draw, clust.left, x + ll, top + h1 / 2, scaling, labels)
        drawNode( draw, clust.right, x + ll, bottom - h2 / 2, scaling, labels)
    else:
        # If this is an endpoint, draw the item label
        draw.text((x + 5, y - 7), labels[clust.id], (0, 0, 0))
