from flask import Flask, render_template, request, send_from_directory
import os
from tts.tts import TextToSpeech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voices')
def voices():
    tts = TextToSpeech()
    voices = tts.list_voices()
    return {'voices': voices}

@app.route('/generate', methods=['POST'])
def generate():
    tts = TextToSpeech()
    text = request.form.get('text', '').strip()
    voice = request.form.get('voice', '').strip()
    if not text:
        return {'error': 'No text provided'}, 400

    # Generate a unique filename
    import uuid
    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join('static', 'audio', filename)

    try:
        # Set default voice to Nova-like voice (Zira is closest to Nova)
        if not voice:
            voices = tts.list_voices()
            for v in voices:
                if 'zira' in v.get('name', '').lower():
                    voice = v['id']
                    break
        tts.save_to_file(text, filepath, voice=voice if voice else None)
        return {'audio_url': f'/audio/{filename}'}
    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/audio/<filename>')
def audio(filename):
    return send_from_directory(os.path.join('static', 'audio'), filename)

if __name__ == '__main__':
    os.makedirs('static/audio', exist_ok=True)
    app.run(host='0.0.0.0', debug=True)
