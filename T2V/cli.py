"""Simple command-line interface for the TTS library.

Usage examples:
  python cli.py --text "hello world"
  python cli.py --file message.txt --save out.wav --voice "Microsoft Zira Desktop"
  python cli.py --list-voices
"""
import argparse
import sys
from tts.tts import TextToSpeech


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description="Text-to-Speech CLI")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--text", "-t", help="Text to speak")
    group.add_argument("--file", "-f", help="Path to text file to read and speak")
    parser.add_argument("--save", "-s", help="Save output to audio file instead of speaking")
    parser.add_argument("--list-voices", action="store_true", help="List available voices")
    parser.add_argument("--voice", help="Voice id or name to use")
    parser.add_argument("--rate", type=int, help="Speech rate (integer)")
    parser.add_argument("--volume", type=float, help="Volume between 0.0 and 1.0")

    args = parser.parse_args(argv)
    tts = TextToSpeech()

    if args.list_voices:
        for v in tts.list_voices():
            print(f"id: {v['id']} name: {v['name']} languages: {v['languages']}")
        return 0

    if not args.text and not args.file:
        parser.print_help()
        return 1

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as fh:
                text = fh.read()
        except Exception as e:
            print(f"Failed to read file: {e}")
            return 2
    else:
        text = args.text

    try:
        if args.save:
            out = tts.save_to_file(text, args.save, voice=args.voice, rate=args.rate, volume=args.volume)
            print(f"Saved audio to: {out}")
        else:
            tts.speak(text, voice=args.voice, rate=args.rate, volume=args.volume, block=True)
    except Exception as e:
        print(f"TTS error: {e}")
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
