import streamlit as st
import ollama

st.set_page_config(
    page_title="Skill Sphere AI",
    page_icon="🎓"
)

st.title("🎓 Skill Sphere AI")
st.subheader("AI-Powered Skill Assessment & Career Guidance")

# ---------------- SIDEBAR ----------------

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Home",
        "Skill Assessment",
        "Career Recommendation",
        "Learning Roadmap",
        "AI Career Assistant"
    ]
)

# ---------------- HOME ----------------

if menu == "Home":

    st.header("Welcome to Skill Sphere AI")

    st.write("""
    Skill Sphere AI is an AI-based platform that helps
    students identify their skills, choose suitable careers,
    create learning roadmaps and get AI career guidance.
    """)

    st.success("Choose an option from the sidebar to begin.")

# ---------------- SKILL ASSESSMENT ----------------

elif menu == "Skill Assessment":

    st.header("🧠 Skill Assessment")

    python = st.slider("Python", 0, 10, 0)
    java = st.slider("Java", 0, 10, 0)
    sql = st.slider("SQL", 0, 10, 0)
    dsa = st.slider("Data Structures", 0, 10, 0)
    communication = st.slider("Communication", 0, 10, 0)

    if st.button("Calculate Score"):

        score = (
            python +
            java +
            sql +
            dsa +
            communication
        ) / 50 * 100

        st.metric(
            "Overall Skill Score",
            f"{score:.1f}%"
        )

        if score >= 75:
            st.success("Excellent skill level!")
        elif score >= 50:
            st.info("Good! Continue improving your skills.")
        else:
            st.warning("You should focus on building your basics.")

# ---------------- CAREER RECOMMENDATION ----------------

elif menu == "Career Recommendation":

    st.header("🎯 Career Recommendation")

    skills = st.multiselect(
        "Select your skills",
        [
            "Python",
            "Java",
            "SQL",
            "Data Structures",
            "Machine Learning",
            "HTML",
            "CSS",
            "JavaScript",
            "Cybersecurity",
            "Networking"
        ]
    )

    if st.button("Recommend Career"):

        if not skills:

            st.warning("Please select your skills.")

        elif "Machine Learning" in skills:

            st.success("Recommended Career: AI/ML Engineer")

        elif "Cybersecurity" in skills:

            st.success("Recommended Career: Cybersecurity Analyst")

        elif "HTML" in skills or "JavaScript" in skills:

            st.success("Recommended Career: Web Developer")

        elif "SQL" in skills:

            st.success("Recommended Career: Data Analyst")

        else:

            st.success("Recommended Career: Software Developer")

# ---------------- LEARNING ROADMAP ----------------

elif menu == "Learning Roadmap":

    st.header("📚 Learning Roadmap")

    career = st.selectbox(
        "Choose your career",
        [
            "Software Developer",
            "Data Analyst",
            "AI/ML Engineer",
            "Cybersecurity Analyst",
            "Web Developer"
        ]
    )

    roadmaps = {

        "Software Developer": [
            "Learn Python/Java",
            "Learn Data Structures",
            "Learn Algorithms",
            "Learn SQL",
            "Learn Git",
            "Build projects"
        ],

        "Data Analyst": [
            "Learn Python",
            "Learn SQL",
            "Learn Excel",
            "Learn Statistics",
            "Learn Pandas",
            "Create data projects"
        ],

        "AI/ML Engineer": [
            "Learn Python",
            "Learn NumPy and Pandas",
            "Learn Statistics",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Build AI projects"
        ],

        "Cybersecurity Analyst": [
            "Learn Networking",
            "Learn Linux",
            "Learn Cybersecurity",
            "Learn Ethical Hacking",
            "Learn Web Security",
            "Practice security labs"
        ],

        "Web Developer": [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn React",
            "Learn SQL",
            "Build websites"
        ]
    }

    for i, step in enumerate(
        roadmaps[career],
        1
    ):
        st.write(f"**{i}.** {step}")

# ---------------- AI ASSISTANT ----------------

elif menu == "AI Career Assistant":

    st.header("🤖 AI Career Assistant")

    question = st.text_area(
        "Ask your career question",
        placeholder="Example: How can I become a Python developer?"
    )

    if st.button("Ask AI"):

        if not question:

            st.warning("Please enter a question.")

        else:

            with st.spinner("AI is thinking..."):

                try:

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "system",
                                "content": """
                                You are Skill Sphere AI,
                                a friendly career guidance
                                assistant for students.
                                Give simple and practical
                                answers.
                                """
                            },
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    )

                    answer = response["message"]["content"]

                    st.subheader("🤖 AI Response")
                    st.write(answer)

                except Exception as e:

                    st.error(
                        "Ollama is not running or the model "
                        "is not installed."
                    )

                    st.write(
                        "Run Ollama and install the model "
                        "using: ollama pull llama3.2"
                    )