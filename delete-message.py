import logging
import os

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

# The ts of the message you want to delete
message_id = "REPLACE_WITH_THE_MESSAGE_ID"
# The ID of the channel that contains the message
channel_id = "REPLACE_WITH_THE_CHANNEL_ID"

try:
    # Call the chat.chatDelete method using the built-in WebClient
    # result = client.chat_delete(channel=channel_id, ts=message_id)
    result = client.users_info(user="REPLACE_WITH_YOUR_BOT_USER_ID")

    logger.info(result)

except SlackApiError as e:
    logger.error(f"Error deleting message: {e}")
