"""
This is a simple script to export the created model to coreml for testing
"""

import turicreate as tc

model = tc.load_model('m.model')

model.export_coreml('model/m.mlmodel')
