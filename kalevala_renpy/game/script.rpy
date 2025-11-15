## The Tales of Kalevala: Financial Wisdom
## Main Story Script

# Background Image Definitions
image bg market = "images/backgrounds/market_village.png"
image bg market_stall = "images/backgrounds/merchant_stall.png"
image bg market_distant = "images/backgrounds/market_village.png"
image bg morning = "images/backgrounds/morning_camp.png"
image bg title = "images/backgrounds/morning_camp.png"
image bg mmo = "images/backgrounds/kalevalaMMO.png"

# UI Element Images
image belt_display = "images/ui/shimmering_belt.png"
image iron_charm = "images/ui/iron_charm.png"

# The game starts here
label start:
    scene bg title with fade
    centered "{b}{size=+20}{color=#ff1493}THE TALES OF KALEVALA{/color}{/size}\n\n{color=#96d9ff}Financial Wisdom{/color}\n\n{size=-5}A Journey Through Ancient Lessons{/size}{/b}"
    pause 2.0

    # Introduction
    scene bg market with fade
    narrator "You are a young hero in the lands of Kalevala."
    narrator "You've been traveling and saving silver carefully."
    narrator "But you don't travel alone..."

    # Introduce companions
    call introduce_companions

    # Show status
    #call screen show_status

    # Start the belt scenario
    jump belt_scenario

# ===== COMPANION INTRODUCTION =====
label introduce_companions:
    scene bg market with fade

    # Aino introduction
    show aino neutral at character_left with dissolve

    aino "Silver saved today is warmth earned tomorrow."

    # Ilmarinen introduction
    hide aino with dissolve
    show ilmarinen neutral at character_center with dissolve

    ilmarinen "Even gold must be tested before trusted."

    # Lemminkäinen introduction
    hide ilmarinen with dissolve
    show lemminkainen neutral at character_right with dissolve

    lemminkainen "Luck won't wait—so why should we?"

    hide lemminkainen with dissolve

    narrator "These three have traveled with you to Pohjola. Each brings their own wisdom and their own view on silver."

    return

# ===== BELT SCENARIO START =====
label belt_scenario:
    scene bg market with fade

    narrator "The sun is high. A crowd has gathered."

    # Show companions reacting (all 3 at once, use smaller transforms)
    show aino neutral at character_small_left with dissolve
    show lemminkainen excited at character_small_right with dissolve
    show ilmarinen skeptical at character_small_center with dissolve

    aino "Look at that crowd."
    lemminkainen "Ooh, excitement! Let's see!"
    ilmarinen "Crowds and drums. Someone's selling."

    hide aino
    hide lemminkainen
    hide ilmarinen
    with dissolve

    narrator "You approach. Louhi's messengers stand before a glowing display."

    scene bg market_stall with fade
    show belt_display at Position(xalign=0.5, yalign=0.3)
    centered "{size=+10}THE SHIMMERING BELT OF SAMPO'S LIGHT{/size}"
    hide belt_display

    narrator "A magnificent belt radiates golden light."
    narrator "The crowd buzzes. Whispers of power spread."

    # Merchant's pitch
    show merchant neutral at character_center with dissolve
    merchant "Step forward, heroes of Kalevala!"

    merchant "This belt carries the blessing of the Sampo itself!"
    merchant "Fortune in battle! Charm in love! Luck in all!"

    show merchant neutral at character_emphasized
    merchant "{size=+10}ONLY 3 BELTS REMAIN!{/size}"
    merchant "{size=+10}Miss it now, miss it FOREVER!{/size}"

    hide merchant with dissolve

    # Companions react
    show lemminkainen excited at character_right with dissolve
    lemminkainen "Only THREE?! Look at it shine!"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "Why sell something so powerful here? And why the urgency?"
    hide aino with dissolve

    show ilmarinen skeptical at character_center with dissolve
    ilmarinen "So much shine, so much pressure. I've forged enough gold to know genuine from glamour."
    hide ilmarinen with dissolve

    # Companions debate
    show lemminkainen excited at character_right with dissolve
    lemminkainen "Come on! Fortune favors the brave! NOW!"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "But that silver is for winter supplies and horse repairs."
    hide aino with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "Perhaps examine it first? Claims and truth are often distant cousins."
    hide ilmarinen with dissolve

    # Merchant's urgency increases
    show merchant neutral at character_center with dissolve
    merchant "{size=+10}TWO BELTS LEFT! TWO!{/size}"
    merchant "{size=+10}Who will seize DESTINY?!{/size}"
    hide merchant with dissolve

    narrator "The crowd surges. The pressure is immense."

    # THE BIG CHOICE
    menu:
        "Buy now - Lemminkäinen is right!":
            jump impulse_path

        "Ask Ilmarinen to inspect it first":
            jump investigate_path

        "Walk away - Aino's caution makes sense":
            jump resist_path

