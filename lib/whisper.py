import whisper

def get_model(model='base'):
  return whisper.load_model(model)