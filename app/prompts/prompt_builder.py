def build_chat_messages(
    system_prompt: str,
    history_messages: list,
    user_message: str,
    resolved_dates: dict | None = None,
):
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        *history_messages,
    ]

    if resolved_dates:
        messages.append(
            {
                "role": "system",
                "content": (
                    "Resolved date context for this request:\n"
                    f"{resolved_dates}\n"
                    "Use these exact dates when calling tools. "
                    "Do not infer or modify the date range."
                ),
            }
        )

    messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    return messages