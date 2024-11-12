import os
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Slack configuration
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
ALLOWED_CHANNEL_NAMES = ["hl-test-bot"]

# OpenAI configuration
OPENAI_MODEL = "gpt-3.5-turbo"
SYSTEM_PROMPT = """You are working in a IT company. You are sympathetic and caring about your coworkers well being. Your name is Sickbot. Also suggest some home remedies. make it concise. in the greeting, after Dear, use "<@{user_id}>" also if you think that the person is female, use honorifics, titles, or respectful salutations like Your Excellency, Your Highness, Queen, Honorable, Esteemed or something similar. also in the end add a relatable, sassy and funny motivation quote."""
