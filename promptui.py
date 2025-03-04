from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt # to design prompt template

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')

# which paper does the user want
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need",
                                                           "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", 
                                                           "Diffusion Models Beat GANs on Image Synthesis"] )

# what should be the level of explanation
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", 
                                                         "Technical",
                                                         "Code-Oriented", 
                                                         "Mathematical"] ) 

# what should be the length of explanation
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", 
                                                           "Medium (3-5 paragraphs)",
                                                           "Long (detailed explanation)"] )

# Designing the prompt template (we created a dynamic prompt for the prompt template)
template = PromptTemplate(
    
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where
     applicable.
     2. Analogies:
   - Use relatable analogies to simplify complex ideas.
     If certain information is not available in the paper, respond with: "Insufficient
    information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    
""",
inputs_variables = ['paper_input', 'style_input', 'length_input'],

)

# after input_variables, you can also define validate=True which checks if you have defined all the placeholders
# in the template. If not, it will raise an error.


# fill the placeholders with the user inputs
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

# invoking the model
if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
    
'''
prompt_generator.py

You can also reuse your prompt templates in other files.
Adding prompt templates always can make the code look bulky.
You can save this template seperately as a json file, and then reuse it whenever and wherever needed.
You can check prompt_generator.py for more details.
'''