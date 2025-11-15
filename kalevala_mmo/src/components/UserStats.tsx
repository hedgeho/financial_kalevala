import { userStats, achievements } from '../data/mockData';
import './UserStats.css';

const UserStats = () => {
  const { region, recentActivity, weeklyProgress } = userStats;

  return (
    <div className="user-stats">
      <div className="stats-header">
        <h2 className="stats-title">🌾 Your Region: {region.name}</h2>
        <div className="current-rank">Rank #{region.rank}</div>
      </div>

      <div className="companions-bar">
        <div className="companion-indicator aino">
          <span className="companion-icon">🌾</span>
          <span className="companion-name">Aino</span>
          <span className="companion-trait">Cautious</span>
        </div>
        <div className="companion-indicator ilmarinen">
          <span className="companion-icon">🔨</span>
          <span className="companion-name">Ilmarinen</span>
          <span className="companion-trait">Analytical</span>
        </div>
        <div className="companion-indicator lemminkainen">
          <span className="companion-icon">⚔️</span>
          <span className="companion-name">Lemminkäinen</span>
          <span className="companion-trait">Risk-Taking</span>
        </div>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-label">💎 Wisdom Points</div>
          <div className="stat-value">{region.points.toLocaleString()}</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">🏅 Quests Complete</div>
          <div className="stat-value">{region.achievements}/{region.totalAchievements}</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">📈 Weekly Journey</div>
          <div className="stat-value">{weeklyProgress}%</div>
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: `${weeklyProgress}%` }}></div>
          </div>
        </div>
      </div>

      <div className="achievements-section">
        <h3 className="section-title">🎭 Your Companion Achievements</h3>
        <div className="companion-note">Wisdom gained through your journey with Aino, Ilmarinen & Lemminkäinen</div>
        <div className="achievements-grid">
          {achievements.map((achievement) => (
            <div
              key={achievement.id}
              className={`achievement-card ${achievement.unlocked ? 'unlocked' : 'locked'}`}
            >
              <div className="achievement-icon">{achievement.icon}</div>
              <div className="achievement-info">
                <div className="achievement-name">{achievement.name}</div>
                <div className="achievement-desc">{achievement.description}</div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="activity-section">
        <h3 className="section-title">📜 Recent Quest Log</h3>
        <div className="activity-list">
          {recentActivity.map((activity, index) => (
            <div key={index} className="activity-item">
              <span className="activity-bullet">•</span>
              {activity}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UserStats;
