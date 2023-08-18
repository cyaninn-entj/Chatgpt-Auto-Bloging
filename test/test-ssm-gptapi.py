import boto3
import openai 

def get_parameter_fromSSM() :
    ssm = boto3.client('ssm')

    parameters=['/chatgpt-auto-bloging/chatgpt-api-key']

    for i in parameters:
        response = ssm.get_parameter(
            Name=i,
            WithDecryption=True
        )
        api_key=response['Parameter']['Value']
    
    return api_key

def get_completion(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


openai.api_key=get_parameter_fromSSM()
model="gpt-3.5-turbo"
#model="gpt-3.5"
prompt='im using openai api, and i asked you something, and if i want to ask same or related question next day, can you answer me with our yesterday talk?'
answer=get_completion(prompt,model)
print(answer)