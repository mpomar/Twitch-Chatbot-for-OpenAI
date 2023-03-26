# Twitch Chatbot for OpenAI

[Football2Twitch](https://github.com/mpomar/Football2Twitch) was my first attempt at creating a Twitch chatbot. 
Given the popularity of Open AI, I thought it was time to create a new Twitch chatbot. 
What this one does is quite simple:
- It joins the desired Twitch channel and listen to the chat
- It reacts to the !ai command in the chat (ex. !ai who was defeated in the battle of Sedan?)
- It sends the content of the command to Open AI as a prompt
- It returns the Open AI answer to the chat 

## Status

Currently (March 2023) the script works like a charm. I will not maintain the code over time though. Should something change either on Twitch or on Open AI, the script will need to be updated accordingly. 

## Usage / Description

Before running the script, you will need to provide all the needed variables:
1) username: this is the bot username on Twitch 
2) oauth_token: this is the Oauth Token of the Twitch bot
3) channel: this is the Twitch channel the bot will join 
4) openai.api_key: this is the Open API Key you need to connect to Open AI

You might also want to update some Open AI parameters:

1) model: this is the model Open AI will use to generate the answers
3) temperature: this controls the creativity of the answers, I set it to 0.3 to avoid creative answers and keep the bot informative 
4) max_tokens: this controls the length of the answer, I set it to 20 to keep the answers short (OpenAI will charge you more for lengthy answers)

## Final comments
If you found this script useful and want to show some ♥ feel free to connect with [DrFredPlays](https://www.twitch.tv/drfredplays) on Twitch - a follow is always appreciated as well :-D


