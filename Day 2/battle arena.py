class Character:
    def _init_(self,name,health,attack_power,defence,speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defence = defence
        self.speed = speed

    def attack(self,target):
        damage = max(1, self.attack_power - target.defense)  # Minimum 1 damage
        target.take_damage(self.attack_power)
        print(f"{self.name} attacks {target.name}! Deals {damage} damage.")

    def take_damage(self,amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def _init_(self,name,health,attack_power,defence,speed,rage):
        super()._init_(health,name,attack_power,defence,speed)
        self.rage = rage

    def berserk_Mode(self):
        if self.health < (self.health * 0.3):  # If health drops below 30%
            self.attack_power *= 2
            print(f"{self.name} enters Berserk Mode! Attack power doubled!")

class Mage(Character):
    def _init_(self,name,health,attack_power,defence,speed,mana):
        super()._init_(name,health,attack_power,defence,speed)
        self.mana = mana

    def Fireball(self):
        pass

class Archer(Character):
    def _init_(self,name,health,attack_power,defence,speed,critical_chance):
        super()._init_(name,health,attack_power,defence,speed)
        self.critical_chance = critical_chance

    def Precision_Shot(self):
        pass




