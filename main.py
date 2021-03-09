import random
class Character:
    #constructors
    def __init__(self,power,life,defense,speed,luck):
        self.power = power
        self.life = life
        self.speed = speed
        self.luck = luck
        self.defense = defense

    #function double power
    def dragon_power(self):
        self.power *= 2

    #function half power opponent
    def opponent_half(self):
        self.power = self.power / 2


#SETTER and GETTER
    def get_life(self):
        return self.life

    def set_life(self,x):
        self.life = x

    def get_power(self):
        return self.power

    def set_power(self,x):
        self.power = x


    def get_luck(self):
        return self.luck

    def set_luck(self,x):
        self.luck = x


    def get_speed(self):
        return self.speed

    def set_speed(self,x):
        self.speed = x


    def get_defense(self):
        return self.defense

    def set_defense(self,x):
        self.defense = x
#-------------------------

def double_power(carl):
    chance_dragon_power = random.randint(1,100)
    if(chance_dragon_power > 0 and chance_dragon_power <= 10):
        print("Carl's power before doubling {}".format(carl.get_power()))
        carl.dragon_power()
        print("Carl's power after doubling {}".format(carl.get_power()))


def half_power(opponent):
    chance_opponent_power = random.randint(1,100)
    if(chance_opponent_power > 0 and chance_opponent_power <= 20):
        print("The opponent's power before halving {}".format(opponent.get_power()))
        opponent.opponent_half()
        print("The opponent's power after having {}".format(opponent.get_power()))

def carl_start_first(carl,opponent):
    print("Carl attaks first \n")
    double_power(carl)
    half_power(opponent)

    for i in range(20):
        ############    CARL              ######################
        chance_luck_opponent = random.randint(0,100)/100
        if(not(chance_luck_opponent <= opponent.get_luck())):
            opponent_life_before_damage = opponent.get_life()
            damange_carl = carl.get_power() - opponent.get_defense()
            opponent_life = opponent.get_life() - damange_carl
            opponent.set_life(opponent_life)
            print("Round: {}".format(i) + " life opponents's before damange {}".format(opponent_life_before_damage)+
                  " carl damange {}".format(damange_carl)+" life opponent's after damage {}"
                  .format(opponent_life <= 0 if 0 else opponent_life)+"\n")
        else:
            print("Carl lost!")

        if(opponent.get_life() <= 0):
            opponent.set_life(0)
            print("Carl win!")

        elif(opponent.get_life() > 100 ):
            opponent.set_life(100)
            break;

############# OPPONENT   ##################
        chance_luck_carl = random.randint(1,100)/100

        if(not(chance_luck_carl <= carl.get_luck())):
            car_life_before_damange = carl.get_life()
            damage_opponent = opponent.get_power() - carl.get_defense()
            carl_life = carl.get_life() - damage_opponent
            carl.set_life(carl_life)
            print("round {}".format(i) + " Carl life's before the damage {}".format(car_life_before_damange) +
                  " opponent damage: {}".format(damage_opponent)+ "Carl life's after the damage{}"
                  .format(carl_life <= 0 if 0 else carl_life)+"\n")
        else:
            print("The opponent lost!")

        if(carl.get_life() <= 0):
            carl.set_life = 0
            print("The opponent win!")

        elif (opponent.get_life() > 100):
            opponent.set_life(100)
            break;

def opponent_start_first(carl,opponent):
    print("The opponent attaks first \n")
    double_power(carl)
    half_power(opponent)

    for i in range(20):
        ################# opponent ###################
        chance_luck_carl = random.randint(1, 100) / 100

        if (not (chance_luck_carl <= carl.get_luck())):
            car_life_before_damange = carl.get_life()
            damage_opponent = opponent.get_power() - carl.get_defense()
            carl_life = carl.get_life() - damage_opponent
            carl.set_life(carl_life)
            print("Round {}".format(i) + " Carl's life before the damage {}".format(car_life_before_damange) +
                  " opponent damage: {}".format(damage_opponent) + "Carl's life after the damage{}"
                  .format(carl_life <= 0 if 0 else carl_life) + "\n")
        else:
            print("The opponent lost!")

        if (carl.get_life() <= 0):
            carl.set_life = 0
            print("The opponent win")
            break
            ############## CARL##################
        chance_luck_opponent = random.randint(0, 100) / 100
        if (not (chance_luck_opponent <= opponent.get_luck())):
            opponent_life_before_damage = opponent.get_life()
            damange_carl = carl.get_power() - opponent.get_defense()
            opponent_life = opponent.get_life() - damange_carl
            opponent.set_life(opponent_life)
            print(
                "Round: {}".format(i) + " Opponent life's before the damage {}".format(opponent_life_before_damage) +
                " carl damange {}".format(damange_carl) + " Opponent life's after after the damage {}"
                .format(opponent_life <= 0 if 0 else opponent_life) + "\n")
        else:
            print("Carl win")

        if (opponent.get_life() <= 0):
            opponent.set_life(0)
            print("Carl lost")
            break;


carl = Character(
random.randint(65,95),
random.randint(60,70),
random.randint(40,50),
random.randint(40,50),
random.randint(10,30)/100
);

opponent = Character(
random.randint(55,80),
random.randint(50,80),
random.randint(35,55),
random.randint(40,60),
random.randint(25,40)/100
);
if(carl.get_speed() > opponent.get_speed()):
    carl_start_first(carl,opponent)
elif(carl.get_speed() < opponent.get_speed()):
    opponent_start_first(carl,opponent)
else:
    print("Depends on luck")
    if(carl.get_luck() > opponent.get_luck()):
        carl_start_first(carl,opponent)
    else:
        opponent_start_first(carl,opponent)