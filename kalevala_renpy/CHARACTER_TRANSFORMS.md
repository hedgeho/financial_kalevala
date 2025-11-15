# 🎭 Character Transform Reference

This document explains how character positioning and sizing works in the game.

## 🎯 Transform System Overview

The game uses **custom transforms** defined in `characters.rpy` to ensure character sprites display at reasonable, consistent sizes regardless of the source image dimensions.

### Why This Matters

Without transforms:
- ❌ A 2000px tall image would fill the entire screen
- ❌ A 200px tall image would be tiny and hard to see
- ❌ Different image sizes would look inconsistent
- ❌ Mobile displays would be unpredictable

With transforms:
- ✅ All characters scale to appropriate screen percentage
- ✅ Consistent sizing across all scenes
- ✅ Automatically adapts to mobile screens
- ✅ Professional, polished look

---

## 📐 Available Transforms

### **Standard Single Character Display**

```renpy
show aino happy at character_left
show ilmarinen thoughtful at character_center
show lemminkainen excited at character_right
```

**Specifications:**
- Height: 540px (50% of 1080p screen)
- Bottom-aligned (standing on "ground")
- Positions: 15% (left), 50% (center), 85% (right) from left edge

**Use when:** Showing 1-2 characters in a scene

**Visual:**
```
┌────────────────────────────────────────┐
│                                        │
│        Character (540px tall)          │
│            ┌────────┐                  │
│            │        │                  │
│            │  Aino  │                  │
│            │        │                  │
│            └────────┘                  │
└────────────────────────────────────────┘
         Bottom-aligned at 15%
```

---

### **Group Scene (3 Characters)**

```renpy
show aino happy at character_small_left
show ilmarinen thoughtful at character_small_center
show lemminkainen excited at character_small_right
```

**Specifications:**
- Height: 450px (slightly smaller to fit all)
- Bottom-aligned
- Positions: 10% (left), 50% (center), 90% (right)

**Use when:** Showing all 3 companions simultaneously

**Visual:**
```
┌────────────────────────────────────────┐
│                                        │
│  ┌───┐        ┌───┐       ┌───┐       │
│  │ A │        │ I │       │ L │       │
│  │ i │        │ l │       │ e │       │
│  │ n │        │ m │       │ m │       │
│  │ o │        │ a │       │ m │       │
│  └───┘        └───┘       └───┘       │
└────────────────────────────────────────┘
   10%          50%          90%
 (450px)      (450px)      (450px)
```

---

### **Emphasized/Dramatic Display**

```renpy
show merchant neutral at character_emphasized
```

**Specifications:**
- Height: 720px (larger for dramatic effect)
- Bottom-aligned
- Center positioned (50%)

**Use when:** Dramatic moments, important reveals, villain emphasis

**Visual:**
```
┌────────────────────────────────────────┐
│     Large Character (720px tall)       │
│        ┌──────────────┐                │
│        │              │                │
│        │   Merchant   │                │
│        │   (ANGRY!)   │                │
│        │              │                │
│        │              │                │
│        └──────────────┘                │
└────────────────────────────────────────┘
            Centered, larger
```

---

## 🔧 How It Works (Technical)

### Transform Definition (in characters.rpy)

```renpy
transform character_standard:
    fit "contain"        # Scale to fit, maintain aspect ratio
    ysize 540           # Maximum height in pixels
    yalign 1.0          # Bottom-align (0.0=top, 1.0=bottom)

transform character_left:
    character_standard  # Inherit size settings
    xalign 0.15         # Horizontal position (0.0=left edge, 1.0=right edge)
```

### Usage in Script (in script.rpy)

```renpy
# Show character with transform
show aino happy at character_left with dissolve

# Character speaks
aino "Silver saved today is warmth earned tomorrow. 🍃"

# Hide character
hide aino with dissolve
```

---

## 📱 Mobile Responsiveness

The transforms are **automatically responsive**:

