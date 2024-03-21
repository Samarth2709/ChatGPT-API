from openai import OpenAI
import time

client = OpenAI(
    api_key = "", 
)

end = False
while not end:
    systeminput = input("System: \n")
    userinput = input("User: \n")
    if not (userinput):
        break
    
    print("Loading...")

    completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": systeminput},
        {"role": "user", "content": userinput}
            ]
        )
    
    print("__________________________________________")
    print("Assistant: \n")
    print(dict(completion.choices[0].message)['content'] + '\n')

    if not input():
        break
