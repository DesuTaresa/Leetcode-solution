class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        op="+-*/"
        for i in tokens:
            if(i not in op):
                stack.append(i)
            else:
                if(i=="+"):
                    num2=int(stack.pop())
                    num1=int(stack.pop())
                    stack.append(num1+num2)
                elif(i=="-"):
                    num2=int(stack.pop())
                    num1=int(stack.pop())
                    stack.append(num1-num2) 
                elif(i=="*"):
                    num2=int(stack.pop())
                    num1=int(stack.pop())
                    stack.append(num1*num2)  
                else:
                    num2=int(stack.pop())
                    num1=int(stack.pop())
                    stack.append(int(num1/num2))
        return int (stack.pop() )                

        