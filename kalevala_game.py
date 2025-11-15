#!/usr/bin/env python3
import time
import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    AMBER = '\033[38;5;214m'

class Companion:
    def __init__(self, name, philosophy, personality, color, avatar):
        self.name = name
        self.philosophy = philosophy
        self.personality = personality
        self.color = color
        self.avatar = avatar
        self.approval = 0

    def speak(self, text, show_avatar=False):
        if show_avatar:
            print(f"\n{self.color}{self.avatar}{Colors.END}")
        print(f"{self.color}{Colors.BOLD}{self.name}:{Colors.END} {self.color}\"{text}\"{Colors.END}")

    def adjust_approval(self, delta):
        self.approval += delta

    def get_tone(self):
        if self.approval >= 2:
            return "enthusiastic"
        elif self.approval >= 0:
            return "neutral"
        elif self.approval >= -2:
            return "concerned"
        else:
            return "disappointed"

class Player:
    def __init__(self):
        self.silver = 150
        self.inventory = []
        self.titles = []
        self.financial_wisdom = 0
        self.decisions = []

    def add_item(self, item):
        self.inventory.append(item)

    def add_title(self, title):
        self.titles.append(title)

    def make_decision(self, decision, outcome):
        self.decisions.append({"decision": decision, "outcome": outcome})

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause(prompt=""):
    if prompt:
        input(f"\n{Colors.CYAN}[{prompt}]{Colors.END}")
    else:
        input(f"\n{Colors.CYAN}[Press ENTER to continue...]{Colors.END}")

def print_divider():
    print(f"\n{Colors.CYAN}{'═' * 70}{Colors.END}\n")

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{text}{Colors.END}")

def print_narrator(text):
    print(f"\n{Colors.CYAN}{text}{Colors.END}")

def print_thought(text):
    print(f"\n{Colors.BLUE}💭 {text}{Colors.END}")

def show_status(player):
    print(f"\n{Colors.GREEN}Silver: {player.silver} | Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}{Colors.END}")
    if player.titles:
        print(f"{Colors.BOLD}Titles: {', '.join(player.titles)}{Colors.END}")

def get_choice(options):
    print()
    for i, option in enumerate(options, 1):
        print(f"{Colors.BOLD}{i}.{Colors.END} {option}")

    while True:
        try:
            choice = input(f"\n{Colors.BOLD}Your choice: {Colors.END}").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                return choice_num
            else:
                print(f"{Colors.FAIL}Please choose a number between 1 and {len(options)}{Colors.END}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number{Colors.END}")

def show_ascii_art():
    art = f"""{Colors.WARNING}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     ✦ THE SHIMMERING BELT OF SAMPO'S LIGHT ✦           ║
    ║                                                          ║
    ║          ╭─────────────────────────╮                    ║
    ║          │  ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧   │                    ║
    ║          │ ═══════════════════════ │                    ║
    ║          │  ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦   │                    ║
    ║          ╰─────────────────────────╯                    ║
    ║                                                          ║
    ║            "Fortune • Charisma • Luck"                   ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
{Colors.END}"""
    print(art)

def show_intro():
    title = f"""{Colors.BOLD}{Colors.HEADER}
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   🔱  THE TALES OF KALEVALA: FINANCIAL WISDOM  🔱        ║
    ║                                                           ║
    ║          A Journey Through Ancient Lessons                ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    {Colors.END}"""
    print(title)
    time.sleep(1)

