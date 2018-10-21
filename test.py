import turicreate as tc

from glob import glob

# load image
test = tc.SFrame(
    {'image': [tc.Image(image) for image in glob('generator/test/*.JPG')]})

# load the model
model = tc.load_model('m.model')

# make predictions for each image
test['predictions'] = model.predict(test)

print(test['predictions']) # print them out

# tell the visualizer how we want to display boxes on the images
test['image_with_predictions'] = tc.object_detector.util.draw_bounding_boxes(
    test['image'],  test['predictions'])

# open the visualizer
test.explore()
