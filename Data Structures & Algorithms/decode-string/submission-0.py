class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                temp_s = ""
                while stack and stack[-1] != "[":
                    temp_s = stack.pop() + temp_s
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * temp_s)
                
        return "".join(stack)
             