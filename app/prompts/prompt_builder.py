def build_chat_messages(
    system_prompt: str,
    user_message: str,
):
    return [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_message
        }
    ]