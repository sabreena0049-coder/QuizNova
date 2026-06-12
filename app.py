
import streamlit as st
import json, random, os, time
from datetime import datetime

st.set_page_config(page_title="QuizNova", page_icon="🏆")

QUESTIONS_FILE = "questions.json"
LEADERBOARD_FILE = "leaderboard.json"

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=2)

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

st.title("🏆 QuizNova")

page = st.sidebar.radio("Menu", ["Take Quiz", "Leaderboard"])

if page == "Leaderboard":
    st.header("Leaderboard")
    scores = sorted(load_leaderboard(), key=lambda x: x["score"], reverse=True)
    for i, s in enumerate(scores, start=1):
        st.write(f"{i}. {s['name']} - {s['score']}/10 ({s['category']})")
else:
    name = st.text_input("Your Name")
    category = st.selectbox(
    "Category",
    sorted(set(q["category"] for q in questions))
) 

    if not st.session_state.quiz_started:
        if st.button("Start Quiz"):
            category_questions = [q for q in questions if q["category"] == category]
            selected = random.sample(category_questions, min(10, len(category_questions)))
            for q in selected:
                random.shuffle(q["options"])
            st.session_state.selected_questions = selected
            st.session_state.quiz_started = True
            st.session_state.start_time = time.time()
            st.session_state.name = name
            st.session_state.category = category
            st.rerun()

    if st.session_state.quiz_started:
        remaining = max(0, 60 - int(time.time() - st.session_state.start_time))
        st.warning(f"⏳ Time Remaining: {remaining} sec")

        with st.form("quiz"):
            answers = []
            for i, q in enumerate(st.session_state.selected_questions):
                ans = st.radio(q["question"], q["options"], key=i)
                answers.append(ans)

            submitted = st.form_submit_button("Submit")

        if submitted or remaining == 0:
            score = 0
            for ans, q in zip(answers, st.session_state.selected_questions):
                if ans == q["answer"]:
                    score += 1

            data = load_leaderboard()
            data.append({
                "name": st.session_state.name or "Anonymous",
                "score": score,
                "category": st.session_state.category,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            save_leaderboard(data)

            st.success(f"Score: {score}/10")
            st.progress(score * 10)

            if st.button("New Quiz"):
                st.session_state.quiz_started = False
                st.rerun()
