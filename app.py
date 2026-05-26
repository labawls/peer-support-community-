import streamlit as st

st.title("Peer Support Community")

st.subheader("A safe space for students")

st.write(
    "Share your worries anonymously, "
    "find study partners, and support one another."
)
st.header("Anonymous Sharing")

post = st.text_area(
    "Share your worries or struggles"
)

if st.button("Post"):
    st.success("Your post has been shared anonymously!")
    st.write("Your post:")
    st.write(post)

    post = st.text_area(
    "Share your worries or struggles"
)

if st.button("Post"):

    with open("posts.txt", "a") as file:
        file.write(post + "\n")

    st.success("Your post has been shared!")

    st.header("Community Posts")

try:
    with open("posts.txt", "r") as file:
        posts = file.readlines()

    for p in posts:
        st.write("🫂", p)

except FileNotFoundError:
    st.write("No posts yet.")

    st.header("Study Groups")

subject = st.selectbox(
    "Choose a study group",
    ["Math", "Biology", "Chemistry", "Programming"]
)

if st.button("Join Study Group"):
    st.success(f"You joined the {subject} study group!")

    st.header("Words of Encouragement")

message = st.text_input(
    "Send encouragement to students"
)

if st.button("Send Support"):
    st.success("Your encouragement was sent!")
    st.write("💛", message)