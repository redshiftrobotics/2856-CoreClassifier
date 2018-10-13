# Core Classifier

## Data Loader

load the data using `loader.py`. The data is loaded from the `dataset` directory and saved as an sframe in the directory `data.sframe`

## Train

train the model using `train.py`. This looks for a model, if it exists it will use that and create a mlmodel from it. Otherwise it will train a new model.

### Accuracy and timing

Given the small data set, it is relatively inaccurate (80% accuracy). It takes about 3 minutes to train on a MBP 15 and about 2 to test.

## App

You can find an xcode project in the `App` directory. This contains a mac app that allows you to test the model you created.

NOTE: the app will automatically use the newest model.

## Accuracy

90% is super inaccurate. How can we make this better?

1.  increase `max_iterations`.
2.  split the data on 0.95 or higher
3.  increase the dataset
4.  process the data better
5.  turn off image flipping (right now the network flips and crops the images to allow for a higher diversity of images but flipping the image turns a left image into a right image. )

```
Logistic regression:
--------------------------------------------------------
Number of examples          : 1260
Number of classes           : 4
Number of feature columns   : 1
Number of unpacked features : 2048
Number of coefficients      : 6147
Starting L-BFGS
--------------------------------------------------------
+-----------+----------+-----------+--------------+-------------------+---------------------+
| Iteration | Passes   | Step size | Elapsed Time | Training Accuracy | Validation Accuracy |
+-----------+----------+-----------+--------------+-------------------+---------------------+
| 0         | 1        | NaN       | 0.049693     | 0.646032          | 0.733333            |
| 1         | 7        | 0.000015  | 0.369243     | 0.646032          | 0.733333            |
| 2         | 9        | 1.000000  | 0.534646     | 0.665079          | 0.750000            |
| 3         | 10       | 1.000000  | 0.656373     | 0.909524          | 0.900000            |
| 4         | 11       | 1.000000  | 0.782559     | 0.872222          | 0.883333            |
| 5         | 12       | 1.000000  | 0.918881     | 0.942063          | 0.916667            |
| 10        | 17       | 1.000000  | 2.152360     | 0.970635          | 0.966667            |
+-----------+----------+-----------+--------------+-------------------+---------------------+
```

## Dependencies

On a mac the only dependency is `turicreate`. You can install this with:

```bash
pip install turicreate
```
