import streamlit as st
import tempfile
import sys
import os

# ---------------- FIX IMPORT PATH ----------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)
# ------------------------------------------------

from backend.whisper_asr import transcribe_audio
from backend.evaluator import evaluate_answer

st.set_page_config(page_title="AI Answer Evaluation", layout="centered")

st.title("🎓 AI Answer Evaluation System")
st.write("Evaluate student answers (Text or Audio) like a human examiner")

question = st.text_area("📘 Enter Question")
model_answer = st.text_area("✅ Enter Model Answer")

answer_type = st.radio("Choose Answer Type", ["Text Answer", "Audio Answer"])

student_answer = ""

if answer_type == "Text Answer":
    student_answer = st.text_area("✍️ Student Answer")
else:
    audio_file = st.file_uploader("🎙️ Upload Audio Answer (.wav / .mp3)", type=["wav", "mp3"])
    if audio_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(audio_file.read())
            audio_path = temp.name

        st.info("Transcribing audio using Whisper...")
        student_answer = transcribe_audio(audio_path)

        st.success("Transcription complete!")
        st.subheader("📝 Transcribed Answer")
        st.write(student_answer)

if st.button("Evaluate Answer"):
    if question and model_answer and student_answer:
        result = evaluate_answer(question, model_answer, student_answer)

        st.subheader("📊 Evaluation Result")
        st.write(f"**Score:** {result['Score (/10)']} / 10")
        st.write(f"**Concept Coverage:** {result['Concept Coverage']}")

        st.subheader("🧠 Feedback")
        for f in result["Feedback"]:
            st.write("- ", f)
    else:
        st.warning("Please fill all fields before evaluation.")
