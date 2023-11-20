import platform
import os

import openai

import re
from os.path import splitext, exists

import torch
import transformers
from transformers import AutoTokenizer


def break_up_file_to_chunks(filename, chunk_size=2000, overlap=100):
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    with open(filename, 'r') as f:
        text = f.read()

    tokens = tokenizer.encode(text)
    num_tokens = len(tokens)

    chunks = []
    for i in range(0, num_tokens, chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)

    return chunks

os.environ[""] = 'paste your openai api key here'
openai.api_key = os.getenv("")

filename = "A:/Programming/PyProj/Anna_tasks/done_text/output_10_new.txt"

prompt_response = []
tokenizer = AutoTokenizer.from_pretrained("gpt2")
chunks = break_up_file_to_chunks(filename)

for i, chunk in enumerate(chunks):
    prompt_request = "Summarize this meeting transcript: " + tokenizer.decode(chunks[i])
    messages = [{"role": "system", "content": "This is text summarization."}]
    messages.append({"role": "user", "content": prompt_request})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=.5,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    prompt_response.append(response["choices"][0]["message"]['content'].strip())


prompt_request = "Consoloidate these meeting summaries: " + str(prompt_response)

response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_request,
        temperature=.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


meeting_summary = response["choices"][0]["text"]
print(meeting_summary)
