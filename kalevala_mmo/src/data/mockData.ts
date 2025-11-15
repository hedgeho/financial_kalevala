import { Region, Achievement, UserStats } from '../types';

export const regions: Region[] = [
  { id: 'Uusimaa', name: 'Uusimaa', points: 15420, achievements: 28, totalAchievements: 40, rank: 1, population: 1734000 },
  { id: 'Pirkanmaa', name: 'Pirkanmaa', points: 14850, achievements: 26, totalAchievements: 40, rank: 2, population: 534000 },
  { id: 'Varsinais-Suomi', name: 'Varsinais-Suomi', points: 13920, achievements: 25, totalAchievements: 40, rank: 3, population: 486000 },
  { id: 'Pohjois-Pohjanmaa', name: 'Pohjois-Pohjanmaa', points: 12340, achievements: 23, totalAchievements: 40, rank: 4, population: 420000 },
  { id: 'Keski-Suomi', name: 'Keski-Suomi', points: 11200, achievements: 21, totalAchievements: 40, rank: 5, population: 280000 },
  { id: 'Pohjois-Savo', name: 'Pohjois-Savo', points: 10890, achievements: 20, totalAchievements: 40, rank: 6, population: 248000 },
  { id: 'Päijät-Häme', name: 'Päijät-Häme', points: 10120, achievements: 19, totalAchievements: 40, rank: 7, population: 202000 },
  { id: 'Satakunta', name: 'Satakunta', points: 9850, achievements: 18, totalAchievements: 40, rank: 8, population: 220000 },
  { id: 'Lappi', name: 'Lappi', points: 9340, achievements: 17, totalAchievements: 40, rank: 9, population: 177000 },
  { id: 'Kymenlaakso', name: 'Kymenlaakso', points: 8920, achievements: 16, totalAchievements: 40, rank: 10, population: 174000 },
  { id: 'Etelä-Pohjanmaa', name: 'Etelä-Pohjanmaa', points: 8650, achievements: 15, totalAchievements: 40, rank: 11, population: 193000 },
  { id: 'Pohjanmaa', name: 'Pohjanmaa', points: 8420, achievements: 15, totalAchievements: 40, rank: 12, population: 179000 },
  { id: 'Kanta-Häme', name: 'Kanta-Häme', points: 8100, achievements: 14, totalAchievements: 40, rank: 13, population: 176000 },
  { id: 'Etelä-Savo', name: 'Etelä-Savo', points: 7890, achievements: 14, totalAchievements: 40, rank: 14, population: 153000 },
  { id: 'Etelä-Karjala', name: 'Etelä-Karjala', points: 7450, achievements: 13, totalAchievements: 40, rank: 15, population: 133000 },
  { id: 'Keski-Pohjanmaa', name: 'Keski-Pohjanmaa', points: 6980, achievements: 12, totalAchievements: 40, rank: 16, population: 69000 },
  { id: 'Pohjois-Karjala', name: 'Pohjois-Karjala', points: 6720, achievements: 12, totalAchievements: 40, rank: 17, population: 165000 },
  { id: 'Kainuu', name: 'Kainuu', points: 5890, achievements: 11, totalAchievements: 40, rank: 18, population: 76000 },
  { id: 'Ahvenanmaa', name: 'Ahvenanmaa', points: 4250, achievements: 9, totalAchievements: 40, rank: 19, population: 30000 },
];

export const achievements: Achievement[] = [
  { id: '1', name: 'Clear-Sighted Hero', description: 'Resisted FOMO and investigated before purchasing', icon: '👁️', unlocked: true },
  { id: '2', name: 'Ilmarinen\'s Wisdom', description: 'Used analytical thinking to verify claims', icon: '🔨', unlocked: true },
  { id: '3', name: 'Aino\'s Patience', description: 'Walked away from pressure tactics', icon: '🌾', unlocked: true },
  { id: '4', name: 'Sampo\'s Fortune', description: 'Master impulse control in 10 scenarios', icon: '✨', unlocked: false },
  { id: '5', name: 'Pohjola\'s Champion', description: 'Complete all financial quests with wisdom', icon: '🔱', unlocked: false },
];

const uusimaRegion = regions.find(r => r.id === 'Uusimaa') || regions[0];

export const userStats: UserStats = {
  region: uusimaRegion,
  recentActivity: [
    'Completed: "The Shimmering Belt" - Followed Ilmarinen\'s advice',
    'Earned: Clear-Sighted Hero achievement',
    'Contributed 320 points to Uusimaa',
    'New quest: "Pohjola\'s Market - The Winter Supplies"'
  ],
  weeklyProgress: 85
};
