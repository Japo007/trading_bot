from alpaca_trade_api.rest import REST, TimeFrame
from alpaca_trade_api.stream import Stream


class AlpacaPaperSocket(REST):
    def __init__(self):
        super().__init__(
            key_id='PKCXE0TVF1BPMZ0DG3N2',
            secret_key='QuFHvJ4XiGa9lXO03oWtPEl0bR0f83r1Y46uwUTg',
            base_url='https://paper-api.alpaca.markets'
        )
