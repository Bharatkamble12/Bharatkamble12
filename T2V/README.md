# Text-to-Voice (TTS) Generator

A small, offline Text-to-Speech starter project using pyttsx3.

Quick start

1. Create a virtual environment and install dependencies (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\\Scripts\\Activate.ps1; pip install -r requirements.txt
```

2. List voices:

```powershell
python cli.py --list-voices
```

3. Speak text:

```powershell
python cli.py --text "Hello world"
```

4. Save to file:

```powershell
python cli.py --text "Hello file" --save out.wav
```

Notes
- This project uses `pyttsx3`, which is offline and uses platform-native speech engines (SAPI5 on Windows).
- If you need higher-quality voices or cloud-based features, consider integrating cloud TTS services.
