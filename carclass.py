class Car(object):
    def __init__(self,model,color,plate,company,speed):
        self.color= color
        self.company= company
        self.plate= plate
        self.speed= speed
        self.model= model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")

    def changegear(self):
        print("gear changed")

audi= Car('A6','blue','MH8985','audi','120')
print(audi.color)
print(audi.company)
print(audi.plate)
print(audi.speed)
print(audi.model)