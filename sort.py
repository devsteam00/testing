wrdstr = "Hello this Is an Example With cased letters"
words = [word.lower() for word in wrdstr.split()]
words.sort()
print("The sorted words are:")
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)

