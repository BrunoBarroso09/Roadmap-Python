class Enemy:
    health = 5

    def attack_enemy(self):
        if self.health >= 0:
            print('I was attacked and I lost 1 health.')
            self.health -= 1

    def check_health(self):
        if self.health <= 0:
            print("I'm dead because I don't have health.")
        else:
            print("I'm in combat and I have", self.health, "health.")


e1 = Enemy()
e1.attack_enemy()
e1.attack_enemy()
e1.attack_enemy()
e1.attack_enemy()
e1.attack_enemy()
e1.check_health()
print("------")
e1 = Enemy()
e1.attack_enemy()
e1.check_health()