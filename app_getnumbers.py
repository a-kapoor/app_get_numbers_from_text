import streamlit as st

def extract_numbers(text):
    """
    Extracts all numbers from the given text.
    """
    numbers = [float(x) for x in text.split() if x.isdigit() or x.replace('.', '').isdigit()]
    return numbers

def run_app():
    st.title("Number Extractor")
    st.write("Enter some text below and we'll extract the numbers for you.")

    text = st.text_area("Enter Text")

    if st.button("Extract Numbers"):
        numbers = extract_numbers(text)
        if numbers:
            st.write("The numbers found in the text are:")
            st.write(numbers)
        else:
            st.write("No numbers found in the text.")

if __name__ == "__main__":
    run_app()
