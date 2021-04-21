class C32:
    state = "A"

    def cull(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 1
        elif self.state == "E":
            self.state = "F"
            return 5
        elif self.state == "G":
            self.state = "H"
            return 10
        else:
            raise RuntimeError

    def print(self):
        if self.state == "C":
            self.state = "D"
            return 2
        elif self.state == "D":
            self.state = "E"
            return 4
        elif self.state == "F":
            self.state = "G"
            return 8
        elif self.state == "H":
            self.state = "B"
            return 11
        elif self.state == "E":
            self.state = "A"
            return 7
        else:
            raise RuntimeError

    def bend(self):
        if self.state == "C":
            self.state = "A"
            return 3
        elif self.state == "F":
            self.state = "C"
            return 9
        elif self.state == "E":
            self.state = "G"
            return 6
        else:
            raise RuntimeError
