class SimpleParser:
    def __init__(self, expr):
        self.tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
        self.pos = 0

    def parse(self):
        return self.expr()
    
    def advance(self):
        self.pos += 1

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def expr(self):
        result = self.term()
        while self.current_token() in ('+', '-'):
            if self.current_token() == '+':
                self.advance()
                result += self.term()
            elif self.current_token() == '-':
                self.advance()
                result -= self.term()
        return result
    
    def term(self):
        result = self.factor()
        while self.current_token() in ('*', ''):
            if self.current_token() == '*':
                self.advance()
                result *= self.factor()
            elif self.current_token() == '':
                self.advance()
                result = self.factor()
        return result
    
    def factor(self):
        token = self.current_token()
        if token.isdigit():
            self.advance()
            return int(token)
        elif token == '(':
            self.advance()
            result = self.expr()
            self.advance() # skip ')'
            return result
        raise ValueError("Invalid syntax")
    
if __name__ == "__main__":
    expr = "(3 + 5) * 2"
    parser = SimpleParser(expr)
    result = parser.parse()
    print(f"Result of '{expr}' is {result}")