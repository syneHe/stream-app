import streamlit as st
from trankit import Pipeline

def ner(sentence):
    p = Pipeline('english', gpu=False)
    return p.ner(sentence)

######################################################
st.title('CogAgent')

st.markdown('''
**A KNOWLEDGE-ENHANCED TEXT REPRESENTATION TOOLKIT FOR NATURAL LANGUAGE UNDERSTANDING**
''')

st.header('NER')
st.info('''
Named entity recognition (NER) is one of the fundamental tasks in natural language processing (NLP)
''')

option = st.selectbox(
    'Input text hear or select an example',
    ('Xi Jinping Sends Messages of Condolences to Presidents of Turkey and Syria', 
     'China will provide 40 million yuan in aid to Turkey'))


st.json(ner(option))
#st.write('You selected:', option)
