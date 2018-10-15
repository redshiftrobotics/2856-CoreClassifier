import turicreate as tc
from xml.dom import minidom
import glob
import os
import math

annotations = []

for file in glob.glob('raccoon_dataset/annotations/*.xml'):
    xml = minidom.parse(file)

    # TODO clean this up
    width = int(xml.getElementsByTagName('width')[0].firstChild.data)
    height = int(xml.getElementsByTagName('height')[0].firstChild.data)

    xmin = int(xml.getElementsByTagName('xmin')[0].firstChild.data)
    ymin = int(xml.getElementsByTagName('ymin')[0].firstChild.data)

    x = xmin + math.floor(width / 2)
    y = ymin + math.floor(height / 2)

    props = {'label': 'Object', 'type': 'rectangle'}
    props['coordinates'] = {'height': height, 'width': width, 'x': x, 'y': y}

    annotations.append([props])

data = tc.image_analysis.load_images('raccoon_dataset/images')

data['label'] = data['path'].apply(lambda _: 'Object')

data['annotations'] = tc.SArray(data=annotations, dtype=list)

data.save('data.sframe')

data['image_with_ground_truth'] = tc.object_detector.util.draw_bounding_boxes(
    data['image'], data['annotations'])

data.explore()
