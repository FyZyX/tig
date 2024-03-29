import openai

client = openai.AsyncClient()


async def get_json_completion(system_prompt, message):
    completion = await client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        response_format={"type": "json_object"},
    )

    return completion.choices[0].message.content
