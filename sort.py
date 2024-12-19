wrdstr = "Hello this Is an Example With cased letters"
words = [word.lower() for word in wrdstr.split()]
words.sort()
print("The sorted words are:")
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)

