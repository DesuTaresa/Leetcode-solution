class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        stack = []
        visited = set()
        
        for i, c in enumerate(s):
           
            if c in visited:
                continue
  
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                visited.remove(removed)
                
            stack.append(c)
            visited.add(c)
            
        return "".join(stack)
        
            