def introduce_companions(aino, ilmarinen, lemminkainen):
    print_divider()
    print_header("✨ YOUR TRAVELING COMPANIONS ✨")
    pause()

    print(f"\n{Colors.BLUE}{aino.avatar}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}💙 Aino the Careful{Colors.END}")
    print(f"{Colors.BLUE}Soft blue shawl, silver birch-leaf brooch{Colors.END}")
    pause()

    aino.speak("Silver saved today is warmth earned tomorrow. 🍃")
    pause()

    print(f"\n{Colors.AMBER}{ilmarinen.avatar}{Colors.END}")
    print(f"{Colors.AMBER}{Colors.BOLD}🔨 Ilmarinen the Forgemind{Colors.END}")
    print(f"{Colors.AMBER}Dark forge apron with glowing runes{Colors.END}")
    pause()

    ilmarinen.speak("Even gold must be tested before trusted. ⚒️")
    print(f"{Colors.AMBER}*adjusts spectacles thoughtfully*{Colors.END}")
    pause()

    print(f"\n{Colors.RED}{lemminkainen.avatar}{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}🔥 Lemminkäinen the Bold{Colors.END}")
    print(f"{Colors.RED}Fiery red cloak, belt full of trinkets{Colors.END}")
    pause()

    lemminkainen.speak("Luck won't wait—so why should we? ⚡")
    print(f"{Colors.RED}*grins mischievously*{Colors.END}")
    pause()

    print_narrator("\n🌲 These three have traveled with you to Pohjola.")
    print_narrator("Each brings their own wisdom... and their own view on silver. 💰")
    pause()

def show_multi_perspective_reflection(decision_type, player, aino, ilmarinen, lemminkainen):
    print_divider()
    print_header("🌟 REFLECTION: Lessons from the Journey")
    pause()

    print_narrator("\n💬 Your three companions gather to share their thoughts...")
    pause()

    if decision_type == "impulse":
        print(f"\n{Colors.RED}{lemminkainen.avatar}{Colors.END}")
        lemminkainen.speak("*sheepishly* I almost bought one too.")
        pause()

        lemminkainen.speak("The thrill! The excitement! 🎭")
        lemminkainen.speak("But now I see - that rush was the trap itself.")
        pause()

        print(f"\n{Colors.BLUE}{aino.avatar}{Colors.END}")
        aino.speak("*gently* That silver was for winter supplies. 🌨️")
        pause()

        aino.speak("One moment of excitement = weeks of lost security.")
        aino.speak("Ask yourself: Need this? Or just want it NOW?")
        pause()

        print(f"\n{Colors.AMBER}{ilmarinen.avatar}{Colors.END}")
        ilmarinen.speak("The merchant used urgency. Scarcity. Social proof. 🎪")
        pause()

        ilmarinen.speak("Tools to bypass your rational mind.")
        ilmarinen.speak("Remember: When someone rushes you, walk slower. ⚖️")
        pause()

        print_header("\n💡 WISDOM GAINED")
        pause()

        print(f"\n{Colors.CYAN}🎯 FOMO (Fear of Missing Out) is a weapon")
        print(f"   It creates false urgency that clouds judgment{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}⏱️  Impulse buys rarely deliver lasting value")
        print(f"   The excitement fades, but the cost remains{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}🚩 High-pressure sales = RED FLAG")
        print(f"   Real deals don't need aggressive tactics{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}🔮 Protect your future self")
        print(f"   Every silver spent is a choice about tomorrow{Colors.END}")
        pause()

        player.financial_wisdom += 1

    elif decision_type == "investigate":
        print(f"\n{Colors.AMBER}{ilmarinen.avatar}{Colors.END}")
        ilmarinen.speak("*nods* You asked: 'Is this real?' 🔍")
        pause()

        ilmarinen.speak("That skepticism saved you 120 silver.")
        ilmarinen.speak("But it taught you something worth even more. 💎")
        pause()

        print(f"\n{Colors.BLUE}{aino.avatar}{Colors.END}")
        aino.speak("You took time to verify. ⏳")
        pause()

        aino.speak("You didn't let their urgency become YOUR emergency.")
        aino.speak("That's the wisdom of patience. 🌿")
        pause()

        print(f"\n{Colors.RED}{lemminkainen.avatar}{Colors.END}")
        lemminkainen.speak("I was drawn to it too! That shine! ✨")
        pause()

        lemminkainen.speak("But watching you stay calm while others panicked...")
        lemminkainen.speak("That takes real courage. The bold choice isn't always loud. 🛡️")
        pause()

        print_header("\n💡 WISDOM GAINED")
        pause()

        print(f"\n{Colors.CYAN}🔎 Always verify before major purchases")
        print(f"   Investigation is cheaper than regret{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}🤝 Seek expert opinions")
        print(f"   Others' knowledge saves you from costly mistakes{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}⏰ Scarcity tactics hide poor quality")
        print(f"   Real value doesn't need manufactured urgency{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}🧠 Taking time = strength, not weakness")
        print(f"   Instant decisions are often traps{Colors.END}")
        pause()

        player.financial_wisdom += 2

    else:
        print(f"\n{Colors.BLUE}{aino.avatar}{Colors.END}")
        aino.speak("*proud* You walked away. 🚶")
        pause()

        aino.speak("You kept your silver. Your plan. Your peace.")
        aino.speak("The hardest choices bring the greatest strength. 💪")
        pause()

        print(f"\n{Colors.AMBER}{ilmarinen.avatar}{Colors.END}")
        ilmarinen.speak("And what happened? 🎭")
        pause()

        ilmarinen.speak("The 'limited' belts? Abundant.")
        ilmarinen.speak("The urgency? Theater. You saw through it by stepping back. 👁️")
        pause()

        print(f"\n{Colors.RED}{lemminkainen.avatar}{Colors.END}")
        lemminkainen.speak("*laughs* The crowd mocked you!")
        pause()

        lemminkainen.speak("But you didn't flinch. 🗡️")
        lemminkainen.speak("I've charged into battle with less courage than your 'not today.'")
        lemminkainen.speak("That's the boldness of wisdom. ⚔️")
        pause()

        print_header("\n💡 WISDOM GAINED")
        pause()

        print(f"\n{Colors.CYAN}✋ You don't need to justify NOT buying")
        print(f"   Keeping resources is as valid as spending{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}👥 Social pressure ≠ reason to spend")
        print(f"   Your budget guides you, not peer pressure{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}🎪 Artificial scarcity = manipulation")
        print(f"   Real scarcity doesn't need aggressive selling{Colors.END}")
        pause()

        print(f"\n{Colors.CYAN}🌅 Walking away gives clarity")
        print(f"   Distance reveals what urgency obscures{Colors.END}")
        pause()

        player.financial_wisdom += 3

    print(f"\n{Colors.GREEN}{Colors.BOLD}💎 Financial Wisdom Gained: +{player.financial_wisdom}{Colors.END}")

    if player.titles:
        print(f"{Colors.BOLD}🏆 Title Earned: {player.titles[-1]}{Colors.END}")
    pause()

    print_narrator("\n🤝 The three companions exchange glances.")
    print_narrator("Despite different philosophies, they agree:")
    print_narrator("You've learned something valuable today. ✨")
    pause()

