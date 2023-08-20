import openai
import time


def separate_language(file_path_answer, file_path_answer_en, file_path_answer_jp):
    with open(file_path_answer, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("en:"):
                text = line[3:]  # Extract the text part after 'en:'
                with open(file_path_answer_en, "w", encoding="utf-8") as en_file:
                    en_file.write(text + "\n")
            elif line.startswith("jp:"):
                text = line[3:]  # Extract the text part after 'jp:'
                with open(file_path_answer_jp, "w", encoding="utf-8") as jp_file:
                    jp_file.write(text + "\n")


def chatGPT(
    gpt_key,
    file_path_prompt,
    file_path_newest,
    file_path_history,
    file_path_answer,
    file_path_answer_jp,
    file_path_answer_en,
    name,
):
    openai.api_key = gpt_key

    # Read prompt, chat history and newest chat from files
    with open(file_path_prompt, "r", encoding="utf-8") as file:
        prompt_content = file.read()
    with open(file_path_history, "r", encoding="utf-8") as file:
        chat_log_content = file.read()
    with open(file_path_newest, "r", encoding="utf-8") as file:
        newest_chat_content = file.read()

    # Function to make the OpenAI API request with retry mechanism
    def make_openai_request():
        messages = [
            {"role": "system", "content": prompt_content},
            {
                "role": "user",
                "content": f"this is chat log:{chat_log_content} this is the newest chat: {newest_chat_content}",
            },
        ]
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        return chat.choices[0].message.content

    # Retry mechanism using exponential backoff
    def retry_with_backoff(func, max_retries=3, initial_wait=1):
        retries = 0
        wait_time = initial_wait

        while retries < max_retries:
            try:
                return func()
            except openai.error.RateLimitError:
                print(
                    "Rate limit exceeded. Retrying in {} seconds...".format(wait_time)
                )
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff
                retries += 1

        raise Exception("Max retries exceeded. Unable to make a successful request.")

    # Use the retry mechanism to make the OpenAI API request
    try:
        reply = retry_with_backoff(make_openai_request)
    except Exception as e:
        print("Error: {}".format(str(e)))
        return

    # Save the assistant's reply to the answer file
    with open(file_path_answer, "w", encoding="utf-8") as raw_file:
        raw_file.write(reply)

    # Separate the reply into English and Japanese parts
    separate_language(file_path_answer, file_path_answer_en, file_path_answer_jp)

    # Read the English answer from the file
    with open(file_path_answer_en, "r", encoding="utf-8") as file:
        answer_en = file.read()

    # Append the English answer to the history file
    with open(file_path_history, "a", encoding="utf-8") as history_file:
        history_file.write(f"\nyou have responded: {answer_en}")

    # Print the English answer in cmd
    print(f"{name}: {answer_en}")
