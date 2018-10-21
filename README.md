# Object detection

## Structure

-   `test.py` test the created model
-   `load_data.py` load the image data and annotations into an sframe
-   `train.py` create and train a model
-   `generator/` generated images annotations and test data
-   `App/` simple iOS app for real time evaluation of the model
-   `model/` location of mlmodel
-   `m.model` turicreate model (download from releases)

## How to run

1. clone this repo
2. install turicreate
3. run `test.py`

### Train model

run `train.py`

### generate sframe

run `load_data.py`

## Example output images

![img](doc/example1)
![img](doc/example2)
![img](doc/example3)
![img](doc/example4)
![img](doc/example5)
![img](doc/example6)
![img](doc/example7)
![img](doc/example8)
![img](doc/example9)

## Layers

```
Neural Network compiler 0: 245 , name = _divscalar0, output shape : (C,H,W) = (3, 416, 416)
Neural Network compiler 1: 100 , name = conv0_fwd, output shape : (C,H,W) = (16, 416, 416)
Neural Network compiler 2: 160 , name = batchnorm0_fwd, output shape : (C,H,W) = (16, 416, 416)
Neural Network compiler 3: 130 , name = leakyrelu0_fwd, output shape : (C,H,W) = (16, 416, 416)
Neural Network compiler 4: 120 , name = pool0_fwd, output shape : (C,H,W) = (16, 208, 208)
Neural Network compiler 5: 100 , name = conv1_fwd, output shape : (C,H,W) = (32, 208, 208)
Neural Network compiler 6: 160 , name = batchnorm1_fwd, output shape : (C,H,W) = (32, 208, 208)
Neural Network compiler 7: 130 , name = leakyrelu1_fwd, output shape : (C,H,W) = (32, 208, 208)
Neural Network compiler 8: 120 , name = pool1_fwd, output shape : (C,H,W) = (32, 104, 104)
Neural Network compiler 9: 100 , name = conv2_fwd, output shape : (C,H,W) = (64, 104, 104)
Neural Network compiler 10: 160 , name = batchnorm2_fwd, output shape : (C,H,W) = (64, 104, 104)
Neural Network compiler 11: 130 , name = leakyrelu2_fwd, output shape : (C,H,W) = (64, 104, 104)
Neural Network compiler 12: 120 , name = pool2_fwd, output shape : (C,H,W) = (64, 52, 52)
Neural Network compiler 13: 100 , name = conv3_fwd, output shape : (C,H,W) = (128, 52, 52)
Neural Network compiler 14: 160 , name = batchnorm3_fwd, output shape : (C,H,W) = (128, 52, 52)
Neural Network compiler 15: 130 , name = leakyrelu3_fwd, output shape : (C,H,W) = (128, 52, 52)
Neural Network compiler 16: 120 , name = pool3_fwd, output shape : (C,H,W) = (128, 26, 26)
Neural Network compiler 17: 100 , name = conv4_fwd, output shape : (C,H,W) = (256, 26, 26)
Neural Network compiler 18: 160 , name = batchnorm4_fwd, output shape : (C,H,W) = (256, 26, 26)
Neural Network compiler 19: 130 , name = leakyrelu4_fwd, output shape : (C,H,W) = (256, 26, 26)
Neural Network compiler 20: 120 , name = pool4_fwd, output shape : (C,H,W) = (256, 13, 13)
Neural Network compiler 21: 100 , name = conv5_fwd, output shape : (C,H,W) = (512, 13, 13)
Neural Network compiler 22: 160 , name = batchnorm5_fwd, output shape : (C,H,W) = (512, 13, 13)
Neural Network compiler 23: 130 , name = leakyrelu5_fwd, output shape : (C,H,W) = (512, 13, 13)
Neural Network compiler 24: 120 , name = pool5_fwd, output shape : (C,H,W) = (512, 13, 13)
Neural Network compiler 25: 100 , name = conv6_fwd, output shape : (C,H,W) = (1024, 13, 13)
Neural Network compiler 26: 160 , name = batchnorm6_fwd, output shape : (C,H,W) = (1024, 13, 13)
Neural Network compiler 27: 130 , name = leakyrelu6_fwd, output shape : (C,H,W) = (1024, 13, 13)
Neural Network compiler 28: 100 , name = conv7_fwd, output shape : (C,H,W) = (1024, 13, 13)
Neural Network compiler 29: 160 , name = batchnorm7_fwd, output shape : (C,H,W) = (1024, 13, 13)
Neural Network compiler 30: 130 , name = leakyrelu7_fwd, output shape : (C,H,W) = (1024, 13, 13)
Neural Network compiler 31: 100 , name = conv8_fwd_output, output shape : (C,H,W) = (105, 13, 13)
Neural Network compiler 32: 300 , name = __tc__internal__ymap_sp_pre, output shape : (C,H,W) = (15, 7, 169)
Neural Network compiler 33: 310 , name = __tc__internal__ymap_sp, output shape : (C,H,W) = (7, 15, 169)
Neural Network compiler 34: 350 , name = __tc__internal__raw_rel_xy_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 35: 130 , name = __tc__internal__rel_xy_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 36: 300 , name = __tc__internal__rel_xy, output shape : (C,H,W) = (2, 2535, 1)
Neural Network compiler 37: 290 , name = __tc__internal__constant_xy, output shape : (C,H,W) = (2, 2535, 1)
Neural Network compiler 38: 230 , name = __tc__internal__xy, output shape : (C,H,W) = (2, 2535, 1)
Neural Network compiler 39: 350 , name = __tc__internal__raw_rel_wh_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 40: 220 , name = __tc__internal__rel_wh_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 41: 300 , name = __tc__internal__rel_wh, output shape : (C,H,W) = (30, 13, 13)
Neural Network compiler 42: 290 , name = __tc__internal__c_anchors, output shape : (C,H,W) = (30, 13, 13)
Neural Network compiler 43: 231 , name = __tc__internal__wh_pre, output shape : (C,H,W) = (30, 13, 13)
Neural Network compiler 44: 300 , name = __tc__internal__wh, output shape : (C,H,W) = (2, 2535, 1)
Neural Network compiler 45: 320 , name = __tc__internal__boxes_out_transposed, output shape : (C,H,W) = (4, 2535, 1)
Neural Network compiler 46: 310 , name = __tc__internal__boxes_out, output shape : (C,H,W) = (2535, 4, 1)
Neural Network compiler 47: 245 , name = coordinates, output shape : (C,H,W) = (2535, 4, 1)
Neural Network compiler 48: 350 , name = __tc__internal__scores_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 49: 175 , name = __tc__internal__probs_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 50: 350 , name = __tc__internal__logit_conf_sp, output shape : (C,H,W) = (1, 15, 169)
Neural Network compiler 51: 130 , name = __tc__internal__conf_sp, output shape : (C,H,W) = (1, 15, 169)
Neural Network compiler 52: 320 , name = __tc__internal__conf_tiled_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 53: 231 , name = __tc__internal__confprobs_sp, output shape : (C,H,W) = (2, 15, 169)
Neural Network compiler 54: 300 , name = __tc__internal__confprobs_transposed, output shape : (C,H,W) = (2, 2535, 1)
Neural Network compiler 55: 310 , name = confidence, output shape : (C,H,W) = (2535, 2, 1)
```
