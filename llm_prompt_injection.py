import json
from llm import _initialize_llm

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

CLASSIFIER_SYSTEM_PROMPT = SystemMessage(
    content="""
    You are an intent classifier for a chat system.
    
    Classify the user's intent into exactly ONE of the following values:
    - normal
    - context_reset
    - role_change
    - system_override
    
    Respond ONLY in valid JSON.
    No explanations.
    Schema:
    {
      "intent": "{{<one of the allowed values>}}",
      "confidence": <float between 0 and 1>
    }
""")


llm = _initialize_llm()
llm_chain = ChatPromptTemplate.from_template("Here is the user query: {user_query}") | llm | StrOutputParser()


def classify_intent(user_input: str):
    messages = [CLASSIFIER_SYSTEM_PROMPT] + [HumanMessage(content=user_input)]
    response = llm.invoke(messages)
    try:
        data = json.loads(str(response.content))
        return data
    except json.JSONDecodeError:
        return None


ALLOWED_INTENTS = {"normal", "context_reset"}


def call_main_llm(user_input: str):
    return llm_chain.invoke({"user_query": user_input})


def handle_user_message(user_input: str):
    classification = classify_intent(user_input)

    # Classifier failed → degrade safely
    if classification is None:
        return "Sorry, I couldn’t process that request safely."

    intent = classification.get("intent")
    confidence = classification.get("confidence", 0)

    # Hard rule: never allow system override
    if intent == "system_override":
        return "That request is not allowed."

    if intent == "role_change":
        return "Role changes are restricted."

    if intent == "normal" or intent == "context_reset":
        return call_main_llm(user_input)

    return "invalid or malicious input, try again with different question!"


if __name__ == "__main__":
    print(handle_user_message(input("Ask you question\n>")))
