## this file defines all the different ships and weapons that you'll be using
## 1) player ships
## 2) PACT ships
## 3) pirate ships
## 4) weapons

init 2 python:

###  PLAYER Ships ###

    class Sunrider(Battleship): # your ship!
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Cruiser'
            self.name = 'Sunrider'
            self.animation_name = 'sunrider'
            self.faction = 'Player'
            self.max_hp = 1500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 1
            self.max_rockets = 2
            self.missiles = self.max_missiles
            self.rockets = 0
            self.evasion = -25  # cruisers are easy to hit
            self.lbl = 'Battle UI/label_sunrider.png'  #this is the battle avatar
            self.portrait = 'Battle UI/ava_portrait.png'
            self.flak = 40
            self.flak_range = 2
            self.move_cost = 30
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 15
            self.armor = self.base_armor
            store.BM.ships.append(self)  #register itself upon creation
            self.test = 'test1234'
            self.test2 = 'test2'

            ####################VOICES
            self.voice_channel = "avavoice"
            self.selection_voice = ['Ava/Ava Selection 1.ogg','Ava/Ava Selection 2.ogg','Ava/Ava Selection 3.ogg','Ava/Ava Selection 4.ogg','Ava/Ava Selection 5.ogg','Ava/Ava Selection 6.ogg','Ava/Ava Selection 7.ogg']
            self.moveforward_voice = ['Ava/Ava Move Forward 1.ogg','Ava/Ava Move Forward 2.ogg','Ava/Ava Move Forward 3.ogg']
            self.movebackward_voice = ['Ava/Ava Move Backward 1.ogg','Ava/Ava Move Backward 2.ogg','Ava/Ava Move Backward 3.ogg']
            self.buffed_voice = ['Ava/Ava Buffed 1.ogg','Ava/Ava Buffed 2.ogg','Ava/Ava Buffed 3.ogg']
            self.cursed_voice = ['Ava/Ava Cursed 1.ogg','Ava/Ava Cursed 2.ogg','Ava/Ava Cursed 3.ogg']

          ##the sunrider gets personal death code!
        def destroy(self,attacker,no_animation = False):
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            BM.grid[a][b] = False #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            renpy.jump('sunrider_destroyed')

    class BlackJack(Battleship): # defining the Blackjack
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Black Jack'
            self.animation_name = 'blackjack'
            self.faction = 'Player'
            self.max_hp = 600
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.evasion = 25
            self.lbl = 'Battle UI/label_blackjack.png'  #this is the battle avatar
            self.portrait = 'Battle UI/asaga_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/BlackJack/blackjack.png',
                'melee':'gameplay/Animations/BlackJack/blackjack_sword.png',
                'character':"Character/Asaga/asaga_plugsuit_point_happy.png"
                }
            self.flak = 35
            store.BM.ships.append(self)  #register itself upon creation

            ####################VOICES
            self.voice_channel = "asavoice"
            self.attack_voice = ["sound/Voice/Asaga/Asaga Melee 1.ogg","sound/Voice/Asaga/Asaga Melee 2.ogg","sound/Voice/Asaga/Asaga Melee 3.ogg","sound/Voice/Asaga/Asaga Melee 4.ogg"]
            self.no_damage_voice = ["sound/Voice/Asaga/Asaga No Damage 1.ogg","sound/Voice/Asaga/Asaga No Damage 2.ogg","sound/Voice/Asaga/Asaga No Damage 3.ogg","sound/Voice/Asaga/Asaga No Damage 4.ogg","sound/Voice/Asaga/Asaga No Damage 5.ogg","sound/Voice/Asaga/Asaga No Damage 6.ogg"]
            self.selection_voice = ['Asaga/Asaga Select 1.ogg','Asaga/Asaga Select 2.ogg','Asaga/Asaga Select 3.ogg','Asaga/Asaga Select 4.ogg','Asaga/Asaga Select 5.ogg','Asaga/Asaga Select 6.ogg','Asaga/Asaga Select 7.ogg']
            self.moveforward_voice = ['Asaga/Asaga Forward 1.ogg','Asaga/Asaga Forward 2.ogg','Asaga/Asaga Forward 3.ogg']
            self.movebackward_voice = ['Asaga/Asaga Backwards 1.ogg','Asaga/Asaga Backwards 2.ogg','Asaga/Asaga Backwards 3.ogg']
            self.buffed_voice = ['Asaga/Asaga Buffed 1.ogg','Asaga/Asaga Buffed 2.ogg']
            self.cursed_voice = ['Asaga/Asaga Cursed 1.ogg','Asaga/Asaga Cursed 2.ogg','Asaga/Asaga Cursed 3.ogg']

    class Liberty(Battleship):  #you can use any existing blueprint as a base, which makes things really easy.
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Liberty'
            self.animation_name = 'liberty'
            self.faction = 'Player'
            self.max_hp = 475
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.move_cost = 20
            self.evasion = 20
            self.lbl = 'Battle UI/label_liberty.png'  #this is the battle avatar
            self.portrait = 'Battle UI/chigara_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Liberty/side.png'
                }
            self.flak = 0
            self.shield_generation = 35
            self.shields = self.shield_generation
            self.shield_range = 1
            store.BM.ships.append(self)  #register itself upon creation

            ####################VOICES
            self.voice_channel = "chivoice"
            self.selection_voice = ['Chigara/Selection Line 1.ogg','Chigara/Selection Line 2.ogg','Chigara/Selection Line 3.ogg','Chigara/Selection Line 4.ogg','Chigara/Selection Line 5.ogg','Chigara/Selection Line 6.ogg','Chigara/Selection Line 7.ogg',]
            self.moveforward_voice = ['Chigara/Move Forward Line 1.ogg','Chigara/Move Forward Line 2.ogg','Chigara/Move Forward Line 3.ogg']
            self.movebackward_voice = ['Chigara/Move Backward Line 1.ogg','Chigara/Move Backward Line 2.ogg','Chigara/Move Backward Line 3.ogg']
            self.buffed_voice = ['Chigara/Buffed Line 1.ogg','Chigara/Buffed Line 2.ogg']
            self.cursed_voice = ['Chigara/Cursed Line 1.ogg','Chigara/Cursed Line 2.ogg','Chigara/Cursed Line 3.ogg']

    class Phoenix(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Phoenix'
            self.animation_name = 'phoenix'
            self.faction = 'Player'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 0
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 10
            self.hate = 100
            self.evasion = 50
            self.lbl = 'Battle UI/label_phoenix.png'  #this is the battle avatar
            self.portrait = 'Battle UI/icari_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/side.png',
                'melee':'gameplay/Animations/Phoenix/melee.png',
                'character':"Character/Icari/icari_plugsuit_point_angry.png"
                }
            self.flak = 20
            store.BM.ships.append(self)  #register itself upon creation

            ####################VOICES
            self.voice_channel = "icavoice"
            self.selection_voice = ['Icari/Icari Selection 1.ogg','Icari/Icari Selection 2.ogg','Icari/Icari Selection 3.ogg','Icari/Icari Selection 4.ogg','Icari/Icari Selection 5.ogg','Icari/Icari Selection 6.ogg','Icari/Icari Selection 7.ogg']
            self.attack_voice = ['sound/Voice/Icari/Icari Attacking Melee 1.ogg','sound/Voice/Icari/Icari Attacking Melee 2.ogg','sound/Voice/Icari/Icari Attacking Melee 3.ogg','sound/Voice/Icari/Icari Attacking Melee 4.ogg']
            self.no_damage_voice = ['Icari/Icari No Damage 1.ogg','Icari/Icari No Damage 2.ogg','Icari/Icari No Damage 3.ogg','Icari/Icari No Damage 4.ogg','Icari/Icari No Damage 5.ogg','Icari/Icari No Damage 6.ogg','Icari/Icari No Damage 7.ogg']
            self.moveforward_voice = ['Icari/Icari Move Forward 1.ogg','Icari/Icari Move Forward 2.ogg','Icari/Icari Move Forward 3.ogg']
            self.movebackward_voice = ['Icari/Icari Move Backward 1.ogg','Icari/Icari Move Backward 2.ogg','Icari/Icari Move Backward 3.ogg']
            self.buffed_voice = ['Icari/Icari Buffed 1.ogg','Icari/Icari Buffed 2.ogg']
            self.cursed_voice = ['Icari/Icari Cursed 1.ogg','Icari/Icari Cursed 2.ogg','Icari/Icari Cursed 3.ogg','Icari/Icari Cursed 4.ogg']

    class Bianca(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Bianca'
            self.animation_name = 'bianca'
            self.faction = 'Player'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.move_cost = 30
            self.evasion = 20
            self.lbl = 'Battle UI/label_bianca.png'  #this is the battle avatar
            self.portrait = 'Battle UI/claude_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Bianca/side.png'
                }
            self.flak = 0
            self.shield_generation = 35
            self.shields = self.shield_generation
            self.shield_range = 1
            store.BM.ships.append(self)  #register itself upon creation

            ####################VOICES
            self.voice_channel = "clavoice"
            self.selection_voice = ['Claude/Selection 1.ogg','Claude/Selection 2.ogg','Claude/Selection 3.ogg','Claude/Selection 4.ogg','Claude/Selection 5.ogg','Claude/Selection 6.ogg','Claude/Selection 7.ogg',]
            self.moveforward_voice = ['Claude/Forward 1.ogg','Claude/Forward 2.ogg','Claude/Forward 3.ogg']
            self.movebackward_voice = ['Claude/Backward 1.ogg','Claude/Backward 2.ogg','Claude/Backward 3.ogg']
            self.buffed_voice = ['Claude/Buffed 1.ogg','Claude/Buffed 2.ogg']
            self.cursed_voice = ['Claude/Cursed 1.ogg','Claude/Cursed 2.ogg','Claude/Cursed 3.ogg','Claude/Cursed 4.ogg','Claude/Cursed 5.ogg']

    class Seraphim(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Seraphim'
            self.animation_name = 'seraphim'
            self.faction = 'Player'
            self.max_hp = 375
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.hate = 100
            self.evasion = 20
            self.lbl = 'Battle UI/label_seraphim.png'  #this is the battle avatar
            self.portrait = 'Battle UI/sola_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Seraphim/side.png',
                }
            self.flak = 0
            store.BM.ships.append(self)  #register itself upon creation

            ####################VOICES
            self.voice_channel = "solvoice"
            self.selection_voice = ['Sola/Selection 1.ogg','Sola/Selection 2.ogg','Sola/Selection 3.ogg','Sola/Selection 4.ogg','Sola/Selection 5.ogg']
            self.no_damage_voice = ['Sola/Evade 1.ogg','Sola/Evade 2.ogg','Sola/Evade 3.ogg','Sola/Evade 4.ogg','Sola/Evade 5.ogg','Sola/Evade 6.ogg']
            self.moveforward_voice = ['Sola/Forward 1.ogg','Sola/Forward 2.ogg','Sola/Forward 3.ogg']
            self.movebackward_voice = ['Sola/Backward 1.ogg','Sola/Backward 2.ogg','Sola/Backward 3.ogg','Sola/Backward 4.ogg']
            self.buffed_voice = ['Sola/Buffed 1.ogg','Sola/Buffed 2.ogg']
            self.cursed_voice = ['Sola/Curse 1.ogg','Sola/Curse 2.ogg','Sola/Curse 3.ogg','Sola/Curse 4.ogg']

    class Agamemnon(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ship'
            self.name = 'Agamemnon'
            self.animation_name = 'agamemnon'
            self.faction = 'Player'
            self.max_hp = 800
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 50
            self.hate = 300
            self.evasion = 0
            self.lbl = 'Battle UI/label_agamemnon.png'  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0
            store.BM.ships.append(self)  #register itself upon creation

            self.voice_channel = "avavoice"
            self.selection_voice = ['Agamemnon/beep1.ogg']
            self.moveforward_voice = ['Agamemnon/beep2.ogg']
            self.movebackward_voice = ['Agamemnon/beep2.ogg']
            self.buffed_voice = ['Agamemnon/beep2.ogg']
            self.cursed_voice = ['Agamemnon/beep2.ogg']

    class PhoenixBoaster(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Unknown Hostile'
            self.animation_name = 'phoenixboaster'
            self.faction = 'PACT'
            self.max_hp = 700
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 15
            self.base_armor = 4
            self.money_reward = 300
            self.armor = 4
            self.blbl = 'Battle UI/label_phoenixboaster.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/boaster_side.png',
                }
            self.flak = 20
            self.flak_range = 1
            store.BM.ships.append(self)

    class PactBomber(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder' #subtype bomber
            self.name = 'PACT Bomber'
            self.animation_name = 'pactbomber'
            self.faction = 'PACT'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 2
            self.max_rockets = 1
            self.money_reward = 75
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 10  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 5
            self.move_cost = 30
            self.blbl = 'Battle UI/label_pactbomber.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTBomber/side.png',
                }
            self.flak = 0
            self.flak_range = 0
            store.BM.ships.append(self)

    class Mochi(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ship'
            self.name = 'Mochi'
            self.animation_name = 'mochi'
            self.faction = 'Player'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 200
            self.hate = 300
            self.evasion = -20
            self.lbl = 'Battle UI/label_mochi.png'  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0
            store.BM.ships.append(self)  #register itself upon creation

            self.voice_channel = "avavoice"
            self.selection_voice = ['Agamemnon/beep1.ogg']
            self.moveforward_voice = ['Agamemnon/beep2.ogg']
            self.movebackward_voice = ['Agamemnon/beep2.ogg']
            self.buffed_voice = ['Agamemnon/beep2.ogg']
            self.cursed_voice = ['Agamemnon/beep2.ogg']


### PACT ships ###

    class MissileFrigate(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Frigate'
            self.name = 'PACT Missile Frigate'
            self.animation_name = 'pactmissilefrigate'
            self.faction = 'PACT'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.move_cost = 30
            self.money_reward = 50
            self.max_missiles = 6   #a lot of missiles, but it's all it has. things go wrong when it's out anywway
            self.missiles = self.max_missiles
            self.evasion = 0 # frigates get no penalty and no bonus to evasion
            self.blbl = 'Battle UI/label_missilefrigate.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.flak = 0
            self.flak_range = 0
            store.BM.ships.append(self)

    class PactMook(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'PACT Mook'
            self.animation_name = 'pactmook'
            self.faction = 'PACT'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 25
            self.move_cost = 20
            self.base_armor = 0
            self.money_reward = 50
            self.armor = 0
            self.blbl = 'Battle UI/label_pactmook.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTMook/side.png'
                }
            self.flak = 10
            self.flak_range = 1
            store.BM.ships.append(self)

    class PhoenixEnemy(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Phoenix'
            self.animation_name = 'phoenixenemy'
            self.faction = 'PACT'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 50
            self.move_cost = 10
            self.base_armor = 0
            self.money_reward = 200
            self.armor = 0
            self.blbl = 'Battle UI/label_phoenixenemy.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/side_mirror.png',
                'melee':'gameplay/Animations/Phoenix/melee_mirror.png',
                'character':"Character/Icari/icari_plugsuit_point_crazylaugh.png"
                }
            self.flak = 20
            self.flak_range = 1
            store.BM.ships.append(self)

            self.voice_channel = "icavoice"
            self.attack_voice = ["sound/Voice/Icari/Icari Attacking Melee 1.ogg","sound/Voice/Icari/Icari Attacking Melee 2.ogg","sound/Voice/Icari/Icari Attacking Melee 3.ogg","sound/Voice/Icari/Icari Attacking Melee 1.ogg"]

    class PactCruiser(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Cruiser'
            self.name = 'PACT Cruiser'
            self.faction = 'PACT'
            self.animation_name = 'pactcruiser'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 200
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -25  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactcruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.flak = 30
            self.flak_range = 2
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 1
            self.base_armor = 30
            self.move_cost = 30
            self.armor = self.base_armor
            store.BM.ships.append(self)  #register itself upon creation

    class PactOutpost(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Station'
            self.name = 'PACT Outpost'
            self.faction = 'PACT'
            self.animation_name = 'pactstation'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 0
            self.money_reward = 1000
            self.boss = True
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -40  # cruisers are easy to hit
            self.blbl = 'Battle UI/pactstation.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 20
            self.armor = self.base_armor
            self.move_cost = 1000
            store.BM.ships.append(self)  #register itself upon creation

### pirate ships ###

    class PirateBomber(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder' #subtype bomber
            self.name = 'Pirate Bomber'
            self.animation_name = 'piratebomber'
            self.faction = 'Pirate'
            self.max_hp = 350
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 1
            self.max_rockets = 0
            self.money_reward = 50
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 8  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 10
            self.move_cost = 30
            self.blbl = 'Battle UI/label_piratebomber.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PirateBomber/bomber_side.png'
                }
            self.flak = 20
            self.flak_range = 1
            store.BM.ships.append(self)

    class Havoc(PirateBomber):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Havoc'
            self.animation_name = 'havoc'
            self.faction = 'Pirate'
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.boss = True
            self.max_missiles = 2
            self.max_rockets = 1
            self.money_reward = 200
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 14
            self.armor = 14
            self.evasion = 8
            self.move_cost = 30
            self.blbl = 'Battle UI/havoc.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Havoc/havoc.png',
                'melee':'gameplay/Animations/Havoc/havoc_melee.png',
                'character':"Character/Cosette/cosette_plugsuit_front_evilsmile.png"
                }
            self.flak = 20
            self.flak_range = 2
            store.BM.ships.append(self)
            ##voices##
            self.voice_channel = "cosvoice"
            self.attack_voice = ["sound/Voice/Cosette/Cosette Melee Attack 1.ogg","sound/Voice/Cosette/Cosette Melee Attack 2.ogg","sound/Voice/Cosette/Cosette Melee Attack 3.ogg","sound/Voice/Cosette/Cosette Melee Attack 4.ogg"]


    class PirateGrunt(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Ryder'
            self.name = 'Pirate Grunt'
            self.animation_name = 'pirategrunt'
            self.faction = 'Pirate'
            self.max_hp = 275
            self.hp = self.max_hp
            self.max_missiles = 0
            self.max_rockets = 0
            self.base_armor = 0
            self.armor = 0
            self.money_reward = 50
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 12
            self.move_cost = 20
            self.blbl = 'Battle UI/label_pirategrunt.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PirateGrunt/side.png'
                }
            self.flak = 15
            self.flak_range = 1
            store.BM.ships.append(self)

    class PirateDestroyer(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Destroyer'
            self.name = 'Pirate Destroyer'
            self.animation_name = 'piratedestroyer'
            self.faction = 'Pirate'
            self.max_hp = 500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.move_cost = 30
            self.evasion = -10
            self.money_reward = 50
            self.blbl = 'Battle UI/label_piratedestroyer.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.flak = 0
            self.flak_range = 0
            store.BM.ships.append(self)

    class PirateBase(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            self.stype = 'Station'
            self.name = 'Pirate Base'
            self.faction = 'Pirate'
            self.animation_name = 'piratebase'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 5
            self.max_rockets = 0
            self.boss = True
            self.money_reward = 500
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -50  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_piratebase.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 50
            self.armor = self.base_armor
            self.move_cost = 1000
            store.BM.ships.append(self)  #register itself upon creation


### Weapons ###

##############SUNRIDER WEAPONS
    class SunriderLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            self.name = 'Sunrider_Laser'
            self.lbl = 'Battle UI/button_laser.png'

    class SunriderMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 80
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Sunrider_Missile'
            self.lbl = 'Battle UI/button_missile.png'

    class SunriderKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 70
            self.wtype = 'Kinetic'
            self.name = 'Sunrider_Kinetic'
            self.lbl = 'Battle UI/button_kinetic.png'

    class SunriderPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 25
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 90
            self.wtype = 'Pulse'
            self.name = 'Sunrider_Pulse'
            self.lbl = 'Battle UI/button_pulse.png'

    class SunriderAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'Sunrider_Assault'
            self.lbl = 'Battle UI/button_assault.png'

    class SunriderRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 800
            self.energy_use = 30
            self.shot_count = 1
            self.accuracy = 100
            self.uses_rockets = True
            self.uses_missiles = False
            self.wtype = 'Rocket'
            self.name = 'Sunrider_Rocket'
            self.lbl = 'Battle UI/button_rocket.png'

###################BLACK JACK WEAPONS

    class BlackjackLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'Blackjack_Laser'
            self.lbl = 'Battle UI/button_laser.png'

    class BlackjackMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 20
            self.shot_count = 10
            self.accuracy = 70
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Sunrider_Missile'
            self.lbl = 'Battle UI/button_missile.png'

    class BlackjackPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 30
            self.energy_use = 50
            self.shot_count = 8
            self.accuracy = 80
            self.wtype = 'Pulse'
            self.name = 'Sunrider_Pulse'
            self.lbl = 'Battle UI/button_pulse.png'

    class BlackjackAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.name = 'Sunrider_Assault'
            self.lbl = 'Battle UI/button_assault.png'

    class BlackjackMelee(Melee):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 400    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 0
            self.accuracy = 170
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_melee.png'

#############################################LIBERTY WEAPONS

    class LibertyLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 100
            self.energy_use = 50
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'Liberty_Laser'
            self.lbl = 'Battle UI/button_laser.png'

############################################# PACT MISSILE FRIGATE

    class PactFrigateMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.shot_count = 6
            self.energy_use = 60

############################################# PIRATE GRUNT

    class PirateGruntLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 120
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PirateGruntMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 70

    class PirateGruntAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'


######################################### HAVOC

    class HavocMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 70
            self.wtype = 'Missile'

    class HavocAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 50
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'

    class HavocRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

    class HavocMelee(Melee):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 50    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 0
            self.accuracy = 140
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 10

########################################## PIRATE BOMBER

    class PirateBomberMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 6
            self.accuracy = 70
            self.wtype = 'Missile'

    class PirateBomberAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 50
            self.shot_count = 10
            self.accuracy = 60
            self.wtype = 'Assault'

    class PirateBomberRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 200
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

########################################### PIRATE DESTROYER

    class PirateDestroyerLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PirateDestroyerKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 250
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 60

################################################PACT CRUISER

    class PACTCruiserLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 175
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55

    class PACTCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 50
            self.wtype = 'Assault'

################################################PACT OUTPOST

    class PACTOutpostLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110

    class PACTOutpostKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 150
            self.energy_use = 60
            self.shot_count = 2
            self.accuracy = 50

#################################################PACT MOOK

    class PACTMookLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 140
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTMookMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 9
            self.accuracy = 70

    class PACTMookAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 11
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'


############################################## PIRATE BASE

    class PirateBaseKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 100
            self.energy_use = 60
            self.shot_count = 5
            self.accuracy = 40

    class PirateBaseAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 40
            self.wtype = 'Assault'

    class PirateBaseMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 70

##############################################





### SUPPORT SKILLS ###

    class Repair(Support):
        def __init__(self):
            Support.__init__(self)
            self.repair = True
            self.damage = 300 #also used for heals
            self.energy_use = 80
            self.name = 'Repair I'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_repair.png'

    class AccUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'accuracy'
            self.buff_strength = 15
            self.buff_duration = 3
            self.name = 'Aim Up'
            self.lbl = 'Battle UI/button_aimup.png'

    class DamageUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'damage'
            self.buff_strength = 20
            self.buff_duration = 3
            self.name = 'Damage Up'
            self.lbl = 'Battle UI/button_atkup.png'

    class Restore(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'restore'
            self.buff_strength = 1
            self.buff_duration = 1
            self.name = 'Restore'
            self.lbl = 'Battle UI/button_restore.png'

    class Stealth(Support):
        def __init__(self):
            Support.__init__(self)
            self.self_buff = True
            self.energy_use = 20
            self.accuracy = 100
            self.acc_degradation = 100
            self.modifies = 'stealth'
            self.buff_strength = 100
            self.buff_duration = 1
            self.name = 'Stealth'
            self.lbl = 'Battle UI/button_stealth.png'

#### curse skills ####

    class AccDown(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.modifies = 'accuracy'
            self.buff_strength = -25
            self.buff_duration = 3
            self.name = 'Aim Down'
            self.lbl = 'Battle UI/button_aimdown.png'

    class Disable(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.modifies = 'movement_cost'
            self.buff_strength = 100
            self.buff_duration = 1
            self.name = 'Disable'
            self.lbl = 'Battle UI/button_disable.png'

    class FlakOff(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.modifies = 'flak'
            self.buff_strength = -100
            self.buff_duration = 3
            self.name = 'Flak Off'
            self.lbl = 'Battle UI/button_flak.png'

    class ShutOff(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.modifies = 'en'
            self.buff_strength = -100
            self.buff_duration = 3
            self.name = 'Aim Down'
            self.lbl = 'Battle UI/button_aimdown.png'



###are these still used?##

    class Rocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300   #multiplied by shot count
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.accuracy = 60    #seems low, but missiles have very low accuracy degradation over distance.
            self.wtype = 'Rocket'
            self.name = 'Basic Rockets'
            self.shot_count = 2
            self.lbl = 'Battle UI/button_rocket.png'

    class Flak(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 40
            self.accuracy = 130
            self.acc_degradation = 100 #flak is only useful at point blank range
            self.shot_count = 30  #many shots, but any armor will block it
            self.wtype = 'Assault'
            self.name = 'Basic Flak'
            self.lbl = 'Battle UI/button_assault.png'

    class MachineGun(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.accuracy = 50
            self.shot_count = 15  #many shots, but any armor will block most
            self.wtype = 'Assault'
            self.name = 'Basic Assault'
            self.lbl = 'Battle UI/button_assault.png'

#################################################### PHOENIX BOOSTER

    class PhoenixBoasterLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 180
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PhoenixBoasterAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'

########################################## PACT BOMBER

    class PACTBomberMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 70
            self.wtype = 'Missile'

    class PACTBomberRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

    class PACTBomberLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 140
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

 ###########################################PHOENIX

    class PhoenixAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.name = 'Phoenix_Assault'
            self.lbl = 'Battle UI/button_assault.png'

    class PhoenixMelee(Melee):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 250    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 2
            self.lbl = 'Battle UI/button_melee.png'


 ###########################################PHOENIX ENEMY
    class PhoenixEnemyAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'

    class PhoenixEnemyMelee(Melee):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 250    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 2

################################################# SERAPHIM
    class SeraphimKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.shot_count = 1
            self.accuracy = 150

################################################### BIANCA

    class BiancaAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 250
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55
            self.wtype = 'Assault'
            self.name = 'Bianca Shotgun'
            self.lbl = 'Battle UI/button_kinetic.png'






