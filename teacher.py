from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import re

# Create a new chatbot
bot = ChatBot('CBTBot')

# Train the bot using the English corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Define a dictionary of CBT techniques and their descriptions
cbt_techniques = {
    'Cognitive restructuring': 'Examining and challenging negative thoughts',
    'Behavioral activation': 'Engaging in activities that give a sense of pleasure or accomplishment',
    'Problem-solving skills training': 'Identifying problems and coming up with practical solutions',
    'Relaxation techniques': 'Engaging in relaxation techniques such as deep breathing, progressive muscle relaxation, or visualization',
    'Exposure therapy': 'Gradually exposing oneself to feared situations or stimuli'
}

# Define a regular expression pattern for matching messages that contain a CBT technique keyword
technique_pattern = re.compile(r'(.*)(cognitive restructuring|behavioral activation|problem-solving|relaxation|exposure)(.*)', re.IGNORECASE)

# Start the conversation with the bot
print('Type something to begin...')

while True:
    try:
        user_input = input()

        # Check if the user's message contains a CBT technique keyword
        match = technique_pattern.search(user_input)
        if match:
            # Identify the CBT technique keyword in the user's message and provide a description of the technique
            technique_keyword = match.group(2).title()
            technique_description = cbt_techniques.get(technique_keyword)
            if technique_description:
                print('{} involves {}'.format(technique_keyword, technique_description))
            else:
                print('I\'m sorry, I don\'t know much about that technique. Please try another one.')

        # If the user's message does not contain a CBT technique keyword, get a response from the bot
        else:
            bot_response = bot.get_response(user_input)
            print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
