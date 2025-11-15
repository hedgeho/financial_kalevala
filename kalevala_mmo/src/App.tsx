import FinlandMap from './components/FinlandMap';
import Leaderboard from './components/Leaderboard';
import UserStats from './components/UserStats';
import './App.css';

function App() {
  return (
    <div className="app">
      <FinlandMap />

      <header className="app-header">
        <h1 className="app-title">🔱 Kalevala Financial Quest</h1>
        <p className="app-subtitle">Journey Through Pohjola's Market with Wisdom</p>
      </header>

      <div className="overlay-panels">
        <div className="panel-left">
          <Leaderboard />
        </div>

        <div className="panel-right">
          <UserStats />
        </div>
      </div>
    </div>
  );
}

export default App;
