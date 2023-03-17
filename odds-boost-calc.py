def american_to_decimal(odds):
    return odds / 100 + 1 if odds > 0 else 1 - (100 / odds)

def decimal_to_american(odds):
    return -100 / (odds - 1) if odds < 2 else (odds - 1) * 100

def append_odds_sign(odds):
    return f'+{odds}' if odds > 0 else odds

# max profit boost amount that you can wager
PB_AMOUNT = 50
# profit boost %, 50% = 1.5, 100% = 2, ...
PB_PCT = 1.5
# Expected conversion rate of the free bet
CONVERSION_RATE = 0.7

while (True):
    pb_og_american_odds = int(input('Enter profit boost original odds:\n'))
    hedge_american_odds = int(input('Enter hedge odds:\n'))

    pb_og_odds = american_to_decimal(pb_og_american_odds)
    pb_boosted_odds = pb_og_odds * PB_PCT
    pb_cash_winnings = pb_og_odds * PB_AMOUNT
    pb_boosted_winnings = pb_boosted_odds * PB_AMOUNT - pb_cash_winnings
    pb_total = pb_cash_winnings + pb_boosted_winnings * CONVERSION_RATE
    pb_profit = pb_total - PB_AMOUNT

    hedge_odds = american_to_decimal(hedge_american_odds)
    hedge_amount = pb_total / hedge_odds
    hedge_total = hedge_amount * hedge_odds
    hedge_profit = hedge_total - hedge_amount

    pb_winnings = pb_profit - hedge_amount
    hedge_winnings = hedge_profit - PB_AMOUNT


    print(f'\nYour bet of $50 with {append_odds_sign(pb_og_american_odds)} odds will be boosted to {append_odds_sign(round(decimal_to_american(pb_boosted_odds), 2))} and get you ${round(pb_cash_winnings, 2)} in cash winnings and ${round(pb_boosted_winnings, 2)} in boosted winnings.\n')
    print(f'This will result in ${round(pb_total, 2)} in total winnings, and ${round(pb_profit, 2)} in profit.\n')
    print(f'With hedge odds of {append_odds_sign(hedge_american_odds)}, you will need ${round(hedge_amount, 2)}.\n')
    print(f'This will result in ${round(hedge_total, 2)} in total winnings, and ${round(hedge_profit, 2)} in profit.\n')
    print(f'If you win the original bet, you will profit ${round(pb_profit, 2)} - ${round(hedge_amount, 2)} = ${round(pb_winnings, 2)}\n')
    print(f'If you win the hedge bet, you will profit ${round(hedge_profit, 2)} - ${round(PB_AMOUNT, 2)} = ${round(hedge_winnings, 2)}\n')