from datetime import date, timedelta
import calendar
import re

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def resolve_date_range(user_message: str) -> dict | None:
    message = user_message.lower().strip()
    today = date.today()

    if "today" in message:
        return {"start_date": today.isoformat(), "end_date": today.isoformat()}

    if "yesterday" in message:
        yesterday = today - timedelta(days=1)
        return {"start_date": yesterday.isoformat(), "end_date": yesterday.isoformat()}

    if "this month" in message:
        start = today.replace(day=1)
        return {"start_date": start.isoformat(), "end_date": today.isoformat()}

    if "last month" in message:
        if today.month == 1:
            year, month = today.year - 1, 12
        else:
            year, month = today.year, today.month - 1
        start = date(year, month, 1)
        end = date(year, month, calendar.monthrange(year, month)[1])
        return {"start_date": start.isoformat(), "end_date": end.isoformat()}

    if "this year" in message:
        start = date(today.year, 1, 1)
        return {"start_date": start.isoformat(), "end_date": today.isoformat()}

    match = re.search(
        r"\b(january|february|march|april|may|june|july|august|september|october|november|december)"
        r"(?:\s+(\d{4}))?\b",
        message,
    )

    if match:
        month = MONTHS[match.group(1)]
        year = int(match.group(2)) if match.group(2) else today.year
        start = date(year, month, 1)
        end = date(year, month, calendar.monthrange(year, month)[1])
        return {"start_date": start.isoformat(), "end_date": end.isoformat()}

    return None