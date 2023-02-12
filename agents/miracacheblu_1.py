import copy
import random
def trade_with(historical_results, picks_and_trades , overall_standings):
    """
    name your file with the first two letters of:
    - a color (e.g. [gr]een)
    - your first name (e.g. [an]tony)
    - your last name (e.g. [co]sta)
    - a sport (e.g. [pa]del)
    - your zodiac sign (e.g. [le]o)
    """
    # get current distribution of gifts
    current_standing = picks_and_trades[list(picks_and_trades.keys())[-1]]['decisions']
    gifts = list(current_standing.values())
    
    # get random gift
    best_gift = random.choice(gifts)
    trade = list(picks_and_trades[list(picks_and_trades.keys())[-1]]['decisions'].keys())[-1]  
    
    return trade
