from slack_bolt import App
from config import logger, SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, ALLOWED_CHANNEL_NAMES


class SlackService:
    def __init__(self):
        self.app = App(
            token=SLACK_BOT_TOKEN,
            signing_secret=SLACK_SIGNING_SECRET,
        )

    def get_channel_info(self, client, channel_id: str) -> dict:
        try:
            channel_info = client.conversations_info(channel=channel_id)
            return channel_info["channel"]
        except Exception as e:
            logger.error(f"Error getting channel info: {str(e)}")
            raise

    def get_thread_messages(self, client, channel_id: str, thread_ts: str) -> dict:
        try:
            return client.conversations_replies(channel=channel_id, ts=thread_ts)
        except Exception as e:
            logger.error(f"Error getting thread messages: {str(e)}")
            raise

    def get_user_info(self, client, user_id: str) -> dict:
        try:
            user_info = client.users_info(user=user_id)
            return user_info["user"]
        except Exception as e:
            logger.error(f"Error getting user info: {str(e)}")
            raise

    def is_channel_allowed(self, channel_name: str) -> bool:
        return channel_name in ALLOWED_CHANNEL_NAMES
