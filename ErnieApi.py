import requests
import json


class Ernie:
    APIKEY = "Jq4KC8EmWy6JkTqQ9In31NWv"
    SecretKey = "6X8pbo728iFYcMlZ8TdrFslQQZLg4UbU"
    access_token = "24.442f1f81dec8bf5421d61fadc3dd0b83.2592000.1712488778.282335-55529566"
    ConversationStored = []
    max_length = 10
    length_now = 1

    def __init__(self):
        length_now = 1
        return

    def get_access_token(self):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """

        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + APIKET + "&client_secret=" + SecretKey

        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.access_token = response.json().get("access_token")
        return

    def add_message(self, role, text):
        des = {"role": role, "content": text}
        self.ConversationStored.append(des)
        self.length_now += 1
        if self.length_now > self.max_length:
            del self.conversationStored[1]
            self.length_now -= 1  # api有token上限，因此存储的对话总量也有上限

    def textToText(self, input):
        self.add_message("user", input)
        print(self.ConversationStored)
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + self.access_token

        payload = json.dumps({
            "messages": self.ConversationStored
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.add_message("assistant", response.json().get("result"))
        return response.json().get("result")