- **Desktop (1920x1080):** 540px = 50% of screen height ✅
- **Tablet (1024x768):** Auto-scales to ~50% of 768px ✅
- **Mobile (375x667):** Auto-scales to ~50% of 667px ✅

Ren'Py handles the math - you just use the transform names!

---

## 🎨 For Artists: Size Recommendations

| Source Image Size | Result | Notes |
|-------------------|--------|-------|
| 400px tall | Upscaled to 540px | May look pixelated |
| 600px tall | Downscaled to 540px | ✅ Good balance |
| 800px tall | Downscaled to 540px | ✅ Sharp on retina displays |
| 1200px tall | Downscaled to 540px | Overkill, larger file size |

**Recommendation:** Create sprites at **700-800px tall**
- Sharp on high-DPI screens
- Reasonable file size
- Good for future-proofing

---

## 🔀 Scene Layout Examples

### Example 1: Companion Debate (used in belt scenario)

```renpy
show aino worried at character_small_left
show ilmarinen thoughtful at character_small_center
show lemminkainen excited at character_small_right

aino "That's almost all our silver... 😟"
ilmarinen "I could inspect it first. 🔬"
lemminkainen "We can't wait! This is NOW OR NEVER! ⚡"
```

Result: All 3 companions visible, each with distinct position and expression.

---

### Example 2: Dramatic Merchant Moment

```renpy
show merchant neutral at character_center
merchant "This belt is blessed by the Sampo!"

# Merchant gets louder and more aggressive
show merchant neutral at character_emphasized
merchant "{size=+10}ONLY 3 BELTS REMAIN!{/size}"
```

Result: Merchant gets larger to emphasize urgency and manipulation.

---

### Example 3: One-on-One Dialogue

```renpy
show ilmarinen approving at character_center

ilmarinen "You trusted wisdom over impulse. Rare. 💎"
ilmarinen "Here - take this. 🎁"
```

Result: Single character centered, plenty of screen space for dialogue.

---

## 🛠️ Customizing Transforms

Want different sizes or positions? Edit `characters.rpy`:

```renpy
# Make characters even larger
transform my_custom_size:
    fit "contain"
    ysize 650  # Bigger than standard
    yalign 1.0

# Position further left
transform my_custom_left:
    character_standard
    xalign 0.05  # Very far left
```

Then use in script:
```renpy
show aino happy at my_custom_size
```

---

## ✅ Best Practices

**DO:**
- ✅ Use `character_left/center/right` for 1-2 character scenes
- ✅ Use `character_small_*` variants when showing all 3
- ✅ Use `character_emphasized` for dramatic moments
- ✅ Keep characters bottom-aligned for consistency

**DON'T:**
- ❌ Mix standard and small transforms in same scene (looks inconsistent)
- ❌ Put multiple characters at same position (they'll overlap)
- ❌ Use emphasized transform for every scene (loses impact)
- ❌ Manually specify pixel positions (breaks mobile responsiveness)

---

## 🎬 Animation Examples (Future Enhancement)

Transforms can also do animations:

```renpy
# Character enters from off-screen
show aino happy at character_left with moveinleft

# Character slides to center
show aino happy at character_center with move

# Character bounces for emphasis
show lemminkainen excited at character_right:
    yoffset 0
    linear 0.2 yoffset -20
    linear 0.2 yoffset 0
```

These are optional but can add polish!

---

## 📊 Transform Quick Reference

| Transform Name | Height | Position | Use Case |
|----------------|--------|----------|----------|
| `character_left` | 540px | 15% | Single character, left |
| `character_center` | 540px | 50% | Single character, center |
| `character_right` | 540px | 85% | Single character, right |
| `character_small_left` | 450px | 10% | Group scene, left |
| `character_small_center` | 450px | 50% | Group scene, center |
| `character_small_right` | 450px | 90% | Group scene, right |
| `character_emphasized` | 720px | 50% | Dramatic moment |

---

**Summary:** Use these transforms consistently and your characters will always look professional and appropriately sized, regardless of screen size or source image dimensions! 🎭✨
