with open('./day2/input.txt') as f:
    tot=0
    for line in f.read().strip().split('\n'):
        game, results = line.split(': ')
        game_id = int(game.split()[1])

        for result in results.split('; '):
            res={'red':0, 'blue':0, 'green':0}
            for subresult in result.split(', '):
                num, col = subresult.split()
                res[col]+=int(num)
            if res['red']>12 or res['green']>13 or res['blue']>14:
                break
        else:
            tot+=game_id
                
        print(game_id, tot, res)
    
    print(tot)