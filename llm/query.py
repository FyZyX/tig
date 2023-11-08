import openai

import config

openai.api_key = config.OPENAI_API_KEY


def get_completion(system_prompt, message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )

    return completion.choices[0].message["content"]
