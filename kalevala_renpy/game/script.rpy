## The Tales of Kalevala: Financial Wisdom
## Main Story Script

# Background Image Definitions
image bg market = "images/backgrounds/market_village.png"
image bg market_stall = "images/backgrounds/merchant_stall.png"
image bg market_distant = "images/backgrounds/market_village.png"
image bg morning = "images/backgrounds/morning_camp.png"
image bg title = "images/backgrounds/morning_camp.png"

# UI Element Images
image belt_display = "images/ui/shimmering_belt.png"
image iron_charm = "images/ui/iron_charm.png"

# The game starts here
label start:
    scene bg title with fade
    centered "{size=+20}{color=#ff1493}🔱 THE TALES OF KALEVALA{/color}{/size}\n\n{color=#96d9ff}Financial Wisdom{/color}\n\n{size=-5}A Journey Through Ancient Lessons{/size}"
    pause 2.0

    # Introduction
    scene bg market with fade
    narrator "🗺️  You are a young hero in the lands of Kalevala."
    narrator "💰 You've been traveling and saving silver carefully."
    narrator "👥 But you don't travel alone..."

    # Introduce companions
    call introduce_companions

    narrator "\n🌲 Today's journey brings you all to Pohjola's market..."

    # Show status
    #call screen show_status

    "✨ Press to begin your tale... ✨"

    # Start the belt scenario
    jump belt_scenario

# ===== COMPANION INTRODUCTION =====
label introduce_companions:
    scene bg market with fade
    centered "{size=+10}✨ YOUR TRAVELING COMPANIONS ✨{/size}"

    # Aino introduction
    show aino neutral at character_left with dissolve
    show aino_ascii at Position(xalign=0.5, yalign=0.3)
    centered "{color=#5dadec}{size=+5}💙 Aino the Careful{/size}{/color}\n{size=-2}Soft blue shawl, silver birch-leaf brooch{/size}"
    hide aino_ascii

    aino "Silver saved today is warmth earned tomorrow. 🍃"

    # Ilmarinen introduction
    hide aino with dissolve
    show ilmarinen neutral at character_center with dissolve
    show ilmarinen_ascii at Position(xalign=0.5, yalign=0.3)
    centered "{color=#f5a442}{size=+5}🔨 Ilmarinen the Forgemind{/size}{/color}\n{size=-2}Dark forge apron with glowing runes{/size}"
    hide ilmarinen_ascii

    ilmarinen "Even gold must be tested before trusted. ⚒️"
    show ilmarinen thoughtful
    narrator "*adjusts spectacles thoughtfully*"

    # Lemminkäinen introduction
    hide ilmarinen with dissolve
    show lemminkainen neutral at character_right with dissolve
    show lemminkainen_ascii at Position(xalign=0.5, yalign=0.3)
    centered "{color=#ff6b6b}{size=+5}🔥 Lemminkäinen the Bold{/size}{/color}\n{size=-2}Fiery red cloak, belt full of trinkets{/size}"
    hide lemminkainen_ascii

    lemminkainen "Luck won't wait—so why should we? ⚡"
    show lemminkainen grinning
    narrator "*grins mischievously*"

    hide lemminkainen with dissolve

    narrator "\n🌲 These three have traveled with you to Pohjola."
    narrator "Each brings their own wisdom... and their own view on silver. 💰"

    return

