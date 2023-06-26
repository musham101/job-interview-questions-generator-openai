import streamlit as st
import requests
import json, time
from globals import API_KEY

api_key = API_KEY

def convert_string_to_json(json_string):
    try:
        json_object = json.loads(json_string)
        return json_object
    except ValueError as e:
        print("Invalid JSON format:", e)
        return None

def make_request(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key,
    }
    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': f'{prompt}',
            },
        ],
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    json_response = json.loads(response.text)
    answers = json_response["choices"][0]["message"]["content"]
    resp = convert_string_to_json(answers)
    if resp == None:
        return answers
    else:
        resp

job_description = st.text_input("Enter Job Description")

prompt = f'i got an interview for a job.\n {job_description}\n this is the job description.\n Can you give me the possible interview questions and their answers that the interviewer can ask?'

if st.button('Get Interview Questions'):
    start_time = time.time()
    api_response = make_request(prompt)
    end_time = time.time()
    st.write('Interview Questions:')
    st.write(api_response)
    elapsed_time = end_time - start_time
    st.write("Response Time: " + str(elapsed_time) + " Seconds")
