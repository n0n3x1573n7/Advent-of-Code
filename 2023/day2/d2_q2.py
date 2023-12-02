with open('./day2/input.txt') as f:
    tot=0
    for line in f.read().strip().split('\n'):
        game, results = line.split(': ')
        game_id = int(game.split()[1])

        res={'red':0, 'blue':0, 'green':0}
        for result in results.split('; '):
            subres={'red':0, 'blue':0, 'green':0}
            for subresult in result.split(', '):
                num, col = subresult.split()
                subres[col]+=int(num)
            for col in res:
                res[col] = max(res[col], subres[col])
        tot+=res['red']*res['blue']*res['green']
    
    print(tot)