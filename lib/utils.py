import os

def transcribe_audio(file, model):
    file.save("audio")
    result = model.transcribe("audio", fp16=False, language='English')
    os.remove("audio")
    return result["text"]

def is_extension_file_allowed(name, extensions=['.mp3', '.mp4', '.wav']): 
    extension = os.path.splitext(name)[1]
    if (extension != '' and extension in extensions):
        return True
    return False