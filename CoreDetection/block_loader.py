import turicreate as tc
from xml.dom import minidom
import glob
import os
import math

unsorted_annotations = []

for file in glob.glob('generator/annotations/*.xml'):
    xml = minidom.parse(file)

    # TODO clean this up
    width = int(xml.getElementsByTagName('width')[0].firstChild.data)
    height = int(xml.getElementsByTagName('height')[0].firstChild.data)

    xmin = int(xml.getElementsByTagName('xmin')[0].firstChild.data)
    ymin = int(xml.getElementsByTagName('ymin')[0].firstChild.data)

    image_name = str(xml.getElementsByTagName(
        'filename')[0].firstChild.data)

    x = xmin + math.floor(width / 2)
    y = ymin + math.floor(height / 2)

    props = {'label': 'block', 'type': 'rectangle', 'filename': image_name}
    props['coordinates'] = {'height': height, 'width': width, 'x': x, 'y': y}

    unsorted_annotations.append([props])

data = tc.image_analysis.load_images('generator/data')

data['label'] = data['path'].apply(lambda _: 'block')

# the data is in no particular order, so we have to loop it to match
# we also have the 'misc' images, which won't have an annotation, to skip
annotations = []
for item in data:
    for row in unsorted_annotations:
        if str(row[0]['filename']) == str(os.path.split(item['path'])[1]):
            # match image name in path
            annotations.append(row)
            break

data['annotations'] = tc.SArray(data=annotations, dtype=list)

data.save('data.sframe')

data['image_with_ground_truth'] = tc.object_detector.util.draw_bounding_boxes(
    data['image'], data['annotations'])

# data['image_with_predictions'] = tc.object_detector.util.draw_bounding_boxes(
#    data['image'], data['annotations'])

data.explore()
