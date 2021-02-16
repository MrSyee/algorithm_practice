from collections import defaultdict

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def is_pelindrom(string):
            if len(string) % 2 == 0
                mid = len(string) // 2 - 1
                if string[0:mid] == string[::-mid]:
                    return True
                else:
                    return False
            else:
                mid = len(string) // 2
                if string[0:mid-1] == string[::-(mid-1)]:
                    return True
                else:
                    return False
        
        pelindromes = defaultdict(list)
        i = 0
        for j in range(len(s)):
            if i == j:
                pelindrome[i].append(i)
                continue
            
            if is_pelindrom(s[i:j]):
                pelindromes[i].append(j)
        
        for ii in pelindromes[i]:
            for j in range(len(s) - ii + 1):
                if ii == j:
                    pelindrome[ii].append(ii)
                    continue

                if is_pelindrom(s[ii:j]):
                    pelindromes[ii].append(j) 
            
        