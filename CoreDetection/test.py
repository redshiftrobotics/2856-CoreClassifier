import turicreate as tc

from glob import glob

# load image
# tc.image_analysis.load_images('generator/test')
# test = tc.SFrame({'image': [tc.Image('test.jpg')]})
test = tc.SFrame(
    {'image': [tc.Image(image) for image in glob('generator/test/*.JPG')]})

# load the model
model = tc.load_model('m.model')

test['predictions'] = model.predict(test)

print(test['predictions'])

test['image_with_predictions'] = tc.object_detector.util.draw_bounding_boxes(
    test['image'],  test['predictions'])
test.explore()
