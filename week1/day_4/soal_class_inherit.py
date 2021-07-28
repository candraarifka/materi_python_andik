class Hewan:
    def __init__(self, name):
        self.name = name
    
    def jenis(self):
        if self.name == 'kucing':
            print("kucing")
        else:
            print("Anjing")
            
class Kucing(Hewan):
    def __init__(self, hewan):
        Hewan.__init__(self, hewan)
    def bunyi(self):
        print("meowww")
        
class Anjing(Hewan):
    def __init__(self, hewan):
        Hewan.__init__(self, hewan)
    def bunyi(self):
        print("gukk gukkk")

def main():
    hewan1 = Kucing("kucing")
    hewan2 = Anjing("anjing")
    hewans = [hewan1,hewan2]
    for hewan in hewans:
        hewan.jenis()
        hewan.bunyi()
main()