import openai_secret_manager
import openai
import telegram

# Use the OpenAI API key
secrets = openai_secret_manager.get_secrets("openai")
openai.api_key = secrets["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"]

# Use the Telegram API key
secrets = openai_secret_manager.get_secrets("telegram_bot")
bot_token = secrets["5929735556:AAFupEOsVNnskK2zKZ44DEbGmGlFxIyO_Ig"]
bot = telegram.Bot(token=bot_token)

def generate_essay(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Handle messages
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    if text == '/essay':
        essay = generate_essay("Write an essay on the topic of your choice:")
        bot.send_message(chat_id=chat_id, text=essay)

bot.set_update_listener(handle_message)
bot.polling()