# ===== BELT SCENARIO START =====
label belt_scenario:
    scene bg market with fade

    # Display the shimmering belt
    show belt_display at Position(xalign=0.5, yalign=0.3)
    centered "{size=+15}✦ THE SHIMMERING BELT OF SAMPO'S LIGHT ✦{/size}"
    hide belt_display

    narrator "🌅 Your group arrives at Pohjola's market village."
    narrator "The sun is high. A crowd has gathered. 🥁"

    # Show companions reacting (all 3 at once, use smaller transforms)
    show aino neutral at character_small_left with dissolve
    show lemminkainen excited at character_small_right with dissolve
    show ilmarinen skeptical at character_small_center with dissolve

    aino "*tugs sleeve* Look at that crowd. 👀"
    lemminkainen "Ooh, excitement! Let's see! ⚡"
    ilmarinen "*skeptical* Crowds and drums... someone's selling. 🤔"

    hide aino
    hide lemminkainen
    hide ilmarinen
    with dissolve

    narrator "\n✨ You approach. Louhi's messengers stand before a glowing display..."

    scene bg market_stall with fade
    show belt_display at Position(xalign=0.5, yalign=0.3)
    centered "{size=+10}✦ THE SHIMMERING BELT OF SAMPO'S LIGHT ✦{/size}"
    hide belt_display

    narrator "💫 A magnificent belt radiates golden light."
    narrator "The crowd buzzes. Whispers of power spread. 🌟"

    # Merchant's pitch
    show merchant neutral at character_center with dissolve
    merchant "🎪"
    merchant "\"Step forward, heroes of Kalevala!\""

    merchant "\"This belt carries the blessing of the Sampo itself!\""
    merchant "\"Fortune in battle! Charm in love! Luck in all!\" ✨"

    show merchant neutral at character_emphasized
    merchant "{size=+10}\"ONLY 3 BELTS REMAIN!\"{/size}"
    merchant "{size=+10}\"Miss it now, miss it FOREVER!\" ⏰{/size}"

    hide merchant with dissolve

    # Companions react
    narrator "\n💬 Your companions react:"

    show lemminkainen excited at character_right with dissolve
    lemminkainen "*breathless* Only THREE?! Look at it shine! ✨"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "*frowning* Why sell something so powerful here? 🤨"
    aino "And why the urgency? 🚩"
    hide aino with dissolve

    show ilmarinen skeptical at character_center with dissolve
    ilmarinen "*crosses arms* So much shine, so much pressure... ⚒️"
    show ilmarinen thoughtful
    ilmarinen "I've forged enough gold to know genuine from glamour. 👓"
    hide ilmarinen with dissolve

    # Bard singing
    narrator "\n🎵 A bard begins singing:"
    bard "\"Oh the lucky wearer of the shining belt,"
    bard "Fortune favors those who dare not melt!\" 🎭"

    # Companions debate
    show lemminkainen excited at character_right with dissolve
    lemminkainen "*swept up* YES! Fortune favors the brave! NOW! 🔥"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "*worried* But that silver is for winter supplies... 🌨️"
    aino "And horse repairs... 🐴"
    hide aino with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "*calmly* Perhaps examine it first? ⚖️"
    ilmarinen "Claims and truth are often distant cousins. 🔍"
    hide ilmarinen with dissolve

    # Merchant's urgency increases
    show merchant neutral at character_center with dissolve
    merchant "{size=+10}\"TWO BELTS LEFT! TWO! ⏰\"{/size}"
    merchant "{size=+10}\"Who will seize DESTINY?!\" 🎪{/size}"
    hide merchant with dissolve

    narrator "The crowd surges. The pressure is immense. 😰"

    #call screen show_status

    narrator "\n💰 The belt costs 120 silver."
    narrator "That's most of your carefully saved money. 💸"

    # Final companion advice
    show lemminkainen excited at character_right with dissolve
    lemminkainen "ONCE IN A LIFETIME! We can't miss this! ⚡"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "That's almost everything we have... 😟"
    aino "Are we certain? 🤔"
    hide aino with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "I could inspect it. Test the enchantment. 🔬"
    ilmarinen "See if the magic is real or just surface shine. 👁️"
    hide ilmarinen with dissolve

    narrator "{i}💭 Three voices. Three perspectives. What should I do?{/i}"

    # THE BIG CHOICE
    menu:
        "🔥 Buy now - Lemminkäinen is right!":
            jump impulse_path

        "🔍 Ask Ilmarinen to inspect it first":
            jump investigate_path

        "🚶 Walk away - Aino's caution makes sense":
            jump resist_path

