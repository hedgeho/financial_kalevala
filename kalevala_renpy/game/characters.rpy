## Character Definitions for Kalevala Financial Wisdom

# Narrator
define narrator = Character(None, what_color="#96d9ff", what_italic=True)

# Player character
define player = Character("You", color="#ffffff")

# Three Companions - Each with distinct personality colors
define aino = Character("Aino the Careful", color="#5dadec", image="aino")
define ilmarinen = Character("Ilmarinen the Forgemind", color="#f5a442", image="ilmarinen")
define lemminkainen = Character("Lemminkäinen the Bold", color="#ff6b6b", image="lemminkainen")

# NPCs
define merchant = Character("Merchant", color="#f5d742", image="merchant")
define friendly_merchant = Character("Friendly Merchant", color="#7bed9f")
define bard = Character("Bard", color="#dda0dd")

# Character Image Definitions
# Format: layeredimage <character_name>
# This allows dynamic expression changes

# AINO - Cautious, Thoughtful
image aino neutral:
    "images/characters/aino.png"
image aino worried:
    "images/characters/aino_worried.png"
image aino happy:
    "images/characters/aino_happy.png"
image aino proud:
    "images/characters/aino_happy.png"
image aino sad:
    "images/characters/aino_worried.png"

# ILMARINEN - Analytical, Calm
image ilmarinen neutral:
    "images/characters/ilmarinen.png"
image ilmarinen skeptical:
    "images/characters/ilmarinen_thoughtful.png"
image ilmarinen approving:
    "images/characters/ilmarinen_approving.png"
image ilmarinen thoughtful:
    "images/characters/ilmarinen_thoughtful.png"

# LEMMINKÄINEN - Bold, Impulsive
image lemminkainen neutral:
    "images/characters/lemminkainen.png"
image lemminkainen excited:
    "images/characters/lemminkainen_excited.png"
image lemminkainen shocked:
    "images/characters/lemminkainen_shocked.png"
image lemminkainen embarrassed:
    "images/characters/lemminkainen_embarrassed.png"
image lemminkainen grinning:
    "images/characters/lemminkainen.png"

# MERCHANT
image merchant neutral:
    "images/characters/merchant.png"
image merchant nervous:

    "images/characters/merchant_nervous.png"

# ASCII Art alternatives (used in reflections/special moments)
# These can be simple text overlays
image aino_ascii:
    Text("  (•‿•)\n <|   |>\n  /‾‾‾\\", size=24, color="#5dadec")

image ilmarinen_ascii:
    Text(" [0_0]\n <|─┬─|>\n   / \\", size=24, color="#f5a442")

image lemminkainen_ascii:
    Text("  (⌐■_■)\n  <|  ^)>\n   /🔥\\", size=24, color="#ff6b6b")

# Character Display Transforms
# These ensure characters display at reasonable proportions regardless of source image size

# Standard character size - scales to fit within screen bounds
transform character_standard:
    # Target: Character sprites should be ~40-50% of screen height
    # Assuming 1080p screen, that's ~432-540px tall
    # This will auto-scale larger/smaller images
    fit "contain"
    ysize 540  # Max height in pixels
    yalign 1.0  # Bottom-aligned (standing on ground)

transform character_left:
    character_standard
    xalign 0.15  # Left side positioning

transform character_center:
    character_standard
    xalign 0.5  # Center positioning

transform character_right:
    character_standard
    xalign 0.85  # Right side positioning

# Smaller size for when 3 characters are on screen simultaneously
transform character_small:
    fit "contain"
    ysize 450  # Slightly smaller for group scenes
    yalign 1.0

transform character_small_left:
    character_small
    xalign 0.1

transform character_small_center:
    character_small
    xalign 0.5

transform character_small_right:
    character_small
    xalign 0.9

# Emphasized/close-up version (for dramatic moments)
transform character_emphasized:
    fit "contain"
    ysize 720  # Larger for emphasis
    yalign 1.0
    xalign 0.5
