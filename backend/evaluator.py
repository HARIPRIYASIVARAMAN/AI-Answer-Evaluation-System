from backend.similarity import semantic_similarity
from backend.concepts import extract_concepts

def evaluate_answer(question, model_answer, student_answer):
    """
    Evaluates a student answer against model answer
    Returns score, concept coverage and feedback
    """

    concepts = extract_concepts(model_answer)
    covered = 0

    for concept in concepts:
        score = semantic_similarity(concept, student_answer)
        if score > 0.6:
            covered += 1

    concept_score = covered / len(concepts) if concepts else 0
    final_score = round(concept_score * 10, 2)

    feedback = []

    if concept_score < 0.5:
        feedback.append("Key concepts are missing.")
    if len(student_answer.split()) < 50:
        feedback.append("Answer lacks depth.")
    if not feedback:
        feedback.append("Good explanation overall.")

    return {
        "Score (/10)": final_score,
        "Concept Coverage": f"{covered}/{len(concepts)}",
        "Feedback": feedback
    }