# ===== IMPULSE BUY PATH =====
label impulse_path:
    $ adjust_approval("lemminkainen", 2)
    $ adjust_approval("aino", -2)
    $ adjust_approval("ilmarinen", -1)

    scene bg market_stall with fade

    narrator "Your hand moves to your coin purse."
    narrator "The energy is infectious. The moment pulls you in."

    show lemminkainen excited at character_right with dissolve
    lemminkainen "YES! That's the spirit! Fortune favors the bold!"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "Wait, are you sure? Maybe we should—"
    hide aino with dissolve

    narrator "But the moment has you. You're already counting out silver pieces."

    $ silver -= 120
    $ add_item("Shimmering Belt (enchanted)")
    $ has_belt = True

    centered "{color=#00ff00}You acquired: The Shimmering Belt of Sampo's Light!{/color}"

    #call screen show_status

    narrator "The belt feels warm. It glows brilliantly. The crowd cheers. You feel validated!"

    show lemminkainen grinning at character_right with dissolve
    lemminkainen "THAT'S how a hero acts!"
    hide lemminkainen with dissolve

    show aino sad at character_left with dissolve
    aino "I hope it's worth it."
    hide aino with dissolve

    show ilmarinen skeptical at character_center with dissolve
    ilmarinen "..."
    hide ilmarinen with dissolve

    narrator "You wear it proudly for the rest of the day. But as the sun sets, something changes."

    # Next morning
    scene bg morning with fade
    centered "{size=+10}THE NEXT MORNING{/size}"

    narrator "You wake. You look down at the belt. The golden shimmer is gone."

    narrator "What remains: a plain cloth sash. Tarnished copper thread. Nothing more."

    $ remove_item("Shimmering Belt (enchanted)")
    $ add_item("Faded Cloth Sash (worthless)")
    $ belt_faded = True

    centered "{color=#ff0000}The enchantment has faded completely.{/color}"

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "What?! But it was so... I was so sure."
    hide lemminkainen with dissolve

    show aino sad at character_left with dissolve
    aino "120 silver. Our winter fund. I spoke with others who bought belts. Theirs faded too."
    hide aino with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "The pressure. The urgency. The fear. These are tools of deception. A hard lesson, friend. But better learned now."
    hide ilmarinen with dissolve

    narrator "{i}I felt so rushed. So pressured.{/i}"
    narrator "{i}The excitement felt real... but it was manipulation.{/i}"

    $ add_title("The Hasty Hero")
    $ record_decision("Bought the belt impulsively", "Lost 120 silver to a scam, but learned about FOMO")

    call reflection_impulse
    jump ending

