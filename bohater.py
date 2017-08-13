import random
class Potwor:
    # int move, defense, hp, attack_min, attack_max, actions      
    # PVector position        
    def __init__(self, move, defense, hp, attack_min, attack_max, x):#konstruktor
        self.move=move
        self.defense=defense
        self.hp=hp
        self.attack_min=attack_min
        self.attack_max=attack_max
        self.position=x
    
    def Damage(self,enemy_defense): #ile zada obrażeń przeciwnikowi
        damage=random.randint(self.attack_min,self.attack_max)
        damage-=enemy_defense
        damage=max(damage,0)
        return damage       
    
    def Move(self,v): #poruszanie się(uproszczone)
        self.position=v
    
    def TakeDamage(self, damage): #dostaje 
        damage                
        self.hp-=damage                
        if self.hp<=0:                        
            del self        
    
    def NewTour(self):                
        self.actions=2        
    
    def DoAction(self):                
        self.actions-=1        
    
    def Attack(self, enemy):                
        damage=self.Damage(enemy.defense)                
        enemy.TakeDamage(damage)
        self.DoAction()