# ===== IMPULSE BUY PATH =====
label impulse_path:
    $ adjust_approval("lemminkainen", 2)
    $ adjust_approval("aino", -2)
    $ adjust_approval("ilmarinen", -1)

    scene bg market_stall with fade

    narrator "💸 Your hand moves to your coin purse."
    narrator "The energy is infectious. The moment pulls you in."

    show lemminkainen excited at character_right with dissolve
    lemminkainen "*excited* YES! That's the spirit! 🔥"
    lemminkainen "Fortune favors the bold! ⚡"
    hide lemminkainen with dissolve

    show aino worried at character_left with dissolve
    aino "*anxiously* Wait, are you sure? 😰"
    aino "Maybe we should—"
    hide aino with dissolve

    narrator "But the moment has you."
    narrator "You're already counting out silver pieces... 💰"

    $ silver -= 120
    $ add_item("Shimmering Belt (enchanted)")
    $ has_belt = True

    centered "{color=#00ff00}✦ You acquired: The Shimmering Belt of Sampo's Light! ✨{/color}"

    #call screen show_status

    narrator "\n✨ The belt feels warm. It glows brilliantly."
    narrator "🎉 The crowd cheers. You feel validated!"

    show lemminkainen grinning at character_right with dissolve
    lemminkainen "*claps your back* THAT'S how a hero acts! 💪"
    hide lemminkainen with dissolve

    show aino sad at character_left with dissolve
    aino "*quietly* I hope... I hope it's worth it. 😟"
    hide aino with dissolve

    show ilmarinen skeptical at character_center with dissolve
    ilmarinen "*says nothing*"
    narrator "{color=#f5a442}*watches the belt with narrowed eyes* 👁️{/color}"
    hide ilmarinen with dissolve

    narrator "\n🌞 You wear it proudly for the rest of the day..."

    narrator "🌅 But as the sun sets, something changes."

    # Next morning
    scene bg morning with fade
    centered "{size=+10}⧗ THE NEXT MORNING ⧗{/size}"

    narrator "☀️ You wake. You look down at the belt."

    narrator "😨 The golden shimmer is... gone."

    narrator "What remains: a plain cloth sash."
    narrator "Tarnished copper thread. Nothing more. 💔"

    $ remove_item("Shimmering Belt (enchanted)")
    $ add_item("Faded Cloth Sash (worthless)")
    $ belt_faded = True

    centered "{color=#ff0000}💨 The enchantment has faded completely.{/color}"

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "*shocked* What?! But it was so... 😱"
    lemminkainen "I was so sure..."
    hide lemminkainen with dissolve

    show aino sad at character_left with dissolve
    aino "*sadly* 120 silver. Our winter fund. 🌨️"

    aino "I spoke with others who bought belts."
    aino "Theirs faded too. 💔"
    hide aino with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "*gently* The pressure. The urgency. The fear. 🎪"

    ilmarinen "These are tools of deception. ⚠️"
    ilmarinen "A hard lesson, friend. But better learned now. 📚"
    hide ilmarinen with dissolve

    narrator "{i}💭 I felt so rushed. So pressured. 😰{/i}"
    narrator "{i}💭 The excitement felt real... but it was manipulation. 🎭{/i}"

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

    narrator "✋ You raise your hand. The moment pauses."

    player "💬 \"Ilmarinen - inspect this belt first?\""

    narrator "😤 The crowd groans."

    show lemminkainen neutral at character_right with dissolve
    lemminkainen "*frustrated* But there's no TIME! ⏰"
    lemminkainen "The belts will be GONE! 😠"
    hide lemminkainen with dissolve

    show aino happy at character_left with dissolve
    aino "*relieved* Yes... let's be certain. 🙏"
    aino "Silver saved > silver regretted. 💙"
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "*nods* A wise request. 👓"
    ilmarinen "Let's see what truth hides beneath. 🔍"

    narrator "\n⚗️  The smith produces a vial of magic water."

    narrator "💧 One drop falls onto the belt's surface..."

    hide ilmarinen with fade
    centered "{size=+10}✧ THE TRUTH REVEALED ✧{/size}"

    narrator "✨ The golden glow flickers... stutters... dims."

    narrator "👁️  Beneath: cheap copper wire. Common cloth."
    narrator "The 'ancient magic'? A temporary glamour. 🎪"

    narrator "\n😱 The crowd gasps. The merchant's face reddens."

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "*stunned* It's... it's FAKE?! 😳"
    lemminkainen "But it looked so real!"
    hide lemminkainen with dissolve

    show aino happy at character_left with dissolve
    aino "*exhales* We almost spent everything... 😮‍💨"
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "Not all gold glitters true. ⚖️"

    ilmarinen "If a deal demands haste, its worth is waste."
    ilmarinen "*turns to you* Well done for asking. 🔨"
    hide ilmarinen with dissolve

    narrator "\n👥 The crowd disperses, grumbling."
    narrator "Several demand refunds. 💸"

    show merchant nervous at character_center with dissolve
    merchant "😅"
    merchant "\"The enchantment was... symbolic!\""
    merchant "\"It's about the experience...\""
    hide merchant with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "You trusted wisdom over impulse. Rare. 💎"
    ilmarinen "Here - take this. 🎁"

    show iron_charm at Position(xalign=0.5, yalign=0.4)
    narrator "\n⚒️  He hands you an iron charm shaped like an anvil."
    hide iron_charm

    ilmarinen "A genuine charm. Forged by these hands. ✨"

    ilmarinen "Won't make you lucky - but will remind you:"
    ilmarinen "Think clearly when others rush you. 🧠"
    hide ilmarinen with dissolve

    show aino happy at character_left with dissolve
    aino "*smiling* You protected our silver. 💰"
    aino "And learned something valuable. Good day! ☀️"
    hide aino with dissolve

    show lemminkainen neutral at character_right with dissolve
    lemminkainen "*grudgingly* Your way worked better. 🤷"
    show lemminkainen grinning
    lemminkainen "*grins* Still boring though! 😏"
    hide lemminkainen with dissolve

    $ add_item("Ilmarinen's Iron Charm (genuine)")
    $ add_title("Clear-Sighted Hero")
    $ record_decision("Asked Ilmarinen to investigate", "Avoided scam, gained genuine charm and smith's respect")

    centered "{color=#00ff00}✦ You received: Ilmarinen's Iron Charm! ⚒️{/color}"

    #call screen show_status

    call reflection_investigate
    jump ending

