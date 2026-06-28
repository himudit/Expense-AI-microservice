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
                "content": f"""
Resolved date context.

Use these dates exactly when calling tools.

Start Date: {resolved_dates["start_date"]}
End Date: {resolved_dates["end_date"]}

Do not modify these dates.
Do not infer another date range.
    """.strip(),
            }
        )

    messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    return messages