import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.whisper_asr import transcribe_audio
from backend.evaluator import evaluate_answer
