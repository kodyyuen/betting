def american_to_decimal(odds):
    return odds / 100 + 1 if odds > 0 else 1 - (100 / odds)

def decimal_to_american(odds):
    return -100 / (odds - 1) if odds < 2 else (odds - 1) * 100

def append_odds_sign(odds):
    return f'+{odds}' if odds > 0 else odds

def bet_winnings(amt, odds):
    return amt * (american_to_decimal(odds) - 1)

while (True):
    bet_amt = int(input('Enter bet 1 amount:\n'))
    bet_odds = int(input('Enter bet 1 odds:\n'))

    hedge_1_amt = int(input('Enter hedge 1 amount:\n'))
    hedge_1_odds = int(input('Enter hedge 1 odds:\n'))

    hedge_2_odds = int(input('Enter hedge 2 odds:\n'))

    bet_1_winnings = bet_winnings(bet_amt, bet_odds)
    hedge_1_winnings = bet_winnings(hedge_1_amt, hedge_1_odds)
    
    hedge_2_amt = (bet_amt * american_to_decimal(bet_odds) - hedge_1_amt * american_to_decimal(hedge_1_odds)) / american_to_decimal(hedge_2_odds)

    hedge_2_winnings = bet_winnings(hedge_2_amt, hedge_2_odds)

    print(f'\nWith your bet 1 of ${bet_amt} with {append_odds_sign(bet_odds)} odds, hedge 1 of ${hedge_1_amt} with {append_odds_sign(hedge_1_odds)}, and hedge 2 with {append_odds_sign(hedge_2_odds)} odds, you will need to bet ${hedge_2_amt}.\n')
    print(f'If you win bet 1, you will profit ${round(bet_1_winnings, 2)} - ${round(hedge_1_amt, 2)} - ${round(hedge_2_amt, 2)} = ${round(bet_1_winnings - hedge_1_amt - hedge_2_amt, 2)}\n')
    print(f'If you win the hedge bet, you will profit ${hedge_1_winnings} + ${hedge_2_winnings} - ${bet_amt} = ${hedge_1_winnings + hedge_2_winnings - bet_amt}\n')