def calculate_points (player):
    """This function calculates the points of every player"""
    return (player["kills"] * 3) + (player["assists"] * 1) - (1 if player["deaths"] else 0)

def calculate_score (rounds):
    """
    Show each round, calculate the Most Valuable Player (MVP),
    and compute the total game score.
    """
    scores = {}
    mvp_counter = {}
    total_stats = {}
    
    for i, round in enumerate(rounds):
        print (f'-------------------  RONDA {i + 1} --------------------')
        
        round_score = {}
        round_stats = {}
        
        for player in round:
            stats = round[player]
            score = calculate_points(stats)
            round_score[player] = score
            scores[player] = scores.get(player, 0) + score     
            
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
        
        descendant_players = sorted(round_score.keys(), key= lambda player: round_score[player],reverse=True) 
        
        
        mvp = descendant_players[0] # El MVP siempre va a ser el primero al estar ordenada.
        mvp_counter[mvp] = mvp_counter.get(mvp, 0) + 1
        
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
        mvps = mvp_counter.get(player, 0)
        player_stats = total_stats[player]
        print (f'{player:<7} | {points:<6} | {player_stats["kills"]:<5} | {player_stats["assists"]:<11} | {player_stats["deaths"]:<7} | {mvps:<4}') 