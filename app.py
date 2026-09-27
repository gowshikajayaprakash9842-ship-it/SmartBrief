import streamlit as st

# Page settings
st.set_page_config(
    page_title="SmartBrief",
    page_icon="📝",
    layout="centered"
)

# Title
st.title("📝 SmartBrief")

st.write("### Turn long text into a short and clear summary")

st.divider()

# Text input
text = st.text_area(
    "Enter your text",
    height=250,
    placeholder="Paste your article, notes or study material here..."
)

# Summarize function
def summarize_text(text):

    sentences = text.split(".")

    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    if len(sentences) <= 3:
        return ". ".join(sentences)

    # Simple beginner summarization
    summary = ". ".join(sentences[:3])

    return summary + "."


# Button
if st.button("✨ Summarize Text", use_container_width=True):

    if text.strip():

        summary = summarize_text(text)

        st.success("Summary created successfully!")

        st.subheader("📄 Summary")

        st.write(summary)

        st.divider()

        # Word counts
        original_words = len(text.split())
        summary_words = len(summary.split())

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Original Words",
                original_words
            )

        with col2:
            st.metric(
                "Summary Words",
                summary_words
            )

    else:

        st.warning("Please enter some text first.")

st.divider()

st.caption("SmartBrief © 2026 | Simple Text Summarization")
