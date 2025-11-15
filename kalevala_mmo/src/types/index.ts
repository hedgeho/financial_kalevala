export interface Region {
  id: string;
  name: string;
  points: number;
  achievements: number;
  totalAchievements: number;
  rank: number;
  population?: number;
}

export interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  unlocked: boolean;
}

export interface UserStats {
  region: Region;
  recentActivity: string[];
  weeklyProgress: number;
}
