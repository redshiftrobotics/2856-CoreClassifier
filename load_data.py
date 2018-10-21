import turicreate as tc
import xml.etree.ElementTree as ET
import glob
import os
import math

# array for keeping track  of the annotations we parse
unsorted_annotations = [] # the array *must* be in this shape: [[{dict}]]

for file in glob.glob('generator/annotations/*.xml'): # loop through every xml annotation
    tree = ET.parse(file) # create a tree with the data from the xml file
    root = tree.getroot() # get the root element of the tree

    # array for the extracted properties for each object
    object_props = []
    """
    the object element is an element containing x, y coordinates and the size
    of the detected object along with some meta-data about the object
    """
    for member in root.findall('object'): # get every object element from the tree
        label = member[0].text # class of the detected object (block or ball)

        # coordinates are the 6th member of the object
        xmin = int(member[5][0].text)
        ymin = int(member[5][1].text)
        xmax = int(member[5][2].text)
        ymax = int(member[5][3].text)

        # get the dementions of the object from the coordinates
        width = xmax - xmin
        height = ymax - ymin

        # get the filename so we can map it to an image later
        image_name = root.find('filename').text

        # get the x, y points from the coordinates
        x = xmin + math.floor(width / 2)
        y = ymin + math.floor(height / 2)

        # basic properies
        props = {'label': label, 'type': 'rectangle', 'filename': image_name}
        # add coordinates to properties
        props['coordinates'] = {'height': height,
                                'width': width, 'x': x, 'y': y}

        # add the properies to the array of objects for this annotation
        object_props.append(props)

    # add it to the array of all annotations
    unsorted_annotations.append(object_props)

# load all the images in the data folder
data = tc.image_analysis.load_images('generator/data')

"""
the unsorted annotations are not in any particular order
so we have to match them to each image from data
"""
annotations = [] # sored annotations
for item in data: # loop through every image object
    for row in unsorted_annotations: # find what annotation coorisponds to it
        if str(row[0]['filename']) == str(os.path.split(item['path'])[1]): # messy if statment
            # match image name in path
            annotations.append(row)
            break

data['annotations'] = tc.SArray(data=annotations, dtype=list) # set the annotations property in the data object

data.save('data.sframe') # save it to an sframe (sframe is just a serialized python object)

# this tells the turicreate visualizer how we want it to draw boxes on our images
data['image_with_ground_truth'] = tc.object_detector.util.draw_bounding_boxes(
    data['image'], data['annotations'])

# explore the data using the turicreate visulizer - THIS WILL BREAK ON NON-MAC OSs
data.explore()
