import pyttsx3
import threading
import os


class TextToSpeech:
    """Simple Text-to-Speech wrapper around pyttsx3.

    Methods:
    - list_voices() -> list of voice dicts
    - speak(text, voice=None, rate=None, volume=None)
    - save_to_file(text, filename, voice=None, rate=None, volume=None)
    
    This wrapper uses a lock to make calls thread-safe for sequential engines.
    """

    def __init__(self, driver=None):
        # driverName is optional and driver selection is platform dependent
        self.engine = pyttsx3.init(driverName=driver) if driver else pyttsx3.init()
        self.lock = threading.Lock()

    def list_voices(self):
        voices = self.engine.getProperty("voices")
        out = []
        for v in voices:
            out.append({
                "id": v.id,
                "name": getattr(v, "name", ""),
                "languages": getattr(v, "languages", []),
                "gender": getattr(v, "gender", ""),
            })
        return out

    def set_voice(self, voice_id_or_name):
        voices = self.engine.getProperty("voices")
        for v in voices:
            if v.id == voice_id_or_name or getattr(v, "name", None) == voice_id_or_name:
                self.engine.setProperty("voice", v.id)
                return v.id
        raise ValueError(f"Voice not found: {voice_id_or_name}")

    def set_rate(self, rate):
        if rate is not None:
            self.engine.setProperty("rate", int(rate))

    def set_volume(self, volume):
        if volume is not None:
            v = float(volume)
            if not 0.0 <= v <= 1.0:
                raise ValueError("volume must be between 0.0 and 1.0")
            self.engine.setProperty("volume", v)

    def speak(self, text, voice=None, rate=None, volume=None, block=True):
        if not text:
            raise ValueError("text must not be empty")
        with self.lock:
            if voice:
                self.set_voice(voice)
            if rate is not None:
                self.set_rate(rate)
            if volume is not None:
                self.set_volume(volume)
            self.engine.say(text)
            if block:
                self.engine.runAndWait()

    def save_to_file(self, text, filename, voice=None, rate=None, volume=None):
        if not text:
            raise ValueError("text must not be empty")
        if not filename:
            raise ValueError("filename must not be empty")
        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname, exist_ok=True)
        with self.lock:
            if voice:
                self.set_voice(voice)
            if rate is not None:
                self.set_rate(rate)
            if volume is not None:
                self.set_volume(volume)
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
        return filename


__all__ = ["TextToSpeech"]