def belt_scenario(player, aino, ilmarinen, lemminkainen):
    show_ascii_art()
    pause()

    print_narrator("🌅 Your group arrives at Pohjola's market village.")
    print_narrator("The sun is high. A crowd has gathered. 🥁")
    pause()

    aino.speak("*tugs sleeve* Look at that crowd. 👀")
    lemminkainen.speak("Ooh, excitement! Let's see! ⚡")
    ilmarinen.speak("*skeptical* Crowds and drums... someone's selling. 🤔")
    pause()

    print_narrator("\n✨ You approach. Louhi's messengers stand before a glowing display...")
    pause()

    print_header("\n✦ THE SHIMMERING BELT OF SAMPO'S LIGHT ✦")
    print_narrator("💫 A magnificent belt radiates golden light.")
    print_narrator("The crowd buzzes. Whispers of power spread. 🌟")
    pause()

    print(f"\n{Colors.WARNING}{Colors.BOLD}MERCHANT: 🎪{Colors.END}")
    print(f"{Colors.WARNING}\"Step forward, heroes of Kalevala!\"")
    pause()

    print(f"\"This belt carries the blessing of the Sampo itself!\"")
    print(f"\"Fortune in battle! Charm in love! Luck in all!\" ✨{Colors.END}")
    pause()

    print(f"{Colors.WARNING}{Colors.BOLD}\"ONLY 3 BELTS REMAIN!\"")
    print(f"\"Miss it now, miss it FOREVER!\" ⏰{Colors.END}")
    pause()

    print_narrator("\n💬 Your companions react:")
    pause()

    lemminkainen.speak("*breathless* Only THREE?! Look at it shine! ✨")
    pause()

    aino.speak("*frowning* Why sell something so powerful here? 🤨")
    aino.speak("And why the urgency? 🚩")
    pause()

    ilmarinen.speak("*crosses arms* So much shine, so much pressure... ⚒️")
    ilmarinen.speak("I've forged enough gold to know genuine from glamour. 👓")
    pause()

    print_narrator("\n🎵 A bard begins singing:")
    print(f"{Colors.CYAN}\"Oh the lucky wearer of the shining belt,")
    print(f"Fortune favors those who dare not melt!\" 🎭{Colors.END}")
    pause()

    lemminkainen.speak("*swept up* YES! Fortune favors the brave! NOW! 🔥")
    pause()

    aino.speak("*worried* But that silver is for winter supplies... 🌨️")
    aino.speak("And horse repairs... 🐴")
    pause()

    ilmarinen.speak("*calmly* Perhaps examine it first? ⚖️")
    ilmarinen.speak("Claims and truth are often distant cousins. 🔍")
    pause()

    print(f"\n{Colors.WARNING}{Colors.BOLD}MERCHANT: \"TWO BELTS LEFT! TWO! ⏰\"")
    print(f"\"Who will seize DESTINY?!\" 🎪{Colors.END}")
    print_narrator("The crowd surges. The pressure is immense. 😰")
    pause()

    show_status(player)
    print_narrator("\n💰 The belt costs 120 silver.")
    print_narrator("That's most of your carefully saved money. 💸")
    pause()

    lemminkainen.speak("ONCE IN A LIFETIME! We can't miss this! ⚡")
    pause()

    aino.speak("That's almost everything we have... 😟")
    aino.speak("Are we certain? 🤔")
    pause()

    ilmarinen.speak("I could inspect it. Test the enchantment. 🔬")
    ilmarinen.speak("See if the magic is real or just surface shine. 👁️")
    pause()

    print_thought("Three voices. Three perspectives. What should I do? 💭")

    choice = get_choice([
        "🔥 Buy now - Lemminkäinen is right!",
        "🔍 Ask Ilmarinen to inspect it first",
        "🚶 Walk away - Aino's caution makes sense"
    ])

    if choice == 1:
        impulse_buy_path(player, aino, ilmarinen, lemminkainen)
    elif choice == 2:
        investigate_path(player, aino, ilmarinen, lemminkainen)
    else:
        resist_path(player, aino, ilmarinen, lemminkainen)

