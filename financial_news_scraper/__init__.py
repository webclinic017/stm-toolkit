import azure.functions as func
import logging
import datetime
import os
import sys

# Append the path to the /models folder for access to shared models
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models'))
from alpaca import Alpaca
from alpaca_ticker import AlpacaTicker
from cosmos import Cosmos


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    alpaca = Alpaca()
    ticker: AlpacaTicker = alpaca.getTickerInfo("TSLA")
    Alpaca()
    cosmos = Cosmos()
    cosmos.write([ticker])

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


if __name__ == "__main__":
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    alpaca = Alpaca()
    ticker: AlpacaTicker = alpaca.getTickerInfo("TSLA")
    Alpaca()
    cosmos = Cosmos()
    cosmos.write([ticker])

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)