import json
from pathlib import Path
from revChatGPT.V1 import Chatbot


CONFIG_PATH = Path('~/.config/revChatGPT/config.json').expanduser()
PROMPT = """
I will give you a list of janpanese words, please label each Kanji with Furigana form one by one.

For example, given input ["行く", "見る", "多い"], you should return ["行[い]く", "見[み]る", "多[おお]い"]

Let's begin with

["私", "仕事"]
"""


class ChatFurigana():

    def build_bot(self):
        with CONFIG_PATH.open() as f:
            config = json.load(f)
        self.chatbot = Chatbot(config)
        for _ in self.chatbot.ask(PROMPT):
            pass

    def furigana(self, words):
        q = json.dumps(words, ensure_ascii=False)
        message = ""
        for data in self.chatbot.ask(q):
            message = data["message"]
        return json.loads(message)


if __name__ == '__main__':
    cf = ChatFurigana()
    cf.build_bot()
    print(cf.furigana(["振り仮名", "食べる", "飲む", "歩く"]))
