class vo:
    def isVowel(self, n):
        if (n.lower() in 'aeiou'):
            print("Vowel")
        elif (n.lower() in 'bcdfghjklmnpqrstvwxyz'):
            print("Consonant")
        else:
            print("invalid")
n = (input())
v = vo()
v.isVowel(n)
