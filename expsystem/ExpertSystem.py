"""Simple Vehicle Diagnostics Expert System for AI lab experiment."""

knowledge_base = {
    "battery problem": [
        "engine wont start",
        "dim headlights",
        "clicking sound on startup",
        "battery warning light",
    ],
    "engine overheating": [
        "high temperature gauge",
        "steam from hood",
        "sweet coolant smell",
        "engine shuts down",
    ],
    "tire issues": [
        "vehicle pulling to side",
        "vibration at high speed",
        "visible tread wear",
        "uneven tire wear",
    ],
}


def inference(user_symptoms):
    probability = {}

    for issue in knowledge_base:
        match_count = 0
        for symptom in knowledge_base[issue]:
            if symptom in user_symptoms:
                match_count += 1
        probability[issue] = match_count / len(knowledge_base[issue])

    max_probability = max(probability.values())
    likely_issues = [
        issue for issue, prob in probability.items() if prob == max_probability
    ]

    print("\n--- Diagnostic Result ---")
    if max_probability == 0:
        print("No major vehicle issue detected from given symptoms.")
        print("Advice: Continue regular maintenance or have vehicle inspected by mechanic.")
    elif max_probability == 1:
        print("Most likely issue: " + ", ".join(likely_issues) + ".")
    else:
        percent = round(max_probability * 100, 2)
        print("Possible issue: " + ", ".join(likely_issues) + f" ({percent}% match).")


def ask_symptoms():
    user_symptoms = []
    questions = []

    for issue in knowledge_base:
        questions += knowledge_base[issue]

    # Remove duplicates and preserve first occurrence order.
    questions = list(dict.fromkeys(questions))

    print("--- Vehicle Diagnostics Expert System ---")
    print("Answer with y/n\n")

    for symptom in questions:
        answer = input(f"Do you observe {symptom}? [y/n]: ").strip().lower()
        if answer == "y":
            user_symptoms.append(symptom)

    return user_symptoms


def make_decision():
    symptoms = ask_symptoms()
    inference(symptoms)


make_decision()