def impulse_buy_path(player, aino, ilmarinen, lemminkainen):
    print_divider()
    lemminkainen.adjust_approval(2)
    aino.adjust_approval(-2)
    ilmarinen.adjust_approval(-1)

    print_narrator("💸 Your hand moves to your coin purse.")
    print_narrator("The energy is infectious. The moment pulls you in.")
    pause()

    lemminkainen.speak("*excited* YES! That's the spirit! 🔥")
    lemminkainen.speak("Fortune favors the bold! ⚡")
    pause()

    aino.speak("*anxiously* Wait, are you sure? 😰")
    aino.speak("Maybe we should—")
    pause()

    print_narrator("But the moment has you.")
    print_narrator("You're already counting out silver pieces... 💰")
    pause()

    player.silver -= 120
    player.add_item("Shimmering Belt (enchanted)")

    print(f"\n{Colors.GREEN}✦ You acquired: The Shimmering Belt of Sampo's Light! ✨{Colors.END}")
    show_status(player)
    pause()

    print_narrator("\n✨ The belt feels warm. It glows brilliantly.")
    print_narrator("🎉 The crowd cheers. You feel validated!")
    pause()

    lemminkainen.speak("*claps your back* THAT'S how a hero acts! 💪")
    pause()

    aino.speak("*quietly* I hope... I hope it's worth it. 😟")
    pause()

    ilmarinen.speak("*says nothing*")
    print(f"{Colors.AMBER}*watches the belt with narrowed eyes* 👁️{Colors.END}")
    pause()

    print_narrator("\n🌞 You wear it proudly for the rest of the day...")
    pause()

    print_narrator("🌅 But as the sun sets, something changes.")
    pause()

    print_header("\n⧗ THE NEXT MORNING ⧗")
    pause()

    print_narrator("☀️ You wake. You look down at the belt.")
    pause()

    print_narrator("😨 The golden shimmer is... gone.")
    pause()

    print_narrator("What remains: a plain cloth sash.")
    print_narrator("Tarnished copper thread. Nothing more. 💔")
    pause()

    player.inventory.remove("Shimmering Belt (enchanted)")
    player.add_item("Faded Cloth Sash (worthless)")

    print(f"\n{Colors.FAIL}💨 The enchantment has faded completely.{Colors.END}")
    pause()

    lemminkainen.speak("*shocked* What?! But it was so... 😱")
    lemminkainen.speak("I was so sure...")
    pause()

    aino.speak("*sadly* 120 silver. Our winter fund. 🌨️")
    pause()

    aino.speak("I spoke with others who bought belts.")
    aino.speak("Theirs faded too. 💔")
    pause()

    ilmarinen.speak("*gently* The pressure. The urgency. The fear. 🎪")
    pause()

    ilmarinen.speak("These are tools of deception. ⚠️")
    ilmarinen.speak("A hard lesson, friend. But better learned now. 📚")
    pause()

    print_thought("I felt so rushed. So pressured. 😰")
    print_thought("The excitement felt real... but it was manipulation. 🎭")
    pause()

    player.add_title("The Hasty Hero")
    player.make_decision("Bought the belt impulsively", "Lost 120 silver to a scam, but learned about FOMO")

    show_multi_perspective_reflection("impulse", player, aino, ilmarinen, lemminkainen)