# ===== INVESTIGATE PATH =====
label investigate_path:
    $ adjust_approval("ilmarinen", 2)
    $ adjust_approval("aino", 1)
    $ adjust_approval("lemminkainen", -1)

    scene bg market_stall with fade

    narrator "You raise your hand. The moment pauses."

    player "\"Ilmarinen - inspect this belt first?\""

    narrator "The crowd groans."

    show lemminkainen neutral at character_right with dissolve
    lemminkainen "But there's no TIME! The belts will be GONE!"
    hide lemminkainen with dissolve

    show aino happy at character_left with dissolve
    aino "Yes, let's be certain. Silver saved is better than silver regretted."
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "A wise request. Let's see what truth hides beneath."

    narrator "The smith produces a vial of magic water. One drop falls onto the belt's surface."

    hide ilmarinen with fade
    centered "{size=+10}THE TRUTH REVEALED{/size}"

    narrator "The golden glow flickers, stutters, dims. Beneath: cheap copper wire. Common cloth. The 'ancient magic'? A temporary glamour."

    narrator "The crowd gasps. The merchant's face reddens."

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "It's FAKE?! But it looked so real!"
    hide lemminkainen with dissolve

    show aino happy at character_left with dissolve
    aino "We almost spent everything."
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "Not all gold glitters true. If a deal demands haste, its worth is waste. Well done for asking."
    hide ilmarinen with dissolve

    narrator "The crowd disperses, grumbling. Several demand refunds."

    show merchant nervous at character_center with dissolve
    merchant "The enchantment was symbolic! It's about the experience."
    hide merchant with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "You trusted wisdom over impulse. Rare. Here, take this."

    transform zoom_charm:
        xalign 0.5
        yalign 0.4
        zoom 0.5
    show iron_charm at zoom_charm
    narrator "He hands you an iron charm shaped like an anvil."
    hide iron_charm

    ilmarinen "A genuine charm. Forged by these hands. Won't make you lucky, but will remind you to think clearly when others rush you."
    hide ilmarinen with dissolve

    show aino happy at character_left with dissolve
    aino "You protected our silver and learned something valuable. Good day!"
    hide aino with dissolve

    show lemminkainen neutral at character_right with dissolve
    lemminkainen "Your way worked better. Still boring though!"
    hide lemminkainen with dissolve

    $ add_item("Ilmarinen's Iron Charm (genuine)")
    $ add_title("Clear-Sighted Hero")
    $ record_decision("Asked Ilmarinen to investigate", "Avoided scam, gained genuine charm and smith's respect")

    centered "{color=#00ff00}You received: Ilmarinen's Iron Charm!{/color}"

    #call screen show_status

    call reflection_investigate
    jump ending

# ===== RESIST PATH =====
label resist_path:
    $ adjust_approval("aino", 2)
    $ adjust_approval("ilmarinen", 1)
    $ adjust_approval("lemminkainen", 0)

    scene bg market_stall with fade

    narrator "You take a deep breath. Step back from the crowd."

    player "\"Not today.\""

    narrator "The words are quiet. But firm."

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "WHAT?! But this is your LAST CHANCE!"
    hide lemminkainen with dissolve

    show aino neutral at character_left with dissolve
    aino "You're sure?"
    hide aino with dissolve

    player "\"I'm sure.\""

    show merchant neutral at character_center with dissolve
    merchant "Last chance! ONE BELT LEFT! Only fools wait!"
    hide merchant with dissolve

    narrator "Others in the crowd mutter: Coward. Missed opportunity. I wouldn't hesitate."

    show lemminkainen neutral at character_right with dissolve
    lemminkainen "The crowd thinks you're wrong."
    hide lemminkainen with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "The crowd thought many false things. Walk with confidence."
    hide ilmarinen with dissolve

    narrator "You turn. Walk toward the edge of the market. Your companions follow. Pressure fades."

    scene bg market_distant with fade

    show aino happy at character_left with dissolve
    aino "You kept our silver. Our plan. Well done."
    hide aino with dissolve

    centered "{size=+10}A FEW MINUTES LATER{/size}"

    narrator "From a distance, you watch the stall. The crowd has thinned. Urgency deflated."

    narrator "And then you see it: the merchant pulls out a large chest filled with DOZENS more 'limited' belts."

    $ saw_merchant_chest = True

    centered "{color=#ff0000}The scarcity was manufactured.{/color}\n{color=#ff0000}The urgency was theater.{/color}"

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "DOZENS?! But he said... You were right. I would've bought it."
    hide lemminkainen with dissolve

    show aino happy at character_left with dissolve
    aino "The best purchase? Sometimes it's the one you don't make."
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "You saw through it by stepping back. The hardest choice is often the wisest. Well done."
    hide ilmarinen with dissolve

    narrator "{i}I didn't let the crowd decide.{/i}"
    narrator "{i}My silver stays. My choices remain mine.{/i}"

    $ add_title("The Unshakeable")
    $ record_decision("Walked away despite pressure", "Kept all silver, gained reputation for wisdom")

    #call screen show_status

    # A week later
    scene bg market with fade
    centered "{size=+10}A WEEK LATER{/size}"

    narrator "You return to the market. Merchants nod respectfully."

    friendly_merchant "Ah! The one who doesn't chase fool's gold! Here, a fair discount for you. I respect clear thinking."

    call reflection_resist
    jump ending

