from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

async def run(text):

    path = "voice.wav"

    tts.tts_to_file(
        text=text,
        file_path=path
    )

    return path