def investigate_path(player, aino, ilmarinen, lemminkainen):
    print_divider()
    ilmarinen.adjust_approval(2)
    aino.adjust_approval(1)
    lemminkainen.adjust_approval(-1)

    print_narrator("✋ You raise your hand. The moment pauses.")
    pause()

    print(f"\n{Colors.BOLD}You: 💬{Colors.END} \"Ilmarinen - inspect this belt first?\"")
    pause()

    print_narrator("😤 The crowd groans.")
    pause()

    lemminkainen.speak("*frustrated* But there's no TIME! ⏰")
    lemminkainen.speak("The belts will be GONE! 😠")
    pause()

    aino.speak("*relieved* Yes... let's be certain. 🙏")
    aino.speak("Silver saved > silver regretted. 💙")
    pause()

    ilmarinen.speak("*nods* A wise request. 👓")
    ilmarinen.speak("Let's see what truth hides beneath. 🔍")
    pause()

    print_narrator("\n⚗️  The smith produces a vial of magic water.")
    pause()

    print_narrator("💧 One drop falls onto the belt's surface...")
    pause()

    print_header("\n✧ THE TRUTH REVEALED ✧")
    pause()

    print_narrator("✨ The golden glow flickers... stutters... dims.")
    pause()

    print_narrator("👁️  Beneath: cheap copper wire. Common cloth.")
    print_narrator("The 'ancient magic'? A temporary glamour. 🎪")
    pause()

    print_narrator("\n😱 The crowd gasps. The merchant's face reddens.")
    pause()

    lemminkainen.speak("*stunned* It's... it's FAKE?! 😳")
    lemminkainen.speak("But it looked so real!")
    pause()

    aino.speak("*exhales* We almost spent everything... 😮‍💨")
    pause()

    ilmarinen.speak("Not all gold glitters true. ⚖️")
    pause()

    ilmarinen.speak("If a deal demands haste, its worth is waste.")
    ilmarinen.speak("*turns to you* Well done for asking. 🔨")
    pause()

    print_narrator("\n👥 The crowd disperses, grumbling.")
    print_narrator("Several demand refunds. 💸")
    pause()

    print(f"\n{Colors.WARNING}{Colors.BOLD}Merchant: 😅{Colors.END}")
    print(f"{Colors.WARNING}\"The enchantment was... symbolic!\"")
    print(f"\"It's about the experience...\"{Colors.END}")
    pause()

    ilmarinen.speak("You trusted wisdom over impulse. Rare. 💎")
    ilmarinen.speak("Here - take this. 🎁")
    pause()

    print_narrator("\n⚒️  He hands you an iron charm shaped like an anvil.")
    pause()

    ilmarinen.speak("A genuine charm. Forged by these hands. ✨")
    pause()

    ilmarinen.speak("Won't make you lucky - but will remind you:")
    ilmarinen.speak("Think clearly when others rush you. 🧠")
    pause()

    aino.speak("*smiling* You protected our silver. 💰")
    aino.speak("And learned something valuable. Good day! ☀️")
    pause()

    lemminkainen.speak("*grudgingly* Your way worked better. 🤷")
    lemminkainen.speak("*grins* Still boring though! 😏")
    pause()

    player.add_item("Ilmarinen's Iron Charm (genuine)")
    player.add_title("Clear-Sighted Hero")
    player.make_decision("Asked Ilmarinen to investigate", "Avoided scam, gained genuine charm and smith's respect")

    print(f"\n{Colors.GREEN}✦ You received: Ilmarinen's Iron Charm! ⚒️{Colors.END}")
    show_status(player)
    pause()

    show_multi_perspective_reflection("investigate", player, aino, ilmarinen, lemminkainen)

