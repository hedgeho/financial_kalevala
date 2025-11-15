# 🎨 Asset Specification for Kalevala Financial Wisdom

This document outlines all visual assets needed for the Ren'Py version of the game.

## 📐 General Guidelines

**Mobile Optimization:**
- Recommended canvas: 1920x1080 (16:9 ratio)
- Character sprites: 500-800px tall
- Backgrounds: 1920x1080
- UI elements: Vector or high-res for scaling

**Art Style Recommendations:**
1. **Pixel Art** - Nostalgic, fast to produce, scales well
2. **Chibi/Simple Vector** - Clean, modern, mobile-friendly
3. **Semi-Realistic** - Most polished, requires skilled artist

**File Format:**
- PNG with transparency for characters and UI
- JPG for backgrounds
- Keep file sizes reasonable for web deployment (<500KB per asset)

---

## 👥 CHARACTER SPRITES

All character sprites should have transparent backgrounds and be drawn facing forward or at a 3/4 angle.

### **Aino the Careful** 💙
**Personality:** Cautious, thoughtful, gentle
**Color Palette:** Blues, silvers, soft whites
**Key Features:**
- Soft blue shawl like ripples of a lake
- Silver birch-leaf brooch
- Gentle, calm expression
- Small leather coin pouch visible
- Reed notebook in hand (optional)

**Required Expressions:**
- `aino_neutral.png` - Calm, observant
- `aino_worried.png` - Concerned, anxious (furrowed brow)
- `aino_happy.png` - Gentle smile, eyes softened
- `aino_proud.png` - Quiet satisfaction, upright posture
- `aino_sad.png` - Disappointed but understanding

**Sprite Dimensions:** ~600-800px tall (will be auto-scaled to 540px in-game)

---

### **Ilmarinen the Forgemind** 🔨
**Personality:** Analytical, calm, methodical
**Color Palette:** Ambers, dark grays, copper tones
**Key Features:**
- Dark forge apron with glowing rune patterns
- Copper spectacles (essential!)
- Hammer slung across back
- Amber ember-light in eyes (subtle glow)
- Steady, thoughtful stance

**Required Expressions:**
- `ilmarinen_neutral.png` - Calm, analytical gaze
- `ilmarinen_skeptical.png` - Raised eyebrow, arms crossed
- `ilmarinen_approving.png` - Slight nod, warm expression
- `ilmarinen_thoughtful.png` - Hand on chin, adjusting spectacles

**Sprite Dimensions:** ~600-800px tall (will be auto-scaled to 540px in-game)

---

### **Lemminkäinen the Bold** 🔥
**Personality:** Impulsive, energetic, charismatic
**Color Palette:** Reds, oranges, gold accents
**Key Features:**
- Fiery red cloak flowing like a fox's tail
- Hair tied back with feather charm
- Mischievous/confident expression
- Belt full of trinkets (some junk, some treasure)
- Dynamic, restless pose

**Required Expressions:**
- `lemminkainen_neutral.png` - Confident smirk
- `lemminkainen_excited.png` - Eyes wide, energetic pose
- `lemminkainen_shocked.png` - Mouth open, surprised
- `lemminkainen_embarrassed.png` - Sheepish, hand behind head
- `lemminkainen_grinning.png` - Big mischievous grin

**Sprite Dimensions:** ~600-800px tall (will be auto-scaled to 540px in-game)

---

### **Merchant** 🎪
**Personality:** Theatrical, manipulative, nervous when caught
**Key Features:**
- Colorful but slightly sleazy appearance
- Exaggerated gestures
- Louhi's messenger insignia (optional)

**Required Expressions:**
- `merchant_neutral.png` - Theatrical, arms wide
- `merchant_nervous.png` - Sweating, forced smile

**Sprite Dimensions:** ~600-800px tall (will be auto-scaled to 540px in-game)

---

## 📏 Character Sizing System

**Automatic Scaling:** The game automatically resizes character sprites to appropriate proportions:
- **Standard display:** 540px tall (~40-50% of 1080p screen height)
- **Group scenes (3 characters):** 450px tall (slightly smaller to fit all)
- **Emphasized moments:** 720px tall (dramatic close-ups)

**What this means for artists:**
- Create sprites at **600-800px tall** for best quality
- Larger source images = sharper display on high-DPI screens
- The game will automatically scale down for mobile
- No need to worry about exact pixel dimensions
- Transparent backgrounds required (PNG format)

**Positioning:** Characters are bottom-aligned (standing on "ground") and positioned:
- Left character: 15% from left edge
- Center character: 50% (centered)
- Right character: 85% from left edge (15% from right)

---

## 🖼️ BACKGROUND ART

All backgrounds should be 1920x1080 and evoke Finnish/Nordic mythology aesthetic.

### **Required Backgrounds:**

1. **`title_screen.jpg`**
   - Mystical Finnish landscape
   - Kalevala-inspired runes or patterns
   - Space for title text overlay
   - Color: Mystical blues, purples, golds

2. **`market_village.jpg`**
   - Pohjola market village
   - Nordic wooden structures
   - Bustling atmosphere
   - Daytime, sunny
   - Crowd silhouettes (optional)