# ===== RESIST PATH =====
label resist_path:
    $ adjust_approval("aino", 2)
    $ adjust_approval("ilmarinen", 1)
    $ adjust_approval("lemminkainen", 0)

    scene bg market_stall with fade

    narrator "🫁 You take a deep breath. Step back from the crowd."

    player "✋ \"Not today.\""

    narrator "The words are quiet. But firm. 💪"

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "*shocked* WHAT?! 😱"
    lemminkainen "But... this is your LAST CHANCE!"
    hide lemminkainen with dissolve

    show aino neutral at character_left with dissolve
    aino "*quietly proud* You're sure? 🤔"
    hide aino with dissolve

    player "🗿 \"I'm sure.\""

    show merchant neutral at character_center with dissolve
    merchant "📢"
    merchant "\"Last chance! ONE BELT LEFT!\""
    merchant "\"Only fools wait!\" ⏰"
    hide merchant with dissolve

    narrator "\n👥 Others in the crowd mutter:"
    narrator "{color=#ff0000}\"Coward...\" 🙄{/color}"
    narrator "{color=#ff0000}\"Missed opportunity...\" 🤦{/color}"
    narrator "{color=#ff0000}\"I wouldn't hesitate...\" 💁{/color}"

    show lemminkainen neutral at character_right with dissolve
    lemminkainen "*uncomfortable* The crowd thinks you're wrong... 😟"
    hide lemminkainen with dissolve

    show ilmarinen thoughtful at character_center with dissolve
    ilmarinen "*calmly* The crowd thought many false things. ⚖️"
    ilmarinen "Walk with confidence. 🛡️"
    hide ilmarinen with dissolve

    narrator "\n🚶 You turn. Walk toward the edge of the market."
    narrator "Your companions follow. Pressure fades. 🌬️"

    scene bg market_distant with fade

    show aino happy at character_left with dissolve
    aino "*beside you* You kept our silver. Our plan. 💰"
    aino "Well done. ✨"
    hide aino with dissolve

    centered "{size=+10}⧗ A FEW MINUTES LATER ⧗{/size}"

    narrator "👀 From a distance, you watch the stall."
    narrator "The crowd has thinned. Urgency: deflated. 🎈💨"

    narrator "And then you see it: 📦"

    narrator "The merchant pulls out a large chest..."
    narrator "Filled with DOZENS more 'limited' belts. 😲"

    $ saw_merchant_chest = True

    centered "{color=#ff0000}🎭 The scarcity was manufactured.{/color}\n{color=#ff0000}The urgency was theater.{/color}"

    show lemminkainen shocked at character_right with dissolve
    lemminkainen "*stunned* DOZENS?! 😳"

    lemminkainen "But he said... *long pause*"
    lemminkainen "You were right. I would've bought it. 😔"
    hide lemminkainen with dissolve

    show aino happy at character_left with dissolve
    aino "*smiling* The best purchase?"
    aino "Sometimes it's the one you don't make. 💙"
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "You saw through it by stepping back. 🔍"

    ilmarinen "The hardest choice is often the wisest."
    ilmarinen "*nods* Well done. 🔨"
    hide ilmarinen with dissolve

    narrator "{i}💭 I didn't let the crowd decide. 🗿{/i}"
    narrator "{i}💭 My silver stays. My choices remain mine. ⚖️{/i}"

    $ add_title("The Unshakeable")
    $ record_decision("Walked away despite pressure", "Kept all silver, gained reputation for wisdom")

    #call screen show_status

    # A week later
    scene bg market with fade
    centered "{size=+10}✦ A WEEK LATER ✦{/size}"

    narrator "🏪 You return to the market."
    narrator "Merchants nod respectfully. 🙇"

    show friendly_merchant at character_center with dissolve
    friendly_merchant "😊"
    friendly_merchant "\"Ah! The one who doesn't chase fool's gold!\""

    friendly_merchant "\"Here - a fair discount for you.\""
    friendly_merchant "\"I respect clear thinking.\" 🤝"
    hide friendly_merchant with dissolve

    call reflection_resist
    jump ending

