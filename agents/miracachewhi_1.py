import copy

def trade_with(historical_results, picks_and_trades , overall_standings):
    """
    name your file with 
    """
    # get current distribution of gifts
    current_standing = picks_and_trades[list(picks_and_trades.keys())[-1]]['decisions']
    gifts = list(current_standing.values())
    
    # get player who holds the best gift
    best_gift = gifts.index(min(gifts))
    trade = list(current_standing.keys())[best_gift]  
    
    return trade
