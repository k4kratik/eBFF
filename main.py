from fastapi import FastAPI, Request
from slack_bolt.adapter.fastapi import SlackRequestHandler
from services.openai_service import OpenAIService
from services.slack_service import SlackService
from config import logger

# Initialize services
slack_service = SlackService()
openai_service = OpenAIService()
app_handler = SlackRequestHandler(slack_service.app)


@slack_service.app.event("app_mention")
def respond_to_mention(body, say, client):
    logger.debug("Received app mention event")

    try:
        # Get channel info
        channel_id = body["event"]["channel"]
        channel_info = slack_service.get_channel_info(client, channel_id)
        channel_name = channel_info["name"]

        # Check if channel is allowed
        if not slack_service.is_channel_allowed(channel_name):
            logger.warning(
                f"Mention received in unauthorized channel: {channel_name}")
            say(
                text="Sorry, I can only respond in specific channels!",
                thread_ts=body["event"]["ts"],
            )
            return

        # Get thread info
        thread_ts = body["event"].get("thread_ts", body["event"]["ts"])
        thread_messages = slack_service.get_thread_messages(
            client, channel_id, thread_ts)

        # Get original message author
        original_message = thread_messages["messages"][0]
        thread_author_id = original_message["user"]
        user_info = slack_service.get_user_info(client, thread_author_id)
        user_id = user_info["id"]

        # Generate response using OpenAI
        message_text = original_message["text"]
        response = openai_service.generate_response(
            user_id,
            message_text
        )

        # Post the message in thread
        say(text=response, thread_ts=body["event"]["ts"], channel=channel_id)
        logger.debug("Response sent successfully")

    except Exception as e:
        logger.error(f"Error processing mention: {str(e)}")
        say(
            text="Sorry, I encountered an error processing your request.",
            thread_ts=body["event"]["ts"],
        )


# FastAPI app
api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    logger.debug("Received request to /slack/events endpoint")
    return await app_handler.handle(req)


@api.get("/health")
async def health(req: Request):
    logger.debug("Health check requested")
    return {"status": "OK", "headers": dict(req.headers)}
