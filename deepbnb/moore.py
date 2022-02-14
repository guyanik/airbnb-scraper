from pprint import pprint

def moore(M):
    for i in range(len(M)):
        M[i] = list(M[i])
    

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'O':
                
                count = 0
                indices = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
                for index in indices:
                    if index[0] in range(len(M)) and index[1] in range(len(M[0])) and M[index[0]][index[1]] == 'X':
                        count += 1
                M[i][j] = str(count)

    for i in range(len(M)):
        M[i] = ''.join(M[i])
    
    return M

M = [
				'XOOXXXOO',
				'OOOOXOXX',
				'XXOXXOOO',
				'OXOOOXXX',
				'OOXXXXOX',
				'XOXXXOXO',
				'OOOXOXOX',
				'XOXXOXOX',
			]

pprint(moore(M))
