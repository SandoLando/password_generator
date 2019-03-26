# A password generator
# For all except weak password
# Probability of getting the same password twice ~0.00001746724%
# Probability of getting the same password twice number and all ~1.940827e-10 or 0.000000000194%
import random


def password_strength():
    strength = input("How strong do you want your password? WEAK, MID, or STRONG ").upper()
    return strength


def generator():
    strength = password_strength()
    if strength == 'WEAK':
        adj = '''
            near able rich live safe self away hard high down long born late sure open
            home evil dark many like east good zero sick best lost free thin soft full
            even ugly true nice cold fair past fast real west fine mini dead wild anti
            tall easy kind well lean left deep same cool loud wise pure epic last half made bold
             calm warm holy wide bare slow sent flat sane peak shed plus
             oral salt jain glad weak male busy rude sour shut used otic
             foul just idle held deaf thai eyed tidy bony urdu poor alar sold dull
        '''.split()

        noun = '''
            seven world heart pizza water sixty board month angel
            death green music fifty three party piano mouth woman sugar
            amber dream apple laugh tiger faith earth river money peace forty
            words smile house watch lemon anime stone china
            blood thing light cough story power life love ness ring
             wolf fish five king tree over time have star
             city soul duck foot film lion anna meme safe pain rain sion iron
             ball fire wood care cake back lady work self mole moon
             golf ally nine body down land blue high rock rose wishting baby
             home long line hand girl food hope wind born open wife bird bean
             hair room mine fall hero bell dark jack evil leaf list math goat
             adam head ship face wine hate good edge oven zone
             pear desk fear zeus side gate dana zing asia bear bone pinktaco
             nina band sand mate east maya snow unit best gift bush kiss
             rate move mark corn play zero card ling book town free lost bomb
             sick prom word lord acid lily dove rest idea cent gram four
             gold tube game year cook dish beau itch bath ragehood worm kite
             shot poem nice step loaf form june rice path silk show name suit
             bulb race true tent here rous mess wifi bull barn tone lane cole
             cold yard date gain cube past cone tune hall fair arch oreo rush
             fate park berg sock lava nova york fast
            
        '''.split()

        num = str(random.randint(100,999))
        randomize = Randomizer(adj, noun)

        return randomize.random_insert() + num

    elif strength == 'MID':
        adj = '''
            future animal broken scarce strong indian joyful loving better little julian
            simple stupid hungry public bright united riming second tender modern center double
            square liquid random single german living inside moving rising narrow junior honest
            wicked social canine cereal fabian frozen arctic mobile smooth common linear nepali
            active wasted marine polish muslim fiscal female senior korean feline mental french
            absent insane guilty worthy bovine iconic hollow dental mortal native edible joyous
            trojan humble middle equine steady norman abatic bionic biotic across iambic retail
            sacred burned pulled latino cloudy mature normal cosmic lively acetic gothic wanted
            buried stormy abused tragic atomic floral coital static binary danish jewish gaelic
            shared poetic obtuse closed visual celtic landed opaque polite neuter potent aboral
            sought alpine loaded actual qatari calico rental useful stable mormon innate uneven
            bloody direct arabic scotch extant masted mosaic postal immune carnal meager plural
            rotary stingy spoken manual blonde unreal mystic celiac signed spinal mutant aegean
            manful benign afghan impure ritual folded docile adient fossil banded proven simian
            headed tswana secure annual heroic lamaze astral waning unfair modest colour aortic
            formed metric rested rotten stored sugary savory abasic mutual atonal unsafe artful
            solved custom finite proper covert acidic hebrew serial formal sealed abient amoral
            creole rigged fueled tongan marian starry hourly unsure theist putrid anemic alvine
            raised belted mucous boreal likely walled cooing humane chaste briton bodily lobate
            chalky guided azotic bodied waxing photic beachy inward coptic racial shaped listed
            samoan facial argive buccal baltic turned lesser elated fijian soviet phonic
            '''.split()

        noun ='''
             perfect tuesday country pumpkin special america freedom picture husband monster
             seventy nothing sixteen morning journey history georgia fifteen january
             dolphin teacher kitchen holiday welcome jupiter justice diamond courage
             hundred silence someone science revenge harmony problem penguin blanket yielder
             england dancing musical florida student mercury initial mystery kingdom
             captain library message failure forward honesty fitness sausage popcorn vanilla
             jasmine stomach fortune chicken cheetah fashion uniform probity company patrick
             culture liberty general garbage alcohol goddess lobster climate capital balance
             example purpose running promise program crystal gravity funeral chimney measure
             project volcano respect working whisper quarter element thunder soldier ireland
             snowman october unicorn success sparkle cooking rebecca victory villain
             giraffe panther octopus station cupcake english faction marathi miracle
             college biscuit spanish medical reality cocaine brother vacuole central counter
             weather destiny dracula quality article walking species century stretch warrior
             service montana british dentist tractor wedding fantasy cabbage ability evening
             actress stadium nucleus indiana cricket caution bandana protein baggage numbers
             weekend pretzel subject reading kenning dynasty rainbow houston lithium netball
             feeling coconut chamber italian kannada glitter physics chicago paradox twitter
             poverty impress ironman sangria harvard minuend village plastic meaning
             warning current couplet bromine disease angling radical bezique hormone trouble
             burning surgery minutes address taurine drought goggles product african shallow
             calcium hipster twelfth triumph drawing tristan tweeter phoenix perfume swedish
             thought tiffany captive tonight bargain control camping barring lanyard chapati
             workout average cebuano contest brownie citizen cursive orleans cranium
             machine ceiling mansion smiling formula
        '''.split()

        num = str(random.randint(1000,9999))

        randomize = Randomizer(adj, noun)

        return randomize.random_insert() + num

    elif strength == 'STRONG':
        adj = '''
             american feminine internal personal ordinary physical innocent tropical electric pregnant
             sporadic positive opposite possible accurate chemical hopeless caroline canadian straight
             separate standard thankful fearless original gracious filipino constant biblical friendly
             delicate generous national powerful variable graceful multiple military relative northern
             colorful breaking southern cardinal creative selfless insecure exciting infinite boneless
             glorious catholic acoustic negative juvenile material ultimate allergic adequate official
             overhead athletic absolute circular mindless faithful standing abducted armenian nativist
             dateable comatose familiar brunette scottish truthful sicilian seamless unwanted criminal
             domestic educated prepared compound complete slippery covalent thespian unstable sanitary
             abundant flexible hispanic concrete laxative babbling agitated academic parallel confused
             harmless peaceful sumerian staccato pleasant careless credible epidemic portable animated
             abducent immortal superior neurotic culinary cellular abnormal tolerant dominant gathered
             inverted reliable likeable nonmetal edifying attached pleasing alkaline fallible albanian
             additive bohemian adhesive japanese trusting atlantic aborning auditory peruvian inhalant
             emerging jamaican critical judicial cesarean outgoing dramatic valuable amicable alarming
             backward painless assisted stubborn treeless loveable cerebral stressed existent binomial
             backless nautical prostate impolite vitreous extended tangible meridian cheerful egyptian
             balanced limbless downtown surgical arranged european silenced infernal desirous heavenly
             romantic phonetic balsamic magnetic diatomic fragrant grateful cowardly nigerian accented
             agnostic enclosed punctual abridged decisive palpable existing exacting austrian wireless
             ablative aromatic buddhist bavarian inviting acetonic anglican terminal equipped muscular
             diabetic imperial skeletal approved civilian olympian optional adjusted heedless colonial
             adoptive unshaven ethereal holistic awakened coherent oriented monetary volatile rational
             alveolar exterior abstract dejected forsaken selected amniotic starless hawaiian singular
             clinical tactical incoming regional virtuous faceless artesian eurasian aoristic detected
        '''.split()

        noun = '''
             chocolate christmas happiness wednesday challenge adventure consonant christian masculine
             irregular something knowledge pollution president wrestling pineapple adjective secretary
             halloween ambulance alligator seventeen affection community vegetable influence structure
             packaging nutrition crocodile education beginning boulevard withering breathing sophomore september
             imperfect breakfast xylophone hamburger integrity character adversity charlotte confusion afterlife
             suffering curiosity louisiana celebrity delicious turquoise attention companion elocution agitation
             necessary lightning chemistry recycling treatment spaghetti billboard agreement territory
             amendment architect fledgling ecosystem magnesium twentieth deception caribbean generator
             perimeter amphibian addiction preterite radiation orangutan innocence dandelion nightmare
             commodity abundance direction reference sunflower authority abduction moustache inception
             happening awareness schnitzel hurricane listening prejudice preschool criticism tradition professor
             chameleon gathering scientist astronaut accordion emptiness awakening tangerine waterfall
             injustice nashville jellyfish butterfly sleepover treasurer sanctuary signature shrieking fairytale
             sensation mechanism desperate housewife peninsula halitosis saxophone youngster closeness
             margarita discovery carabiner countdown champlain democracy elevation animation harmonica
             furniture carpenter boyfriend honeymoon snowflake etiquette belonging sacrifice digestion barbarian
             fragrance marketing tellurium caryopsis continent sentiment allowance salvation ascending
             propeller metronome homophone cigarette vancouver equipment blueberry scripture cognition raspberry
             historian commotion automatic rebellion childhood parachute inventory assonance trickster encounter
             underwear miscreant touchdown obsession avalanche diagnosis gladiator cafeteria appetizer terrorist
             telescope hypocrite biography telephone messenger insurance adversary perdition surrender pneumonia
             badminton armadillo duplicate variation infection wolverine gibberish adulation
             chlamydia hollywood volunteer bucharest checklist economics synthesis reticence spaceship evergreen
             container frequency excrement ballerina moonlight
             dashboard slaughter aspersion aeroplane draftsman aftermath
        '''.split()

        num = str(random.randint(10000,99999))

        randomize = Randomizer(adj, noun)

        return randomize.random_insert() + num


