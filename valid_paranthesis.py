
class Solution:
    def __init__(self):
        self.stack = []
    def insert(self,item):

        return self.stack.append(item)
    
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def isValid(self, s: str) -> bool:
        i=0
        n=len(s)
        while(i<n):
            if s[i] in ["(","{","["] :
                self.insert(s[i])
            else: # if closing

                if s[i]== "]":
                    if  self.peek() == "[":
                        self.pop()
                    else:
                        return False
                elif s[i]== "}":
                    if  self.peek() == "{":
                        self.pop()
                    else:
                        return False
                elif s[i]== ")":
                    if  self.peek() == "(":
                        self.pop()
                    else:
                        return False
            i+=1
        
        return len(self.stack)==0
