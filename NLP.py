import streamlit as st
import os
from textblob import TextBlob
import spacy
from gensim.summarization import summarize

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def NLP():
    def sumy_summarizer(docx):
        parser=PlaintextParser.from_string(docx,Tokenizer("english"))
        lex_summarizer=LexRankSummarizer()
        summary=lex_summarizer(parser.document,3)
        summary_list=[str(s) for s in summary]
        result=' '.join(summary_list)
        return result
    st.text("Below You can Enter Any Text and Then Choose a Summarizer to get a Summary of the Entered Text")
    message=st.text_area("Enter Text Here","Type Here...")  
    options=st.selectbox("Choose Summarizer",['sumy','gensim'])
    if st.button("Summarize"):
        if options=='sumy':
            st.text("using Sumy Summarizer..")
            summary_result=sumy_summarizer(message)

        elif options=='gensim':
            st.text("Using Gensim...")
            summary_result=summarize(message)     
        else:
            st.warning("Using Gensim Summarizer...")
            summary_result=summarize(message)

        st.success(summary_result)         
