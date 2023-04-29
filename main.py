from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import re

bot = ChatBot('CBTBot')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

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

        # Check if the user's message contains a CBT keyword
        match = technique_pattern.search(user_input)
        if match:
            # Identify CBT keyword and describe technique
            technique_keyword = match.group(2).title()
            technique_description = cbt_techniques.get(technique_keyword)
            if technique_description:
                print('{} involves {}'.format(technique_keyword, technique_description))
            else:
                print('I\'m sorry, I don\'t know much about that technique. Please try another one.')

        else:
            bot_response = bot.get_response(user_input)
            print(bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break