# ===== REFLECTIONS =====
label reflection_impulse:
    scene bg morning with fade
    centered "{size=+15}🌟 REFLECTION: Lessons from the Journey{/size}"

    narrator "\n💬 Your three companions gather to share their thoughts..."

    # Lemminkäinen reflects
    show lemminkainen embarrassed at character_center with dissolve
    show lemminkainen_ascii at Position(xalign=0.5, yalign=0.2)
    lemminkainen "*sheepishly* I almost bought one too."

    lemminkainen "The thrill! The excitement! 🎭"
    lemminkainen "But now I see - that rush was the trap itself."
    hide lemminkainen
    hide lemminkainen_ascii
    with dissolve

    # Aino reflects
    show aino sad at character_center with dissolve
    show aino_ascii at Position(xalign=0.5, yalign=0.2)
    aino "*gently* That silver was for winter supplies. 🌨️"

    aino "One moment of excitement = weeks of lost security."
    aino "Ask yourself: Need this? Or just want it NOW?"
    hide aino
    hide aino_ascii
    with dissolve

    # Ilmarinen reflects
    show ilmarinen thoughtful at character_center with dissolve
    show ilmarinen_ascii at Position(xalign=0.5, yalign=0.2)
    ilmarinen "The merchant used urgency. Scarcity. Social proof. 🎪"

    ilmarinen "Tools to bypass your rational mind."
    ilmarinen "Remember: When someone rushes you, walk slower. ⚖️"
    hide ilmarinen
    hide ilmarinen_ascii
    with dissolve

    # Wisdom points
    centered "{size=+10}💡 WISDOM GAINED{/size}"

    narrator "{color=#96d9ff}🎯 FOMO (Fear of Missing Out) is a weapon{/color}"
    narrator "{color=#96d9ff}   It creates false urgency that clouds judgment{/color}"

    narrator "\n{color=#96d9ff}⏱️  Impulse buys rarely deliver lasting value{/color}"
    narrator "{color=#96d9ff}   The excitement fades, but the cost remains{/color}"

    narrator "\n{color=#96d9ff}🚩 High-pressure sales = RED FLAG{/color}"
    narrator "{color=#96d9ff}   Real deals don't need aggressive tactics{/color}"

    narrator "\n{color=#96d9ff}🔮 Protect your future self{/color}"
    narrator "{color=#96d9ff}   Every silver spent is a choice about tomorrow{/color}"

    $ financial_wisdom += 1

    centered "{color=#00ff00}{b}💎 Financial Wisdom Gained: +1{/b}{/color}"
    if titles:
        centered "{b}🏆 Title Earned: [titles[-1]]{/b}"

    narrator "\n🤝 The three companions exchange glances."
    narrator "Despite different philosophies, they agree:"
    narrator "You've learned something valuable today. ✨"

    return

