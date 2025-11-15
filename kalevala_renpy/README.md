# 🔱 The Tales of Kalevala: Financial Wisdom (Ren'Py Version)

A mobile-optimized visual novel teaching financial literacy through Finnish mythology and three unique companion perspectives.

## 📦 What's Included

This is a complete Ren'Py conversion of the terminal-based game with:
- ✅ Full scenario with all three decision paths
- ✅ Character sprite system with expressions
- ✅ Background scene transitions
- ✅ Mobile-optimized UI
- ✅ Companion approval tracking (hidden)
- ✅ Multi-perspective reflection system
- ✅ Stats display and inventory
- ✅ Save/load system (Ren'Py built-in)

## 🚀 Getting Started with Ren'Py

### 1. Install Ren'Py

Download from: https://www.renpy.org/latest.html
- Windows/Mac/Linux supported
- No coding experience required
- Free and open-source

### 2. Set Up This Project

**Option A: Start from scratch**
1. Launch Ren'Py
2. Click "Create New Project"
3. Name it "kalevala_financial_wisdom"
4. Choose a theme (will be customized anyway)
5. Replace the generated `game` folder with this `game` folder

**Option B: Quick setup**
1. Copy the entire `kalevala_renpy` folder to your Ren'Py projects directory
2. Launch Ren'Py
3. The project should appear in your project list

### 3. Add Assets

The game currently has **placeholder references** for all visual assets.

📁 Place your assets in:
```
game/images/
├── characters/       # Character sprites (14 images)
├── backgrounds/      # Scene backgrounds (5 images)
└── ui/              # UI elements (2 images)
```

See `ASSETS.md` for complete specifications and checklist.

**Quick Start (No Assets Yet):**
The game will run without assets - you'll see missing image warnings but can test all functionality.

**Character Sizing:**
The game automatically resizes character portraits to appropriate proportions:
- Standard scenes: 540px tall (fits well on screen)
- Group scenes: 450px tall (when 3 characters are shown)
- Dramatic moments: 720px tall (emphasized close-ups)

Artists can create sprites at any reasonable size (600-800px recommended) and they'll be automatically scaled.

### 4. Run the Game

1. In Ren'Py launcher, select your project
2. Click "Launch Project"
3. Game opens in a window
4. Test all three paths (impulse, investigate, resist)

### 5. Build for Web

1. In Ren'Py launcher, select your project
2. Click "Build Distributions"
3. Check "Web (Beta)" option
4. Click "Build"
5. Output appears in `projectname-dists/projectname-web.zip`

**Deploy to Web:**
- Unzip and upload to any web host
- **Recommended:** Itch.io (free hosting, great for games)
- Works on mobile browsers automatically!

---

## 📂 Project Structure

```
kalevala_renpy/
├── game/
│   ├── script.rpy          # Main game story (belt scenario)
│   ├── characters.rpy      # Character definitions and images
│   ├── variables.rpy       # Game state and functions
│   └── images/             # Asset folder (add your images here)
│       ├── characters/     # Character sprites
│       ├── backgrounds/    # Background art
│       └── ui/            # UI elements
├── ASSETS.md              # Complete asset specifications
└── README.md              # This file
```

---

## 🎮 Game Features

### **Three Unique Companions**
- **Aino the Careful** (Blue) - Cautious, long-term planner
- **Ilmarinen the Forgemind** (Amber) - Analytical, investigative
- **Lemminkäinen the Bold** (Red) - Impulsive, risk-taker

### **Three Decision Paths**
1. **Impulse Buy** - Learn about FOMO and manipulation
2. **Investigate** - Learn about due diligence and verification
3. **Resist** - Learn about social pressure and walking away

### **Educational System**
- Multi-perspective reflections after each path
- Financial wisdom scoring (hidden calculations)
- Titles and achievements
- Companion approval tracking

---

## 🔧 Customization

### **Modify Dialogue**
Edit `game/script.rpy` - all dialogue is clearly labeled by scene and character.

### **Add New Scenarios**
1. Create new labels in `script.rpy` (e.g., `label debt_scenario:`)
2. Use existing companion characters
3. Follow the pattern: setup → choice → path → reflection → ending

### **Change UI Theme**
Ren'Py has built-in theme customization:
1. In launcher, go to "Change/Update GUI"
2. Choose colors, fonts, button styles
3. Preview changes instantly

### **Mobile Optimization**
Already optimized! But you can adjust:
- Text size: Edit `gui.rpy` (auto-generated)
- Button size: Modify `screen.rpy` for touch targets
- Aspect ratio: Set in `options.rpy`

---

## 📱 Mobile Testing

### **Desktop Preview**
Ren'Py can simulate mobile:
1. In game, press `Shift+M` to toggle mobile mode
2. Or resize window to phone dimensions

### **Real Device Testing**
1. Build for Web (see above)
2. Upload to Itch.io or host locally
3. Open on phone browser
4. Test tap interactions, text readability

---

## 🎨 Working Without Assets (Testing Mode)

The game is fully functional without visual assets! You can:
- Test all dialogue paths ✅
- Verify game logic ✅
- Check mobile responsiveness ✅
- Demonstrate to stakeholders ✅

**Missing images show as:**
- Pink placeholder boxes (obvious where art goes)
- Text overlays with image names
- Game continues normally

This lets you develop content before commissioning art.

---

## 📚 Ren'Py Resources

### **Official Documentation**
- https://www.renpy.org/doc/html/ - Complete reference
- https://www.renpy.org/doc/html/quickstart.html - Beginner tutorial

### **Community**
- r/RenPy subreddit - Active community
- Ren'Py Discord - Real-time help
- Lemma Soft Forums - Game dev discussions

### **Tutorials**
- YouTube: "Ren'Py Visual Novel Tutorial" by Zeil Learnings
- Ren'Py Cookbook (built into launcher)

---

## 🔄 Converting to Other Formats

### **To Mobile App (iOS/Android)**
Ren'Py can build native apps:
1. Requires more setup (Android SDK/Xcode)
2. Follow: https://www.renpy.org/doc/html/android.html
3. Result: Standalone app (no browser needed)

### **To Desktop Executable**
1. Build Distributions → PC/Mac/Linux
2. Creates standalone .exe/.app/.sh
3. Distribute on itch.io or own site

### **To Other Visual Novel Engines**
- **Godot Visual Novel Plugin:** Port script structure
- **Ink:** Convert to Ink script format
- **Unity with Yarn Spinner:** Recreate in Unity

---

## ⚙️ Technical Notes

### **Performance**
- Target: 60fps on mobile browsers
- Keep total assets <50MB for web
- Use WebP format for smaller files (Ren'Py 8.1+)

### **Browser Compatibility**
- Chrome/Edge: ✅ Full support
- Safari: ✅ Full support (iOS 13+)
- Firefox: ✅ Full support
- Avoid IE11 (not supported)

### **Save System**
- Automatic (Ren'Py built-in)
- Saves to browser localStorage (web)
- Players can save/load anytime
- No extra coding needed!

---

## 🎯 Next Steps

1. **Test the Game** - Run it, try all paths, verify logic
2. **Commission/Create Assets** - Use ASSETS.md as reference
3. **Add Assets** - Drop into `game/images/` folders
4. **Iterate** - Adjust dialogue, test on mobile
5. **Deploy** - Build for web, upload to Itch.io
6. **Expand** - Add more scenarios (debt, investment, etc.)

---

## 📄 License Notes

- Ren'Py: LGPL, free for commercial use
- Your game content: Your license choice
- Assets: Depends on source (commission/royalty-free)

---

## 🆘 Troubleshooting

**"Missing image" errors:**
- Normal if you haven't added assets yet
- Game still works, shows placeholder boxes
- Check file names match exactly (case-sensitive!)

**"Script error" messages:**
- Read error carefully - shows line number
- Common: Indentation issues (Ren'Py uses Python-like syntax)
- Fix in text editor, reload game (Shift+R)

**Mobile not responsive:**
- Check if you enabled web build mode
- Test with actual device, not just emulator
- Adjust GUI settings in `gui.rpy`

**Game runs slowly:**
- Reduce image file sizes
- Use .webp instead of .png (smaller)
- Disable unnecessary effects

---

## 🤝 Contributing

Found bugs or want to improve the game?
1. Test thoroughly
2. Document issues clearly
3. Suggest improvements with context

---

**Ready to create your financial literacy visual novel?**
**Start by running the game, then add assets, then deploy!** 🎮✨

**Questions?** Check Ren'Py docs or community forums.
