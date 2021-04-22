class C32:
    start= "A"
    def cull(self):
        if self.start == "A":
            self.start = "B"
            return 0
        elif self.start == "B":
            self.start = "C"
            return 1
        elif self.start == "E":
            self.start = "F"
            return 5
        elif self.start == "G":
            self.start = "H"
            return 10
        else:
            raise RuntimeError

    def print(self):
        if self.start == "C":
            self.start = "D"
            return 2
        elif self.start == "D":
            self.start = "E"
            return 4
        elif self.start == "F":
            self.start = "G"
            return 8
        elif self.start == "H":
            self.start = "B"
            return 11
        elif self.start == "E":
            self.start = "A"
            return 7
        else:
            raise RuntimeError

    def bend(self):
        if self.start == "C":
            self.start = "A"
            return 3
        elif self.start == "F":
            self.start = "C"
            return 9
        elif self.start == "E":
            self.start = "G"
            return 6
        else:
            raise RuntimeError
