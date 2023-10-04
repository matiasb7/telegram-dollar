# Dollar Telegram Bot

## Overview
Dollar Telegram Bot is an efficient tool designed to provide real-time information on the current exchange rates of Dollar and Euro in comparison to the Argentine Peso. Armed with intuitive commands, users can easily convert values between these currencies right within the Telegram interface.

## Features
- **Real-Time Updates:** Get the latest Dollar and Euro exchange rates instantly.
- **Currency Conversion Commands:** Perform quick and easy currency conversions.
- **Telegram Integration:** Access real-time currency information and conversions directly on Telegram.

## Setup

### Pre-Requisites
1. A Telegram account.
2. Python installed on your local machine or server.

### Steps

#### 1. Create a Telegram Bot
Create your own Telegram bot by following the [official guide](https://core.telegram.org/bots#6-botfather). Note down the API token provided.

#### 2. Clone the Repository
Clone the Dollar Telegram Bot repository to your local machine or server.

#### 3. Install Dependencies
Navigate to the project directory and install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

#### 4. Set Environment Variable
Set the `TELEGRAM_API_TOKEN` environment variable with the API token you received when creating the Telegram bot. You can also set this token inside Github Secrets if you are deploying the bot on a GitHub platform.

#### 5. Run the bot
```bash
python main.py
```

## Usage
Interact with the Dollar Telegram Bot using the following commands for real-time currency information and conversions. Each command is designed to be user-friendly, offering instant responses directly within Telegram.

### Commands:
- `/dolar`: Get the current exchange rate of US Dollar to Argentine Peso.
- `/euro`: Obtain the real-time exchange rate of Euro to Argentine Peso.
- `/convert_to_dolares`: Converts the specified Argentine Peso amount to US Dollars.
- `/convert_to_pesos`: Converts the provided US Dollar amount to Argentine Pesos.

## Support and Contribution
This bot was made only for fun, feel free to contribute!