class Randomizer():
    def __init__(self, adjec, nouns):
        self.adjec = adjec
        self.nouns = nouns

        # A random adjective and noun pulled from list
        adjective = random.choice(adjec)
        noun = random.choice(nouns)

        # A random letter selected from the adjective and noun that was picked
        to_cap_adj = random.randint(0, len(adjective) - 1)
        to_cap_noun = random.randint(0, len(noun) - 1)

        self.adjective = adjective[:to_cap_adj] + adjective[to_cap_adj:].capitalize()
        self.noun = noun[:to_cap_noun] + noun[to_cap_noun:].capitalize()

    ## Insert a 'random_symbol' into adjective and noun##
    def random_insert(self):
        # A list of random symbols to be selected from
        random_symbols = list('!@#$%^&*?')

        self.adjective = list(self.adjective)
        self.noun = list(self.noun)

        for position,letter in enumerate(self.adjective):
            if letter == 'a':
                self.adjective[position] = random_symbols[random_symbols.index('@')]
                break
            if letter == 's':
                self.adjective[position] = random_symbols[random_symbols.index('$')]
                break
            if letter == 'i':
                self.adjective[position] = random_symbols[random_symbols.index('!')]
                break

        for position, letter in enumerate(self.noun):
            if letter == 'a':
                self.noun[position] = random_symbols[random_symbols.index('@')]
                break
            if letter == 's':
                self.noun[position] = random_symbols[random_symbols.index('$')]
                break
            if letter == 'i':
                self.noun[position] = random_symbols[random_symbols.index('!')]
                break

        # A random letter selected from the adjective and noun that was picked
        to_rand_adj = random.randint(0, len(self.adjective) - 1)
        to_rand_noun = random.randint(0, len(self.noun) - 1)

        # Reassigning the selected letter to a symbol from 'random symbol'
        #self.adjective[to_rand_adj] = (random.choice(random_symbols))
        #self.noun[to_rand_noun] = (random.choice(random_symbols))

        adjective = self.adjective[:to_rand_adj] + self.adjective[to_rand_adj:]
        noun = self.noun[:to_rand_noun] + self.noun[to_rand_noun:]
        adjective = ''.join(adjective)
        noun = ''.join(noun)

        return adjective + noun

while True:
    print(generator())
