import requests
import urllib.parse
import sounddevice as sd
import soundfile as sf
import romajitable

# You can change voice model here, for more information go to 'speaker.json' and 'https://voicevox.hiroshiba.jp/'
model = 60


def text_to_speech(answer_jp_file):
    # Read the Japanese answer from the file
    with open(answer_jp_file, "r", encoding="utf-8") as file:
        answer_jp = file.read()

    # Turn some of the answer that have a english text to katakana text for example if answer_jp contain a word "apple" it'll turn it to "appuru"
    result = romajitable.to_kana(answer_jp)
    katakaned = result.katakana

    # TTS part (make sure you have open VOICEVOX.exe)
    voicevox_url = "http://localhost:50021"
    params_encoded = urllib.parse.urlencode({"text": katakaned, "speaker": model})
    request = requests.post(f"{voicevox_url}/audio_query?{params_encoded}")
    params_encoded = urllib.parse.urlencode(
        {"speaker": model, "enable_interrogative_upspeak": True}
    )
    request = requests.post(
        f"{voicevox_url}/synthesis?{params_encoded}", json=request.json()
    )

    with open("JP_Voice.wav", "wb") as outfile:
        outfile.write(request.content)
        outfile.close


def PlayVoice():
    data, fs = sf.read("JP_Voice.wav", dtype="float32")
    sd.play(data, fs)
    status = sd.wait()
