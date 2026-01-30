import streamlit as st
from PyPDF2 import PdfReader

def get_pdf_text_with_pages(pdf_docs):
    text_pages = []
    for pdf in pdf_docs:
        pdf.seek(0)
        pdf_reader = PdfReader(pdf)
        for page_number, page in enumerate(pdf_reader.pages, start=1):
            text_pages.append((page_number, page.extract_text()))
    return text_pages

def search_text_in_pdf(pages, query):
    matches = []
    for page_number, text in pages:
        if query.lower() in text.lower():
            matches.append((page_number, text))
    return matches

def main():
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon="📚")
    st.header("Chat with Multiple PDFs 📚")
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your file here and click on 'Process'", accept_multiple_files=True, type=["pdf"])
        if st.button("Process"):
            with st.spinner("Processing..."):
                if pdf_docs:
                    try:
                        st.session_state['text_pages'] = get_pdf_text_with_pages(pdf_docs)
                        st.success("PDFs processed successfully! Enter a query to search.")
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                else:
                    st.error("Please upload at least one PDF file.")
    query = st.text_input("Enter a keyword or phrase to search:")
    if st.button("Search"):
        if 'text_pages' in st.session_state and query:
            matches = search_text_in_pdf(st.session_state['text_pages'], query)
            if matches:
                st.success(f"Found {len(matches)} result(s) for '{query}':")
                for match in matches:
                    st.write(f"**Page {match[0]}:**")
                    st.write(match[1])
            else:
                st.warning(f"No results found for '{query}'.")
        elif not query:
            st.warning("Please enter a search query.")
        else:
            st.warning("Please upload and process PDF files first.")

if __name__ == "__main__":
    main()
