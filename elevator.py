class App:
    def solve(self, a_position, b_position, called_floor):
        self.a_position = a_position
        self.b_position = b_position
        self.called_floor = called_floor

        if a_position == b_position:
          if b_position - called_floor <=1:
            return 'B'
        if a_position - called_floor <=1:
            return 'A'
        if b_position - called_floor <=1:
            return 'B'
        



app = App()

print(app.solve(0,0,1))