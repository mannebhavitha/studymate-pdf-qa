from config import client

def ask_question(pdf_text, question):
    prompt = f"""
    You are a helpful assistant. Use the following document text to answer the question below.

    Document Text:
    \"\"\"{pdf_text}\"\"\"

    Question: {question}

    Answer:
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()
