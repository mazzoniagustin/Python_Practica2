def calculate_points (player):
    """This function calculates the points of every player"""
    return (player["kills"] * 3) + (player["assists"] * 1) - (1 if player["deaths"] else 0)

def calculate_score (rounds):
    """This function shows every round and calculates the Most Valuable Player(MVP) and the total score of the game."""
    scores = {}
    mvp_counter = {}
    
    for i, round in enumerate(rounds):
        print (f'---- RONDA {i+1} ----')
        
        round_score = {}
        
        for player in round:
            stats = round[player]
            score = calculate_points(stats)
            round_score[player] = score
            scores[player] = scores.get(player,0) + score     
            
        
        descendant_players = sorted(round_score.keys(), key= lambda player: round_score[player],reverse=True) 
        
        
        mvp = descendant_players[0] # El MVP siempre va a ser el primero al estar ordenada.
        mvp_counter[mvp] = mvp_counter.get(mvp,0) + 1
        
        
        for player in descendant_players:
            score = round_score[player]
            print (f'{player}: {score} puntos.')
            
        print(f'MVP de la ronda: {mvp} con {round_score[mvp]} puntos.')
        
    return scores, mvp_counter

def show_ranking(scores, mvp_counter):
    """This functions sort and show the final scoreboard of the game."""
    print ('---- Scoreboard Final ----')
    print ('Jugador | Puntos | MVPs')
    print ('-------------------------')
    
    # Se ordena de menor a mayor la acumulada.
    descendant_players = sorted(scores.keys(), key= lambda player: scores[player],reverse=True) 
    
    for player in descendant_players:
        points = scores[player]
        mvps = mvp_counter.get(player,0)
        print(f'{player:<7} | {points} | {mvps}') 
    
    