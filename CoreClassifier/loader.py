import turicreate as tc
import os

data = tc.image_analysis.load_images('../dataset')

data['possition'] = data['path'].apply(
    lambda path: os.path.basename(os.path.dirname(path)))

data.save('data.sframe')

data.explore()