3. **`merchant_stall.jpg`**
   - Close-up of merchant's stall
   - Central space for belt display
   - Colorful fabrics, market goods
   - Slightly chaotic/theatrical feel

4. **`market_distant.jpg`**
   - View of market from afar
   - More peaceful, less crowded
   - Used for "walking away" scenes
   - Same location as market_village but different angle

5. **`morning_camp.jpg`**
   - Morning scene, soft light
   - Simple camp or inn interior
   - Used for "next morning" reveal
   - Warm but not cheerful

---

## 🎨 UI ELEMENTS

### **Special Item Displays:**

1. **`shimmering_belt.png`**
   - The mystical belt, glowing with golden light
   - Ornate design with magical aura
   - Transparent background
   - Size: ~400x200px
   - Can be animated (glow effect)

2. **`iron_charm.png`**
   - Small anvil-shaped iron charm
   - Simple, genuine craftsmanship
   - No magical glow (contrast with belt)
   - Size: ~200x200px

### **Companion ASCII Art (Optional):**
Simple text-based representations for reflection scenes:
```
Aino:          Ilmarinen:      Lemminkäinen:
  (•‿•)         [◉_◉]            (⌐■_■)
 <|   |>       <|─┬─|>           <|  ^)>
  /‾‾‾\          / \              /🔥\
```
These can be rendered as text or as simple pixel art.

---

## 🎯 UI Customization (Optional)

### **Custom Dialogue Box:**
- Nordic-inspired frame design
- Transparent background with slight tint
- Character name plates with color coding
- Mobile-friendly sizing

### **Choice Buttons:**
- Large, finger-friendly for mobile
- Icon support (🔥, 🔍, 🚶 emojis or icons)
- Visual feedback on hover/tap

### **Stats Display:**
- Compact overlay showing silver/inventory
- Auto-hide after 3 seconds
- Nordic rune border (optional)

---

## 📦 Asset Checklist

### Characters (Total: 14 images)
- [ ] aino_neutral.png
- [ ] aino_worried.png
- [ ] aino_happy.png
- [ ] aino_proud.png
- [ ] aino_sad.png
- [ ] ilmarinen_neutral.png
- [ ] ilmarinen_skeptical.png
- [ ] ilmarinen_approving.png
- [ ] ilmarinen_thoughtful.png
- [ ] lemminkainen_neutral.png
- [ ] lemminkainen_excited.png
- [ ] lemminkainen_shocked.png
- [ ] lemminkainen_embarrassed.png
- [ ] lemminkainen_grinning.png
- [ ] merchant_neutral.png
- [ ] merchant_nervous.png

### Backgrounds (Total: 5 images)
- [ ] title_screen.jpg
- [ ] market_village.jpg
- [ ] merchant_stall.jpg
- [ ] market_distant.jpg
- [ ] morning_camp.jpg

### UI Elements (Total: 2 images)
- [ ] shimmering_belt.png
- [ ] iron_charm.png

**Total Asset Count: 21 images**

---

## 💰 Budget Estimates

### **Commission from Artist:**
- **Pixel Art:** $300-500 (faster, simpler)
- **Chibi Style:** $500-800 (cute, polished)
- **Semi-Realistic:** $800-1500 (most detailed)

### **Asset Packs (Royalty-Free):**
- OpenGameArt.org (free)
- Itch.io asset packs ($10-50)
- Modify existing Nordic/fantasy packs

### **AI-Assisted + Touch-Up:**
- Generate base with Midjourney/DALL-E ($30-80/month)
- Hire artist to refine and ensure consistency ($200-400)
- Fastest path with decent quality

---

## 🔧 Implementation Notes

1. **File Naming:** Must match exactly what's in `characters.rpy` and `script.rpy`
2. **Resolution:** Higher is better (can be scaled down), 2x resolution for retina
3. **Consistency:** Keep art style consistent across all assets
4. **Transparency:** All character sprites MUST have transparent backgrounds
5. **Mobile Testing:** Test on actual mobile devices for readability

---

## 🎨 Style Reference Keywords (for AI or Artist Brief)

**Overall Aesthetic:**
"Finnish mythology, Kalevala-inspired, Nordic folk art, mystical but grounded, educational tone, mobile-friendly character design, semi-realistic or stylized, warm color palette, approachable for teenagers"

**Aino:** "Gentle, calm, blue tones, water imagery, thoughtful expression, modest clothing, leather journal"

**Ilmarinen:** "Blacksmith, analytical, amber/copper tones, spectacles, forge apron with runes, methodical"

**Lemminkäinen:** "Bold warrior, red/fire tones, dynamic pose, confident smirk, adventurous energy, trinket belt"

**Market Scenes:** "Nordic village marketplace, wooden stalls, colorful fabrics, Finnish folk architecture, bustling but not crowded, daytime"

---

## 📱 Mobile Optimization Checklist

- [ ] Character sprites visible on 5" screens
- [ ] Text readable at mobile sizes
- [ ] Tap targets large enough (min 44x44px)
- [ ] Total asset package <50MB for web deployment
- [ ] Backgrounds work in portrait AND landscape
- [ ] Important visual details not lost when scaled down
