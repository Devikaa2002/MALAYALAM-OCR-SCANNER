import pytesseract
from keras.models import load_model

# Load the H5 model
model = load_model('/home/gpuaccess/lstmmalmodel.hdf5')

# Convert the model to Tesseract's .traineddata format
pytesseract.pytesseract.run_tesseract_engine(
    model,
    'traineddata',
    psm=pytesseract.pytesseract.PSM.AUTO,
    lstm_choice_mode=pytesseract.pytesseract.LSTM_CHOICES_MODE.LOADCIDGRU
)
