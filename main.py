from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from openai import OpenAI
import os

OAIclient = OpenAI()

# Initialize your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

app_handler = SlackRequestHandler(app)

allowed_channel_names = ["leave-afk", "test-2"]


# Define a listener for mentions
@app.event("app_mention")
def respond_to_mention(body, say, client):
    print("Got mention!")
    print("Received mention event:", body)
    channel_id = body["event"]["channel"]
    thread_author_id = body["event"]["parent_user_id"]
    thread_id = body["event"]["thread_ts"]

    # Get the user who was mentioned in the message
    user_mentioned = body["event"]["text"].split("<@")[1].split(">")[0]
    print("User mentioned ID:", user_mentioned)

    channel_info = client.conversations_info(channel=channel_id)
    # Extract the channel name from the response
    channel_name = channel_info["channel"]["name"]
    print(channel_name)

    # Check if the mentioned user is your bot
    if (
        user_mentioned == os.environ.get("SLACK_BOT_USER_ID")
        and channel_name in allowed_channel_names
    ):
        thread_replies = client.conversations_replies(channel=channel_id, ts=thread_id)
        thread_original_message = thread_replies["messages"][0]["text"]

        # Get the username of the original author
        original_author_info = client.users_info(user=thread_author_id)
        original_author_user_name = original_author_info["user"]["profile"][
            "display_name"
        ]

        # GPT Magic
        completion = OAIclient.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f'You are working in a IT company. You are sympathetic and caring about your coworkers well being. Your name is Naveen. Also suggest some home remedies. make it concise. in the greeting, after Dear, use "<@{thread_author_id}>" also if you think that the person is female, use honorifics, titles, or respectful salutations like Your Excellency, Your Highness, Queen, Honorable, Esteemed or something similar. also in the end add a relatable, sassy and funny motivation quote.',
                },
                {
                    "role": "user",
                    "content": f"Write a get well soon message reply for {original_author_user_name}. He/She texted in the office group that {thread_original_message}",
                },
            ],
        )

        print(completion.choices[0].message.content)
        res_msg = completion.choices[0].message.content

        # Get well soon message
        # message = f"Hey <@{thread_author_id}>, get well soon! NAME -> {original_author_user_name} 🌟"
        message = res_msg

        # Post the message in a thread
        say(text=message, thread_ts=body["event"]["ts"], channel=channel_id)


from fastapi import FastAPI, Request

api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@api.get("/health")
async def health(req: Request):
    return f"OK! {req.headers}"
