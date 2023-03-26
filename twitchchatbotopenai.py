import websocket
import openai

username = "..."
oauth_token = "..."
channel = "..."
openai.api_key = "..."

class TwitchChatBot:
    def __init__(self, username, oauth_token, channel):
        self.username = username
        self.oauth_token = oauth_token
        self.channel = channel
        self.ws = None

    def connect(self):
        url = f"wss://irc-ws.chat.twitch.tv:443"
        self.ws = websocket.create_connection(url)
        self.ws.send(f"PASS {self.oauth_token}")
        self.ws.send(f"NICK {self.username}")
        self.ws.send(f"JOIN #{self.channel}")

    def listen(self):
        while True:
            try:
                message = self.ws.recv()
                if message == "PING :tmi.twitch.tv\r\n":
                    self.ws.send("PONG :tmi.twitch.tv\r\n")
                if "!ai " in message:
                    fromchat = message.split("!ai ")[1]
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt="Act as an helpful, clever, friendly AI assistant. The assistant always replies with a single, meaningful, concise tagline. I have a question for you: " + fromchat,
                        temperature=0.3,
                        max_tokens=20
                    )
                    message_to_send = response.choices[0].text
                    self.ws.send(f"PRIVMSG #{self.channel} :{message_to_send}")
                print(message)
            except Exception as e:
                print(e)

    def run(self):
        self.connect()
        self.listen()

bot = TwitchChatBot(username=username,
                    oauth_token=oauth_token,
                    channel=channel)

bot.run()