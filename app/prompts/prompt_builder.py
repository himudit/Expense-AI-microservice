def build_chat_messages(
    system_prompt: str,
    history_messages: list,
    user_message: str,
):
    return [
        {
            "role": "system",
            "content": system_prompt
        },
        *history_messages,  # add last 10 messages from DB
        {
            "role": "user",
            "content": user_message
        }
    ]