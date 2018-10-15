import turicreate as tc
import os


def create_and_save():
    data = tc.SFrame('data.sframe')

    train_data, test_data = data.random_split(0.8)

    # TODO max iterations should be way heigher
    model = tc.object_detector.create(
        train_data, feature='image', annotations='annotations', max_iterations=2000)

    preds = model.predict(test_data)

    metrics = model.evaluate(test_data)
    # print 'Accuracy: ', metrics['accuracy']
    print metrics

    model.save('m.model')

    return model


def load_saved():
    return tc.load_model('m.model')


def model_exists():
    return os.path.exists('m.model')


if model_exists():
    model = load_saved()
else:
    model = create_and_save()

model.export_coreml('model/m.mlmodel')
