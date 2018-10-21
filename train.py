import turicreate as tc
import os

# creates a model then saves it
def create_and_save():
    data = tc.SFrame('data.sframe') # load the image data and annotations from the sframe

    train_data, test_data = data.random_split(0.8) # split the data into training data and test data (80% goes to training)

    """
    create an object detection model with the images and annotations
    if it does not learn within 3 epochs it will terminate early
    """
    model = tc.object_detector.create( # TODO max iterations should be way heigher
        train_data, feature='image', annotations='annotations', max_iterations=200)

    """
    make predictions using the test_data inorder to
    gather statistics about the model
    """
    preds = model.predict(test_data)

    # general data about the model
    metrics = model.evaluate(test_data)
    print 'Accuracy: ', metrics['accuracy']  # model accuracy
    print metrics

    model.save('m.model') # save the created model

    return model

# returns a previsouly created model
def load_saved():
    return tc.load_model('m.model')

# look for a previsouly saved model
def model_exists():
    return os.path.exists('m.model')


if model_exists(): # if we already have a model try loading that one
    model = load_saved()
else: # otherwise we need to train a new model
    model = create_and_save()

model.export_coreml('model/m.mlmodel') # export the model to coreml
