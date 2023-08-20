from pytchat import LiveChat
import time


def read_youtube_chat(video_id, history_file, newest_chat_file):
    chat = LiveChat(video_id)
    processed_chat_messages = set()  # Set to store processed chat messages

    while chat.is_alive():
        for c in chat.get().sync_items():
            chat_message = f"viewer:{c.author.name} say: {c.message}"
            if chat_message not in processed_chat_messages:
                print(chat_message)
                with open(history_file, "a", encoding="utf-8") as file:
                    file.write("\n" + chat_message)
                processed_chat_messages.add(chat_message)
                with open(newest_chat_file, "w", encoding="utf-8") as file:
                    file.write(chat_message)

        time.sleep(1)  # Add a delay to avoid excessive API requests


video_id = ""  # you can get your video id at your youtube live url for example https://www.youtube.com/watch?v=CSdEsXa your video id is CSdEsXa
newest_chat_file = "NewestChat.txt"
history_file = "ChatHistory.txt"

while True:
    read_youtube_chat(video_id, history_file, newest_chat_file)
    time.sleep(1)
