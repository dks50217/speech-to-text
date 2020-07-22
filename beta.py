from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\speech-to-text\Cloud_Speech_API.json"



def sample_recognize(storage_uri):
    client = speech_v1p1beta1.SpeechClient()
    language_code = "zh-TW"
    sample_rate_hertz = 8000
    enable_automatic_punctuation = True
    enable_word_time_offsets = True

    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "enable_automatic_punctuation":enable_automatic_punctuation,
        "enable_word_time_offsets": enable_word_time_offsets,
    }
    audio = {"uri": storage_uri}
    response = client.recognize(config, audio)
        
    for result in response.results:
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))


sample_recognize("gs://audio_bucket_stt/g51011a5731257.20200714170247614-in.wav")