def resist_path(player, aino, ilmarinen, lemminkainen):
    print_divider()
    aino.adjust_approval(2)
    ilmarinen.adjust_approval(1)
    lemminkainen.adjust_approval(0)

    print_narrator("🫁 You take a deep breath. Step back from the crowd.")
    pause()

    print(f"\n{Colors.BOLD}You: ✋{Colors.END} \"Not today.\"")
    pause()

    print_narrator("The words are quiet. But firm. 💪")
    pause()

    lemminkainen.speak("*shocked* WHAT?! 😱")
    lemminkainen.speak("But... this is your LAST CHANCE!")
    pause()

    aino.speak("*quietly proud* You're sure? 🤔")
    pause()

    print(f"\n{Colors.BOLD}You: 🗿{Colors.END} \"I'm sure.\"")
    pause()

    print(f"\n{Colors.WARNING}{Colors.BOLD}Merchant: 📢{Colors.END}")
    print(f"{Colors.WARNING}\"Last chance! ONE BELT LEFT!\"")
    print(f"\"Only fools wait!\" ⏰{Colors.END}")
    pause()

    print_narrator("\n👥 Others in the crowd mutter:")
    print(f"{Colors.FAIL}\"Coward...\" 🙄")
    print("\"Missed opportunity...\" 🤦")
    print(f"\"I wouldn't hesitate...\" 💁{Colors.END}")
    pause()

    lemminkainen.speak("*uncomfortable* The crowd thinks you're wrong... 😟")
    pause()

    ilmarinen.speak("*calmly* The crowd thought many false things. ⚖️")
    ilmarinen.speak("Walk with confidence. 🛡️")
    pause()

    print_narrator("\n🚶 You turn. Walk toward the edge of the market.")
    print_narrator("Your companions follow. Pressure fades. 🌬️")
    pause()

    aino.speak("*beside you* You kept our silver. Our plan. 💰")
    aino.speak("Well done. ✨")
    pause()

    print_header("\n⧗ A FEW MINUTES LATER ⧗")
    pause()

    print_narrator("👀 From a distance, you watch the stall.")
    print_narrator("The crowd has thinned. Urgency: deflated. 🎈💨")
    pause()

    print_narrator("And then you see it: 📦")
    pause()

    print_narrator("The merchant pulls out a large chest...")
    print_narrator("Filled with DOZENS more 'limited' belts. 😲")
    pause()

    print(f"\n{Colors.FAIL}🎭 The scarcity was manufactured.")
    print(f"The urgency was theater.{Colors.END}")
    pause()

    lemminkainen.speak("*stunned* DOZENS?! 😳")
    pause()

    lemminkainen.speak("But he said... *long pause*")
    lemminkainen.speak("You were right. I would've bought it. 😔")
    pause()

    aino.speak("*smiling* The best purchase?")
    aino.speak("Sometimes it's the one you don't make. 💙")
    pause()

    ilmarinen.speak("You saw through it by stepping back. 🔍")
    pause()

    ilmarinen.speak("The hardest choice is often the wisest.")
    ilmarinen.speak("*nods* Well done. 🔨")
    pause()

    print_thought("I didn't let the crowd decide. 🗿")
    print_thought("My silver stays. My choices remain mine. ⚖️")
    pause()

    player.add_title("The Unshakeable")
    player.make_decision("Walked away despite pressure", "Kept all silver, gained reputation for wisdom")

    show_status(player)
    pause()

    print_header("\n✦ A WEEK LATER ✦")
    print_narrator("🏪 You return to the market.")
    print_narrator("Merchants nod respectfully. 🙇")
    pause()

    print(f"\n{Colors.GREEN}{Colors.BOLD}Friendly Merchant: 😊{Colors.END}")
    print(f"{Colors.GREEN}\"Ah! The one who doesn't chase fool's gold!\"")
    pause()

    print(f"\"Here - a fair discount for you.\"")
    print(f"\"I respect clear thinking.\" 🤝{Colors.END}")
    pause()

    show_multi_perspective_reflection("resist", player, aino, ilmarinen, lemminkainen)

