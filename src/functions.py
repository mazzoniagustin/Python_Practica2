def calculate_points (stats):
    """This function calculates the points of every player"""
    return (stats["kills"] * 3) + (stats["assists"] * 1) - (1 if stats["deaths"] else 0)

def calculate_score (rounds):
    """ This functions calculate the score of each player every round"""
    scores = {}
    mvp_counter = {}
    total_stats = {}
    
    for i, round in enumerate(rounds):
        print (f'-------------------  RONDA {i + 1} --------------------')
        
        round_score = {}
        round_stats = {}
        
        for player in round:
            stats = round[player] # Diccionario dentro de diccionario.
            score = calculate_points(stats)
            round_score[player] = score # Score de la ronda
            if player not in scores:
                scores[player] = 0
            scores[player] += score
            
            round_stats[player] = {
                "kills": stats["kills"],
                "deaths": stats["deaths"],
                "assists": stats["assists"]
            }
            if player not in total_stats:
                total_stats[player] = {"kills": 0, "deaths": 0, "assists": 0}
                
            total_stats[player]["kills"] += stats["kills"]
            total_stats[player]["deaths"] += stats["deaths"]
            total_stats[player]["assists"] += stats["assists"]
        
        descendant_players = sorted(round_score, key= lambda player: round_score[player],reverse=True) 
        
        
        mvp = descendant_players[0] # El MVP siempre va a ser el primero al estar ordenada.
        if mvp not in mvp_counter:
            mvp_counter[mvp] = 0
        mvp_counter[mvp] += 1
        
        print ("Jugador | Puntos | Kills | Asistencias | Muertes")
        print ("--------------------------------------------------")
        
        for player in descendant_players:
            score = round_score[player]
            player_stats = round_stats[player]
            print (f'{player:<7} | {score:<6} | {player_stats["kills"]:<5} | {player_stats["assists"]:<11} | {player_stats["deaths"]}')
        print ('')
        print(f'MVP de la ronda: {mvp} con {round_score[mvp]} puntos. \n')
        
    return scores, mvp_counter, total_stats

def show_ranking(scores, mvp_counter, total_stats):
    """This functions sort and show the final scoreboard of the game."""
    print ('------------------  Scoreboard Final -------------------')
    print ('Jugador | Puntos | Kills | Asistencias | Muertes | MVPs')
    print ('-' * 55)
    
    # Se ordena de menor a mayor la acumulada.
    descendant_players = sorted(scores.keys(), key= lambda player: scores[player],reverse=True) 
    
    for player in descendant_players:
        points = scores[player]
        if player not in mvp_counter:
            mvps = 0
        else:
            mvps = mvp_counter[player]
        player_stats = total_stats[player]
        print (f'{player:<7} | {points:<6} | {player_stats["kills"]:<5} | {player_stats["assists"]:<11} | {player_stats["deaths"]:<7} | {mvps:<4}') 