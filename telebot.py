import telebot
import cohere

# Cohere API key
API_KEY = "yA9W2zsTNFb18cMsgCjsqyZiJOtigvRwsv6tRTmv"

# Create a Cohere client instance
co = cohere.Client(API_KEY)

# Create a Telegram bot instance
bot = telebot.TeleBot("7144407559:AAHsnSuAMSsCvBz2rhmbtI1rGVyzAXUzhh4")

# Define a handler for incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Get the text from the incoming message
    text = message.text

    try:
        # Use Cohere to summarize the text
        response = co.summarize(
            text=text,
            length='auto',
            format='auto',
            model='summarize-xlarge',
            additional_command='',
            temperature=0.3,
        )

        # Get the summary from the response
        summary = response.summary

        # Send the summary as a reply
        bot.reply_to(message, summary)

    except Exception as e:
        # Log the error message
        print("Error:", str(e))

        # Handle any errors that occur during summarization
        bot.reply_to(message, "Oops! Something went wrong.")

# Start the Telegram bot
bot.polling()