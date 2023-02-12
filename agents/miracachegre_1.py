import copy

def trade_with(historical_results, picks_and_trades , overall_standings):
    """
    name your file with the first two letters of:
    - a color (e.g. [gr]een)
    - your first name (e.g. [an]tony)
    - your last name (e.g. [co]sta)
    - a sport (e.g. [pa]del)
    - your zodiac sign (e.g. [le]o)
    """
    # keep my item
    trade = list(picks_and_trades[list(picks_and_trades.keys())[-1]]['decisions'].keys())[-1]  
    
    return trade