# ===== REFLECTIONS =====
label reflection_impulse:
    scene bg morning with fade
    centered "{size=+15}REFLECTION: Lessons from the Journey{/size}"

    narrator "Your three companions gather to share their thoughts."

    # Lemminkäinen reflects
    show lemminkainen embarrassed at character_center with dissolve
    lemminkainen "I almost bought one too. The thrill! The excitement! But now I see that rush was the trap itself."
    hide lemminkainen
    with dissolve

    # Aino reflects
    show aino sad at character_center with dissolve
    aino "That silver was for winter supplies. One moment of excitement equals weeks of lost security. Ask yourself: need this, or just want it now?"
    hide aino
    with dissolve

    # Ilmarinen reflects
    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "The merchant used urgency, scarcity, social proof. Tools to bypass your rational mind. Remember: when someone rushes you, walk slower."
    hide ilmarinen
    with dissolve

    $ financial_wisdom += 1

    centered "{color=#00ff00}{b}Financial Wisdom Gained: +1{/b}{/color}"
    if titles:
        centered "{b}Title Earned: [titles[-1]]{/b}"

    narrator "The three companions exchange glances. Despite different philosophies, they agree you've learned something valuable today."

    return

label reflection_investigate:
    scene bg market with fade
    centered "{size=+15}REFLECTION: Lessons from the Journey{/size}"

    narrator "Your three companions gather to share their thoughts."

    # Ilmarinen reflects
    show ilmarinen approving at character_center with dissolve
    ilmarinen "You asked: 'Is this real?' That skepticism saved you 120 silver, but it taught you something worth even more."
    hide ilmarinen
    with dissolve

    # Aino reflects
    show aino happy at character_center with dissolve
    aino "You took time to verify. You didn't let their urgency become your emergency. That's the wisdom of patience."
    hide aino
    with dissolve

    # Lemminkäinen reflects
    show lemminkainen neutral at character_center with dissolve
    lemminkainen "I was drawn to it too! That shine! But watching you stay calm while others panicked, that takes real courage. The bold choice isn't always loud."
    hide lemminkainen
    with dissolve

    $ financial_wisdom += 2

    centered "{color=#00ff00}{b}Financial Wisdom Gained: +2{/b}{/color}"
    if titles:
        centered "{b}Title Earned: [titles[-1]]{/b}"

    narrator "The three companions exchange glances. Despite different philosophies, they agree you've learned something valuable today."

    return

label reflection_resist:
    scene bg market_distant with fade
    centered "{size=+15}REFLECTION: Lessons from the Journey{/size}"

    narrator "Your three companions gather to share their thoughts."

    # Aino reflects
    show aino proud at character_center with dissolve
    aino "You walked away. You kept your silver, your plan, your peace. The hardest choices bring the greatest strength."
    hide aino
    with dissolve

    # Ilmarinen reflects
    show ilmarinen approving at character_center with dissolve
    ilmarinen "And what happened? The 'limited' belts? Abundant. The urgency? Theater. You saw through it by stepping back."
    hide ilmarinen
    with dissolve

    # Lemminkäinen reflects
    show lemminkainen neutral at character_center with dissolve
    lemminkainen "The crowd mocked you! But you didn't flinch. I've charged into battle with less courage than your 'not today.' That's the boldness of wisdom."
    hide lemminkainen
    with dissolve

    # Wisdom points
    $ financial_wisdom += 3

    centered "{color=#00ff00}{b}Financial Wisdom Gained: +3{/b}{/color}"
    if titles:
        centered "{b}Title Earned: [titles[-1]]{/b}"

    narrator "The three companions exchange glances. Despite different philosophies, they agree you've learned something valuable today."

    return

# ===== ENDING =====
label ending:
    scene bg market with fade

    #call screen show_status

    $ wisdom_level = get_wisdom_level()
    centered "\n{b}Journey Summary:{/b}\n\n{color=#96d9ff}Financial Wisdom Earned: [financial_wisdom]/3{/color}\n{b}Wisdom Level: [wisdom_level]{/b}"

    transform half_size:
        zoom 0.7
    scene bg mmo at half_size with fade

    narrator "You gained [financial_wisdom] point(s) of Financial Wisdom for Uusimaa."

    return

# ===== CUSTOM SCREENS =====
screen show_status():
    frame:
        xalign 0.5
        yalign 0.1
        xpadding 20
        ypadding 10
        background "#000000cc"

        vbox:
            text "{color=#00ff00}Silver: [silver]{/color}" size 20
            if inventory:
                text "{color=#ffff00}Inventory: [inventory]{/color}" size 16
            if titles:
                text "{color=#ff00ff}Titles: [titles]{/color}" size 16

    timer 3.0 action Hide("show_status")
