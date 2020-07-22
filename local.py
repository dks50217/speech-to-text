from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Cloud_Speech_API.json"

def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech_v1.SpeechClient()
    language_code = "zh-TW"
    sample_rate_hertz = 8000
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    enable_automatic_punctuation = True
    enable_word_time_offsets = True

    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "enable_automatic_punctuation":enable_automatic_punctuation,
        "enable_word_time_offsets": enable_word_time_offsets,
    }

    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
      
    print(response,file=open('output/out.txt', 'w'))
    
    for result in response.results:
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))

sample_recognize("source/g51011a5731257.20200714170247614-in.wav")
