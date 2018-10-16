import turicreate as tc
import xml.etree.ElementTree as ET
import glob
import os
import math

unsorted_annotations = []

for file in glob.glob('generator/annotations/*.xml'):
    tree = ET.parse(file)
    root = tree.getroot()

    object_props = []
    for member in root.findall('object'):
        label = member[0].text

        xmin = int(member[5][0].text)
        ymin = int(member[5][1].text)
        xmax = int(member[5][2].text)
        ymax = int(member[5][3].text)

        width = xmax - xmin
        height = ymax - ymin

        image_name = root.find('filename').text

        x = xmin + math.floor(width / 2)
        y = ymin + math.floor(height / 2)

        props = {'label': label, 'type': 'rectangle', 'filename': image_name}
        props['coordinates'] = {'height': height,
                                'width': width, 'x': x, 'y': y}

        object_props.append(props)

    unsorted_annotations.append(object_props)

data = tc.image_analysis.load_images('generator/data')

# data['label'] = data['path'].apply(lambda _: 'block')

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
