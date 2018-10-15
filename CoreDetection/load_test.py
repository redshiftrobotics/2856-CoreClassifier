import coremltools

coremltools.converters.keras.convert('model/m.mlmodel', 'model.h5')
