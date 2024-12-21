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
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer""a"

    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))
num = 7
result = factorial(num)
print("The factorial of", num, "is", result)
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
else:
   print("Null")

test1-private

