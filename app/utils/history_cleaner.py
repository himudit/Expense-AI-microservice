def clean_history_for_rewriter(messages: list) -> list:
    cleaned = []
    for msg in messages:
        content = msg.get("content") or ""
        # Skip messages that look like tool calls
        if content and ">" in content and "{" in content:
            continue
        cleaned.append(msg)
    return cleaned