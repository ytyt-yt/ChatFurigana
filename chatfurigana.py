import os
import json
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
I will give you a list of janpanese words, please label each Kanji with Furigana one by one.
Please put Kanji in "()" and Furigana in "[]".
"""  # noqa


def chatfurigana(words):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": PROMPT},
            {"role": "user", "content": '["行く", "見る", "多い", "これ", "起こす", 食べ物]'},
            {"role": "assistant", "content": '["(行)[い]く", "(見)[み]る", "(多)[おお]い", "これ", "(起)[こ]す", (食)[た]べ(物)[もの]]'},
            {"role": "user", "content": json.dumps(words, ensure_ascii=False)},
        ]
    )
    return json.loads(completion['choices'][0]['message']['content'])


if __name__ == "__main__":
    res = chatfurigana(["振り仮名", "食べる", "飲む", "歩く"])
    print(res)