label reflection_investigate:
    scene bg market with fade
    centered "{size=+15}🌟 REFLECTION: Lessons from the Journey{/size}"

    narrator "\n💬 Your three companions gather to share their thoughts..."

    # Ilmarinen reflects
    show ilmarinen approving at character_center with dissolve
    show ilmarinen_ascii at Position(xalign=0.5, yalign=0.2)
    ilmarinen "*nods* You asked: 'Is this real?' 🔍"

    ilmarinen "That skepticism saved you 120 silver."
    ilmarinen "But it taught you something worth even more. 💎"
    hide ilmarinen
    hide ilmarinen_ascii
    with dissolve

    # Aino reflects
    show aino happy at character_center with dissolve
    show aino_ascii at Position(xalign=0.5, yalign=0.2)
    aino "You took time to verify. ⏳"

    aino "You didn't let their urgency become YOUR emergency."
    aino "That's the wisdom of patience. 🌿"
    hide aino
    hide aino_ascii
    with dissolve

    # Lemminkäinen reflects
    show lemminkainen neutral at character_center with dissolve
    show lemminkainen_ascii at Position(xalign=0.5, yalign=0.2)
    lemminkainen "I was drawn to it too! That shine! ✨"

    lemminkainen "But watching you stay calm while others panicked..."
    lemminkainen "That takes real courage. The bold choice isn't always loud. 🛡️"
    hide lemminkainen
    hide lemminkainen_ascii
    with dissolve

    # Wisdom points
    centered "{size=+10}💡 WISDOM GAINED{/size}"

    narrator "{color=#96d9ff}🔎 Always verify before major purchases{/color}"
    narrator "{color=#96d9ff}   Investigation is cheaper than regret{/color}"

    narrator "\n{color=#96d9ff}🤝 Seek expert opinions{/color}"
    narrator "{color=#96d9ff}   Others' knowledge saves you from costly mistakes{/color}"

    narrator "\n{color=#96d9ff}⏰ Scarcity tactics hide poor quality{/color}"
    narrator "{color=#96d9ff}   Real value doesn't need manufactured urgency{/color}"

    narrator "\n{color=#96d9ff}🧠 Taking time = strength, not weakness{/color}"
    narrator "{color=#96d9ff}   Instant decisions are often traps{/color}"

    $ financial_wisdom += 2

    centered "{color=#00ff00}{b}💎 Financial Wisdom Gained: +2{/b}{/color}"
    if titles:
        centered "{b}🏆 Title Earned: [titles[-1]]{/b}"

    narrator "\n🤝 The three companions exchange glances."
    narrator "Despite different philosophies, they agree:"
    narrator "You've learned something valuable today. ✨"

    return