def show_ending(player, aino, ilmarinen, lemminkainen):
    print_divider()
    print_header("📜 YOUR TALE CONCLUDES (FOR NOW)")
    pause()

    print(f"\n{Colors.BOLD}✨ Journey Summary:{Colors.END}")
    show_status(player)
    pause()

    print(f"\n{Colors.CYAN}💎 Financial Wisdom Earned: {player.financial_wisdom}/3{Colors.END}")

    if player.financial_wisdom >= 3:
        wisdom_level = "Master of Clear Thinking 🏆"
    elif player.financial_wisdom >= 2:
        wisdom_level = "Student of Wisdom 📚"
    else:
        wisdom_level = "Seeker of Understanding 🌱"

    print(f"{Colors.BOLD}Wisdom Level: {wisdom_level}{Colors.END}")
    pause()

    print_narrator("\n🤝 Your three companions gather one final time...")
    pause()

    aino.speak("Silver saved today = warmth tomorrow. 💙")
    aino.speak("You're learning this. 🍃")
    pause()

    ilmarinen.speak("Even gold must be tested before trusted. ⚒️")
    ilmarinen.speak("Remember this always. 🔨")
    pause()

    lemminkainen.speak("*grins* Sometimes the boldest move? 🔥")
    lemminkainen.speak("To stand still. Who knew? 🤷")
    pause()

    print(f"\n{Colors.HEADER}═══════════════════════════════════════════════════════════")
    print("✨ Thank you for playing ✨")
    print("THE TALES OF KALEVALA: FINANCIAL WISDOM")
    print("═══════════════════════════════════════════════════════════{Colors.END}")
    pause()

    print(f"\n{Colors.CYAN}Three perspectives. One truth:")
    print("Wisdom comes from listening to all voices -")
    print(f"including your own. 🔱{Colors.END}\n")
    pause()

def main():
    show_intro()
    pause()

    player = Player()

    aino = Companion(
        "Aino the Careful",
        "Cautious Spender",
        "Thoughtful, long-term planner, risk-averse",
        Colors.BLUE,
        "  (•‿•)\n <|   |>\n  /‾‾‾\\"
    )

    ilmarinen = Companion(
        "Ilmarinen the Forgemind",
        "Balanced Analyst",
        "Rational, methodical, investigative",
        Colors.AMBER,
        " [◉_◉]\n <|─┬─|>\n   / \\"
    )

    lemminkainen = Companion(
        "Lemminkäinen the Bold",
        "Risk-Taker",
        "Impulsive, thrill-seeking, optimistic",
        Colors.RED,
        "  (⌐■_■)\n  <|  ^)>\n   /🔥\\"
    )

    print_narrator("\n🗺️  You are a young hero in the lands of Kalevala.")
    pause()

    print_narrator("💰 You've been traveling and saving silver carefully.")
    pause()

    print_narrator("👥 But you don't travel alone...")
    pause()

    introduce_companions(aino, ilmarinen, lemminkainen)

    print_narrator("\n🌲 Today's journey brings you all to Pohjola's market...")
    pause()

    show_status(player)
    pause()

    input(f"\n{Colors.BOLD}✨ Press ENTER to begin your tale... ✨{Colors.END}")

    belt_scenario(player, aino, ilmarinen, lemminkainen)

    show_ending(player, aino, ilmarinen, lemminkainen)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Tale interrupted. May wisdom guide your path.{Colors.END}\n")
        sys.exit(0)
