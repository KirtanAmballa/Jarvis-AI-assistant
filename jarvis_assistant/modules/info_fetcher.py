import datetime
import wikipedia


def get_time():
    return datetime.datetime.now().strftime("The time is %I:%M %p.")


def get_date():
    return datetime.datetime.now().strftime("Today's date is %B %d, %Y.")


def get_time_and_date():
    now = datetime.datetime.now()
    return f"The time is {now:%I:%M %p} and today's date is {now:%B %d, %Y}."


def fetch_wikipedia(query):
    try:
        topic = (
            query.replace("who is", "")
            .replace("what is", "")
            .replace("tell me about", "")
            .strip()
        )
        return wikipedia.summary(topic, sentences=2)
    except Exception:
        return "Sorry, I couldn't find information on that."
