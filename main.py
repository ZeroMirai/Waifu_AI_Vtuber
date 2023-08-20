import os
from functions.keys.api_key_chat import API_KEY_OPENAI
from functions.tts import text_to_speech, PlayVoice
from functions.chatbot import chatGPT
from functions.create_subtitle import subtitle

# Change your character name here
name = "kana"
# Change your path to this code here for example "C:\My code\AI_Vtuber"
directory_path = r""

gpt_key = API_KEY_OPENAI
first_time_run = True

# File names
answer_file = "answer.txt"
answer_en_file = "answerEN.txt"
answer_jp_file = "answerJP.txt"
newest_chat_file = "NewestChat.txt"
subtitle_file = "subtitle.txt"
history_file = "ChatHistory.txt"
prompt_file = "RoleAndStory.txt"
story1_file = "story1.txt"
story2_file = "story2.txt"

# File paths
file_path_answer = os.path.join(directory_path, answer_file)
file_path_answer_en = os.path.join(directory_path, answer_en_file)
file_path_answer_jp = os.path.join(directory_path, answer_jp_file)
file_path_story1 = os.path.join(directory_path, story1_file)
file_path_story2 = os.path.join(directory_path, story2_file)
file_path_prompt = os.path.join(directory_path, prompt_file)
file_path_history = os.path.join(directory_path, history_file)
file_path_newest = os.path.join(directory_path, newest_chat_file)

previous_chat = ""


def clear_files(newest_chat_file, subtitle_file, history_file):
    with open(newest_chat_file, "w") as file:
        file.write("the stream just start! introduce yourself")
    open(subtitle_file, "w").close()
    with open(history_file, "w") as file:
        file.write("*this is your chat log*")


# Code to check if the Voicevox engine is already open otherwise code will error
text = "操作する準備ができています"
with open(answer_jp_file, "w", encoding="utf-8") as file:
    file.write(text)
text_to_speech(answer_jp_file)
PlayVoice()

clear_files(newest_chat_file, subtitle_file, history_file)

while True:
    with open(newest_chat_file, "r", encoding="utf-8") as file:
        current_chat = file.read()

    # Check if the chat being read is the same as the previous chat
    if current_chat != previous_chat:
        response = chatGPT(
            gpt_key,
            file_path_prompt,
            file_path_newest,
            file_path_history,
            file_path_answer,
            file_path_answer_jp,
            file_path_answer_en,
            name,
        )
        text_to_speech(file_path_answer_jp)
        previous_chat = current_chat
        with open(answer_en_file, "r", encoding="utf-8") as final_answer_file:
            text = final_answer_file.read()
        subtitle(text)
        PlayVoice()
        with open(history_file, "r", encoding="utf-8") as file:
            file_contents = file.read()

        # Calculate the number of characters in chat log
        character_count = len(file_contents)
        if character_count > 3000:
            with open(history_file, "w") as file:
                file.write("*this is your chat log*")
