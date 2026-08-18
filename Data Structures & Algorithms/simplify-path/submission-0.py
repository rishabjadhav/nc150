class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        given an absolute unix path, return the simpified file path

        all paths must start with a single /
        directories must be separated by a single /, no more
        only root dir must end with a /
        no . or .. in the path, simplify these out

        use a STACK to hold our position in the path.
        '''

        stk = []

        dirs = path.split("/")

        for d in dirs:
            print(d)
            if d == ".." and stk:
                stk.pop()
            if d == "." or d == "" or d == "..":
                continue
            else:
                stk.append(d)
        
        simplified = "/"

        if not stk:
            return "/"

        for s in stk:
            simplified += s + "/"

        return simplified[:-1]