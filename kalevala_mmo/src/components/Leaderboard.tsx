import { regions } from '../data/mockData';
import './Leaderboard.css';

const Leaderboard = () => {
  return (
    <div className="leaderboard">
      <h2 className="leaderboard-title">🔱 Regional Quest Progress</h2>
      <div className="leaderboard-subtitle">Heroes across Finland learning financial wisdom</div>
      <div className="leaderboard-list">
        {regions.map((region) => (
          <div
            key={region.id}
            className={`leaderboard-item ${region.id === 'Uusimaa' ? 'home-region' : ''}`}
          >
            <div className="rank">#{region.rank}</div>
            <div className="region-info">
              <div className="region-name">{region.name}</div>
              <div className="region-stats">
                <span className="points">{region.points.toLocaleString()} wisdom</span>
                <span className="achievements">
                  {region.achievements}/{region.totalAchievements} quests
                </span>
              </div>
            </div>
            {region.id === 'Uusimaa' && (
              <div className="home-badge">Your Region</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Leaderboard;
