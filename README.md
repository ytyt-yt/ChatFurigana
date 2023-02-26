# Chat Furigana

Convert Kanji to Furigana (振り仮名) in japanese words using [ChatGPT](https://openai.com/blog/chatgpt/).

### Installation

```
pip install -r requirements.txt
```

Save your authentication [config](https://github.com/acheong08/ChatGPT) to `~/.config/revChatGPT/config.json`.

### Example
```python
    cf = ChatFurigana()
    cf.build_bot()
    print(cf.furigana(["振り仮名", "食べる", "飲む", "歩く"]))
    # --> ['振[ふ]り仮[が]名[な]', '食[た]べる', '飲[の]む', '歩[ある]く']
```
