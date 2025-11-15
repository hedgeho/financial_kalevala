# 🔱 Kalevala Financial Quest - Dashboard

An interactive nationwide dashboard for Finland's financial literacy solution, where young heroes journey through Pohjola's markets learning financial wisdom alongside three companions: **Aino the Cautious**, **Ilmarinen the Analytical**, and **Lemminkäinen the Bold**.

## 🎭 The Story

Students across Finland embark on financial quests inspired by the Kalevala epic, facing scenarios like "The Shimmering Belt of Sampo's Light" - where they learn to resist FOMO, analyze marketing tactics, and make wise financial decisions with guidance from their three companions, each representing different financial personalities.

## Features

- **Interactive Finland Map**: Accurate visual representation of all 19 Finnish regions using real GeoJSON boundary data with hover tooltips showing points, rankings, and achievements
- **Home Region Highlighting**: Uusimaa is highlighted as the user's home region with distinctive gold styling
- **Regional Leaderboard**: Complete rankings of all 19 Finnish regions by points and achievements earned
- **User Statistics Panel**: Detailed view of the home region's performance including:
  - Total points and achievements
  - Weekly progress tracking
  - Recent achievements (Kalevala-themed)
  - Activity feed
- **Kalevala-Inspired Theme**: Visual design inspired by Finnish mythology featuring:
  - Deep blue color palette (representing Finnish nature)
  - Gold accents (representing the mystical Sampo)
  - Achievement names based on Kalevala characters (Väinämöinen, Ilmarinen, Lemminkäinen)

## Technology Stack

- **React 18** with TypeScript
- **Vite** for fast development and building
- **React-Leaflet** for interactive mapping
- **Leaflet** for map rendering
- **CSS3** for Kalevala-themed styling

## Getting Started

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Build

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## Project Structure

```
src/
├── components/          # React components
│   ├── FinlandMap.tsx  # Interactive map of Finland
│   ├── Leaderboard.tsx # Regional rankings
│   └── UserStats.tsx   # User region statistics
├── data/               # Mock data
│   ├── mockData.ts     # Regions and achievements data
│   └── finlandGeoJSON.ts # Geographic data for Finland
├── types/              # TypeScript type definitions
│   └── index.ts
├── App.tsx            # Main application component
└── main.tsx           # Application entry point
```

## Data

The application uses:
- **Real GeoJSON Data**: Accurate geographic boundaries for all 19 Finnish regions (Maakunta)
- **Mock Statistics**: Sample points, rankings, and achievements for demonstration
  - All 19 regions: Uusimaa, Pirkanmaa, Varsinais-Suomi, Pohjois-Pohjanmaa, Keski-Suomi, Pohjois-Savo, Päijät-Häme, Satakunta, Lappi, Kymenlaakso, Etelä-Pohjanmaa, Pohjanmaa, Kanta-Häme, Etelä-Savo, Etelä-Karjala, Keski-Pohjanmaa, Pohjois-Karjala, Kainuu, and Ahvenanmaa
- **5 Kalevala-themed achievements** with Finnish names
- **Sample user statistics** and recent activity

## 🎭 The Three Companions

Each student journeys with three companion characters who represent different financial decision-making styles:

### 🌾 Aino the Cautious
- **Trait**: Patient and risk-averse
- **Teaches**: Saving, careful planning, resisting pressure
- **Quote**: "Why so much noise? True value rarely needs shouting."

### 🔨 Ilmarinen the Analytical
- **Trait**: Logical and investigative
- **Teaches**: Research, verification, critical thinking
- **Quote**: "Let me test it. Even shining treasure must withstand the forge of truth."

### ⚔️ Lemminkäinen the Bold
- **Trait**: Adventurous and impulsive
- **Teaches**: Opportunity recognition (but also FOMO risks)
- **Quote**: "Now this is a hero's chance! Don't be left behind!"

## 🏆 Quest-Based Achievements

- **Clear-Sighted Hero**: Resisted FOMO and investigated before purchasing
- **Ilmarinen's Wisdom**: Used analytical thinking to verify claims
- **Aino's Patience**: Walked away from pressure tactics
- **Sampo's Fortune**: Master impulse control across multiple scenarios
- **Pohjola's Champion**: Complete all financial quests with wisdom

### Color Palette
- Primary: Deep blue (#2c4875) - Finnish nature and midnight sun
- Secondary: Gold (#c9a961) - The mystical Sampo
- Accent: Bronze (#8b6f47) - Ancient artifacts
- Dark: Navy (#1a2942) - Northern night sky

## Future Enhancements

- Backend integration for real-time data
- More detailed region statistics
- Collaborative challenges between regions
- Visual novel game integration
- User authentication and profiles
- More Kalevala-themed visual elements
