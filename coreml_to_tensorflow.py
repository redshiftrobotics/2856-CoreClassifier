"""
DONT USE THIS SCRIPT
This script was created to test a possible way to convert coreml models to tensorflow models using onnx.
"""

import onnxmltools
import coremltools
from keras.models import model_from_json
import onnx
import onnx_caffe2.backend


def load_json_model():
    with open('model/plain_model.json', 'r') as file:
        data = file.read()
        print data.split()[:5]
        return data


# lode the CoreML model
coreml_model = coremltools.utils.load_spec('model/m.mlmodel')

# convert the CoreML model into IR
onnx_model = onnxmltools.convert_coreml(coreml_model, 'model')

prepared_backend = onnx_caffe2.backend.prepare(onnx_model)

# for printing the model
# print onnx.helper.printable_graph(onnx_model.graph)

""" -- mxnet -- """

# sym, arg_params, aux_params = onnx_mxnet.import_model('super_resolution.onnx')

""" -- caff2 -- """

# caffe2_model = caffe2.python.onnx.backend.prepare(onnx_model)
#
# init_net, predict_net = c2.onnx_graph_to_caffe2_net(caffe2_model)
#
# with open("model/init_model.pb", "wb") as f:
#     f.write(init_net.SerializeToString())
# with open("model/predict_model.pb", "wb") as f:
#     f.write(predict_net.SerializeToString())

""" -- tf -- """

# save the model in ir
# onnxmltools.utils.save_model(onnx_model, 'model/ir_model.onnx')

# convert IR to tensorflow model
# tf_model = prepare(onnx_model)

# then export it as a tensorflow model
# tf_model.export_graph("model/tf_model.ckpt")
