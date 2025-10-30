import os
import time
from tts.tts import TextToSpeech


def test_list_voices():
    t = TextToSpeech()
    voices = t.list_voices()
    assert isinstance(voices, list)
    assert len(voices) > 0


def test_save_to_file(tmp_path):
    t = TextToSpeech()
    out = tmp_path / "test_output.wav"
    # Try saving a very short utterance. If the platform driver writes a file
    # this should exist and be non-empty.
    t.save_to_file("testing one two", str(out))
    # give the driver a moment (pyttsx3 runAndWait should block until done, but be defensive)
    time.sleep(0.1)
    assert out.exists()
    assert out.stat().st_size > 0