label reflection_resist:
    scene bg market_distant with fade
    centered "{size=+15}🌟 REFLECTION: Lessons from the Journey{/size}"

    narrator "\n💬 Your three companions gather to share their thoughts..."

    # Aino reflects
    show aino proud at character_center with dissolve
    show aino_ascii at Position(xalign=0.5, yalign=0.2)
    aino "*proud* You walked away. 🚶"

    aino "You kept your silver. Your plan. Your peace."
    aino "The hardest choices bring the greatest strength. 💪"
    hide aino
    hide aino_ascii
    with dissolve

    # Ilmarinen reflects
    show ilmarinen approving at character_center with dissolve
    show ilmarinen_ascii at Position(xalign=0.5, yalign=0.2)
    ilmarinen "And what happened? 🎭"

    ilmarinen "The 'limited' belts? Abundant."
    ilmarinen "The urgency? Theater. You saw through it by stepping back. 👁️"
    hide ilmarinen
    hide ilmarinen_ascii
    with dissolve

    # Lemminkäinen reflects
    show lemminkainen neutral at character_center with dissolve
    show lemminkainen_ascii at Position(xalign=0.5, yalign=0.2)
    lemminkainen "*laughs* The crowd mocked you!"

    lemminkainen "But you didn't flinch. 🗡️"
    lemminkainen "I've charged into battle with less courage than your 'not today.'"
    lemminkainen "That's the boldness of wisdom. ⚔️"
    hide lemminkainen
    hide lemminkainen_ascii
    with dissolve

    # Wisdom points
    centered "{size=+10}💡 WISDOM GAINED{/size}"

    narrator "{color=#96d9ff}✋ You don't need to justify NOT buying{/color}"
    narrator "{color=#96d9ff}   Keeping resources is as valid as spending{/color}"

    narrator "\n{color=#96d9ff}👥 Social pressure ≠ reason to spend{/color}"
    narrator "{color=#96d9ff}   Your budget guides you, not peer pressure{/color}"

    narrator "\n{color=#96d9ff}🎪 Artificial scarcity = manipulation{/color}"
    narrator "{color=#96d9ff}   Real scarcity doesn't need aggressive selling{/color}"

    narrator "\n{color=#96d9ff}🌅 Walking away gives clarity{/color}"
    narrator "{color=#96d9ff}   Distance reveals what urgency obscures{/color}"

    $ financial_wisdom += 3

    centered "{color=#00ff00}{b}💎 Financial Wisdom Gained: +3{/b}{/color}"
    if titles:
        centered "{b}🏆 Title Earned: [titles[-1]]{/b}"

    narrator "\n🤝 The three companions exchange glances."
    narrator "Despite different philosophies, they agree:"
    narrator "You've learned something valuable today. ✨"

    return

# ===== ENDING =====
label ending:
    scene bg market with fade
    centered "{size=+15}📜 YOUR TALE CONCLUDES (FOR NOW){/size}"

    centered "\n{b}✨ Journey Summary:{/b}"

    #call screen show_status

    $ wisdom_level = get_wisdom_level()
    centered "\n{color=#96d9ff}💎 Financial Wisdom Earned: [financial_wisdom]/3{/color}"
    centered "{b}Wisdom Level: [wisdom_level]{/b}"

    narrator "\n🤝 Your three companions gather one final time..."

    show aino happy at character_left with dissolve
    aino "Silver saved today = warmth tomorrow. 💙"
    aino "You're learning this. 🍃"
    hide aino with dissolve

    show ilmarinen approving at character_center with dissolve
    ilmarinen "Even gold must be tested before trusted. ⚒️"
    ilmarinen "Remember this always. 🔨"
    hide ilmarinen with dissolve

    show lemminkainen grinning at character_right with dissolve
    lemminkainen "*grins* Sometimes the boldest move? 🔥"
    lemminkainen "To stand still. Who knew? 🤷"
    hide lemminkainen with dissolve

    centered "{size=+10}{color=#ff1493}═══════════════════════════════════════════════════════════{/color}{/size}"
    centered "{color=#96d9ff}✨ Thank you for playing ✨{/color}"
    centered "{b}THE TALES OF KALEVALA: FINANCIAL WISDOM{/b}"
    centered "{size=+10}{color=#ff1493}═══════════════════════════════════════════════════════════{/color}{/size}"

    narrator "\n{color=#96d9ff}Three perspectives. One truth:{/color}"
    narrator "{color=#96d9ff}Wisdom comes from listening to all voices -{/color}"
    narrator "{color=#96d9ff}including your own. 🔱{/color}"

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
            text "{color=#00ff00}💰 Silver: [silver]{/color}" size 20
            if inventory:
                text "{color=#ffff00}🎒 Inventory: [inventory]{/color}" size 16
            if titles:
                text "{color=#ff00ff}🏆 Titles: [titles]{/color}" size 16

    timer 3.0 action Hide("show_status")
