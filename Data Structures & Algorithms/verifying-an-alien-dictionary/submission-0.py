class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap={}
        for i,ch in enumerate(order):
            hashmap[ch]=i
        i=0
        while i<len(words)-1:
            w1=words[i]
            w2=words[i+1]
            for ch in range(min(len(w1),len(w2))):
                if w1[ch]==w2[ch]:
                    continue
                elif hashmap[w1[ch]]<hashmap[w2[ch]]:
                    break
                else:
                    return False
            else:
                if len(w1)>len(w2):
                    return False
                
            i+=1
        return True

        