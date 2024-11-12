import os
import logging

# Logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Slack configuration
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
ALLOWED_CHANNEL_NAMES = ["hl-test-bot"]

# OpenAI configuration
OPENAI_MODEL = "gpt-3.5-turbo"
SYSTEM_PROMPT = """You are a caring bot that provides get well soon messages and home remedies. 
Keep responses concise and friendly."""
