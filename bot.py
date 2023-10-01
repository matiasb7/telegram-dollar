from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters
from currencies import CurrencyModel
from constants import DOLLAR_LABEL, EURO_LABEL, PESOS_LABEL, MESSAGES


class Bot:
    CONVERT_COMMANDS = {
        'convert_to_dolares': {'from_label': 'pesos',
                               'to_label': 'dolares',
                               'internal_from': PESOS_LABEL
                               },
        'convert_to_pesos': {'from_label': 'dolares',
                             'to_label': 'pesos',
                             'internal_from': DOLLAR_LABEL
                             }
    }
    CURRENCIES_PRICE_COMMANDS = {
        'dolar': {'internal_from': DOLLAR_LABEL},
        'euro': {'internal_from': EURO_LABEL}
    }

    INSERT_AMOUNT = 1

    def __init__(self, app):
        self.currencies = CurrencyModel()
        self.app = app

        self._register_commands()

    def _register_commands(self):
        self.app.add_handler(CommandHandler('start', self.start_command))

        for command in self.CURRENCIES_PRICE_COMMANDS.keys():
            self.app.add_handler(CommandHandler(command, self.current_price_command))

        for command in self.CONVERT_COMMANDS.keys():
            self.app.add_handler(ConversationHandler(
                entry_points=[CommandHandler(command, self.prompt_for_amount)],
                states={self.INSERT_AMOUNT: [MessageHandler(filters.TEXT, callback=self.convert)]},
                fallbacks=[],
            ))

        self.app.add_error_handler(self.error)

    async def start_command(self, update, context):
        await update.message.reply_text(MESSAGES['start'])

    async def current_price_command(self, update, context):
        currency = update.message.text.replace('/', '')
        info = self.CURRENCIES_PRICE_COMMANDS[currency]
        value = self.currencies.get_coins(info['internal_from'])
        if value:
            await update.message.reply_text(f'El valor del {currency} es: {value}')
        else:
            await update.message.reply_text(MESSAGES['problem'])

    async def prompt_for_amount(self, update, context):
        context.user_data['currency_info'] = self.CONVERT_COMMANDS[
            update.message.text.replace('/', '')]
        await update.message.reply_text(MESSAGES['insert_amount'])
        return self.INSERT_AMOUNT

    async def convert(self, update, context):
        try:
            amount = float(update.message.text)
        except ValueError:
            await update.message.reply_text(MESSAGES['valid_number'])
            return self.INSERT_AMOUNT

        currency_info = context.user_data['currency_info']
        value = self.currencies.convert(amount, currency_info['internal_from'])
        if value:
            reply = f'{update.message.text} {currency_info["from_label"]} son: {value} {currency_info["to_label"]}'
        else:
            reply = MESSAGES['problem']

        await update.message.reply_text(reply)
        return ConversationHandler.END

    async def error(self, update, context):
        print(f'Update {update} caused error {context.error}')
