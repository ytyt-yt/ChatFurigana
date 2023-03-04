# Chat Furigana

Convert Kanji to Furigana (振り仮名) in japanese words using [ChatGPT](https://openai.com/blog/chatgpt/).

### Installation

```
pip install -r requirements.txt
```

Set enviroment variable `OPENAI_API_KEY`.

### Example
```python
    res = chatfurigana(["振り仮名", "食べる", "飲む", "歩く"])
    print(res)
    # --> ['振[ふ]り仮[が]名[な]', '食[た]べる', '飲[の]む', '歩[ある]く']
```
