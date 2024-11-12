# eBFF (electronic Best Friend Forever)

A caring Slack bot that provides personalized get-well-soon messages and home remedies when team members report being unwell.

## Overview

eBFF monitors specific Slack channels where team members post about their availability or health status. When mentioned in a thread, it analyzes the original message and generates a thoughtful, personalized response with well-wishes and relevant home remedies using OpenAI's GPT model.

## Features

- 🤖 Automated well-wishes and support messages
- 🏥 Personalized home remedy suggestions
- 🔒 Channel-specific responses (only works in designated channels)
- 🧵 Thread-based interactions
- 🤝 Personalized responses using team member's real name

## Prerequisites

- Python 3.9+
- A Slack workspace with admin privileges
- OpenAI API key
- Docker (optional)

## Setup Instructions

### 1. Slack App Configuration

1. Create a new Slack App at [api.slack.com/apps](https://api.slack.com/apps)
2. Under "OAuth & Permissions", add the following bot token scopes:
   - `app_mentions:read`
   - `channels:history`
   - `groups:history`
   - `mpim:history`
   - `im:history`
   - `chat:write`
3. Install the app to your workspace
4. Copy the Bot User OAuth Token and Signing Secret

### 2. Environment Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ebff.git
   cd ebff
   ```

2. Copy the environment template:

   ```bash
   cp .env.template .env
   ```

3. Fill in your credentials in `.env`:

   ```
   SLACK_BOT_TOKEN=xoxb-your-bot-token
   SLACK_SIGNING_SECRET=your-signing-secret
   OPENAI_API_KEY=your-openai-api-key
   ```

### 3. Local Development

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   uvicorn main:api --reload --port 3000
   ```

### 4. Docker Deployment

1. Build the Docker image:

   ```bash
   docker build -t ebff .
   ```

2. Run the container:

   ```bash
   docker run -p 3000:3000 --env-file .env ebff
   ```

## Usage

1. Add the bot to the designated channels (default: "leave-afk" and "test-2")
2. When someone posts about being unwell, mention the bot (@eBFF) in a thread reply to their message
3. The bot will analyze the original message and respond with personalized well-wishes and remedies

## Configuration

- Modify `allowed_channel_names` in `main.py` to change which channels the bot responds in
- Adjust the OpenAI prompt in the `respond_to_mention` function to customize the response style

## API Endpoints

- `POST /slack/events`: Handles Slack events
- `GET /health`: Health check endpoint

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Built with [Slack Bolt for Python](https://tools.slack.dev/bolt-python/)
- Powered by OpenAI's GPT-3.5 Turbo
- FastAPI for API endpoints
