from fuzzywuzzy import process
from langchain import PromptTemplate, LLMChain

STANDARD_RESPONSES = ['Attend', 'Not attend', 'Possibly attend', 'Other']


def tidy_responses(response_text, keywords, limit=1, threshold=80):
    comparison = process.extract(response_text, keywords, limit=limit)

    if len(comparison) < 1:
        return None

    if comparison[0][1] < threshold:
        return None

    return comparison[0][0]


def perform_message_inference(llm, template, message):
    prompt = PromptTemplate(template=template, input_variables=["message"])

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    output_raw = llm_chain.predict(message=message)

    return output_raw
