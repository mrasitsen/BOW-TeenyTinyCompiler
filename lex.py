class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.length = len(self.source)
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    #process the next character
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= self.length:
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]    


    #look up the next character but don't consume it    
    def peekChar(self):
        peekPos = self.curPos
        if peekPos >= self.length:
            return '\0' #EOF
        else:
            return self.source[peekPos]

    #invlaid token found and abort the process
    def abort(self, message):
        pass

    #skip whitespace
    def skipWhitespace(self):
        pass

    #skip comment
    def skipComment(self):
        pass

    #get the next token
    def nextToken(self):
        pass
