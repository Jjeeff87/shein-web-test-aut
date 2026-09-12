import os
import random
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def get_env(key, default=None):
    """Reads an environment variable (from .env or the system), falling back to a default value."""
    return os.getenv(key, default)


def is_url_reachable(url, timeout=10):
    """Checks whether a URL is reachable (used to check if the site is up)."""
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code < 500
    except requests.RequestException:
        return False


def human_type(element, text, min_delay=0.06, max_delay=0.18):
    """Types text character by character with small random pauses,
    mimicking human typing instead of filling the field instantly
    (send_keys(text) all at once). Reduces the chance that the test's
    behavior looks obviously automated.
    """
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(min_delay, max_delay))


def human_pause(min_delay=0.4, max_delay=1.2):
    """Small random pause between actions (e.g. after a click, before the next step),
    simulating a real person's reaction time."""
    time.sleep(random.uniform(min_delay, max_delay))
